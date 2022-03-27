## Python programming environment

Describes the Python programming environment used in the tutorial.

The confirmed dependencies for this tutorial are:

 - Python: 3.10.0
 - kafka-python: 2.0.2

If you are familiar with Python programming, you can also move on to the next step.

The following description is based on what was confirmed in the Windows environment.
It notes the differences due to known environments.


### Virtual environment

Describes how to set up a virtual environment using conda in an environment where Anaconda is installed.
Please refer to [Documentation] (https://docs.anaconda.com/anaconda/install/index.html) for the installation of Anaconda.

Create a virtual environment as shown below.

```
> conda create -n aiven python = 3
```

Start the created virtual environment.

```
> activate aiven
```

For MacOS, it will be as follows.

```
$ source activate aiven
```

### Package installation

Install kafka-python on the virtual environment.

```
(aiven) ...> pip install kafka-python
```


[Back to Tabele of Contents](./contents_en.md)
