import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qmodels",
    version="1.0.1",
    author="Jason Liu",
    author_email="jasonxliu2010@gmail.com",
    description="Simulation of Queuing Models with Simulus",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://qmodels.readthedocs.io/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['simulus', 'numpy', 'scipy', 'matplotlib'],
    python_requires='>=3.5',
)
