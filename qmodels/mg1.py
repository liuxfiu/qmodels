import random
import numpy as np
import scipy.stats as stats
import simulus

from qmodels.rng import *

__all__ = ['mg1']

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class mg1(object):
    def __init__(self, sim, mean_iat, svtime_a, svtime_b, dc=None):
        self.sim = sim

        self.inter_arrival_time = expon(mean_iat, sim.rng().randrange(2**32))
        self.service_time = truncnorm(svtime_a, svtime_b, sim.rng().randrange(2**32))

        self.server = sim.resource(collect=dc)
        sim.process(self.gen_arrivals)

    def gen_arrivals(self):
        while True:
            self.sim.sleep(next(self.inter_arrival_time))
            self.sim.process(self.customer)

    def customer(self):
        log.info('%g: customer arrives (num_in_system=%d->%d)' %
                 (sim.now, self.server.num_in_system(), self.server.num_in_system()+1))
        self.server.acquire()
        self.sim.sleep(next(self.service_time))
        log.info('%g: customer arrives (num_in_system=%d->%d)' %
                 (sim.now, self.server.num_in_system(), self.server.num_in_system()-1))
        self.server.release()

def simrun(a, b):
    sim = simulus.simulator() # create an anonymous simulator
    dc = simulus.DataCollector(system_times='dataseries') # statistics collection
    q = mg1(sim, 1.2, a, b, dc) # create m/g/1 queue
    sim.run(1000)
    return dc.system_times.mean()

if __name__ == '__main__':
    # set debug level logging (will print all info messages)
    logging.basicConfig()
    logging.getLogger(__name__).setLevel(logging.DEBUG)

    random.seed(13579) # global random seed
    sim = simulus.simulator('mg1') # create an anonymous simulator instance
    q = mg1(sim, 1.2, 0, 0.8) # create the m/g/1 queue
    sim.run(10)

    # turn logging to warning level (will skip all info messages)
    logging.getLogger(__name__).setLevel(logging.WARNING)

    x = np.linspace(0.1, 3.0, 10)
    print('b\tmean\tlow\thigh')
    for b in x:
        # list of mean wait time from 25 trials
        z = []
        for _ in range(25):
            z.append(simrun(0, b))
        z = np.array(z)

        # the mean, and 5% and 95% percentiles (which would make the
        # 90% confidence interval)
        print('%.1f\t%.4f\t%.4f\t%.4f' %
              (b, z.mean(), np.percentile(z, 5), np.percentile(z, 95)))

