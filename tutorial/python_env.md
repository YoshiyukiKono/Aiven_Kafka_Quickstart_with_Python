## Python programming environment

This section describes the Python programming environment used in the tutorial.

The confirmed dependencies for this tutorial are:

 - Python: 3.10.0
 - kafka-python: 2.0.2


The following description is based on what was confirmed in the Windows environment.
It notes the known differences due to OS.


### Virtual environment

Here it will be explained how to set up a virtual environment using `conda` command in the environment where Anaconda is installed.

If you are familiar with Python programming, you may move on to the next step.

Please refer to [Documentation](https://docs.anaconda.com/anaconda/install/index.html) for the installation of Anaconda.

Create a virtual environment as shown below.

```
> conda create -n aiven python = 3
```

Start the created virtual environment.

```
> activate aiven
```

For macOS, it will be as follows.

```
$ source activate aiven
```

### Package installation

Install [kafka-python](https://kafka-python.readthedocs.io/) package on the virtual environment.

```
(aiven) ...> pip install kafka-python
```


[Back to Table of Contents](./contents_en.md)
