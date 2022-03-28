# Python Kafka Producer


## Overview

The next step is to run a simulation program that feeds data to the Aiven Kafka cluster.

The program has the role of Kafka Producer. In this tutorial, we will not create a Kafka Consumer because we will use the features of the Aiven Web Console to check the data sent to the Kafka topic.

## Data

Open data provided by [HASC (Human Activity Sensing Consortium)](http://hasc.jp/) will be used.

HASC is a consortium that aims to build a large-scale database with wearable sensors for understanding human behavior.

The program uses one of the acceleration data ([HASC1001.csv](../producer/HASC1001.csv)) that can be downloaded from [2010corpus](http://hasc.jp/hc2010/HASC2010corpus/hasc2010corpus-en.html).

## specification

The simulator sends a JSON-formatted message to the Kafka topic.

### Sensor data

The data in csv format has the following data model (header is not included).

```
[time (sec)], [X-axis (G)], [Y-axis (G)], [Z-axis (G)]
```

### Metadata

In addition to the sensor data, the program adds the following metadata to the message:

 - Message-ID (UUID)
 - Transmission date and time

## Program

The tutorial provides a Python program ([producer.py](../producer/producer.py)).

### Connection information

When using the program, you need to edit the connection information to the Aiven Kafka cluster.

Rename the argument to the constructor of the` ProducerSimilator` class, `bootstrap_servers`,  to your Aiven Kafka cluster's URI.

```
    producer_simulator = ProducerSimulator ("./HASC1001.csv",
                                     "sensor", bootstrap_servers = ['YOUR_SERVICE_NAME.aivencloud.com:10779'],
                                     value_serializer = lambda x: json.dumps (x) .encode ('utf-8'),
                                     security_protocol = "SSL",
                                     ssl_cafile = cert_folder +'/ca.pem',
                                     ssl_certfile = cert_folder +'/service.cert',
                                     ssl_keyfile = cert_folder +'/service.key',
                                    )
```

Also, use the following files obtained in the previous step. Place it in the same location as producer.py.

- ca.pem
- service.cert
- service.key



## Run

Run the Python program as follows.

```
> python producer.py
```

When executed, the message to be sent will be displayed on the console as shown below.

```
Simulation running
json message: {'_id': '438e5cb9-beab-42e8-8bf8-2a1f6fce6e85','_date': '2022-03-27T11: 37: 32.919642','sec': '965 6.196248','X':'- 0.905609','Y':'-0.199234','Z': '0.144897'}
json message: {'_id':'c68101b0-fec4-4854-9451-2840699eb072','_date': '2022-03-27T11: 37: 33.934667','sec': '9656.206375','X':'- 0.905609','Y':'-0.163010','Z': '0.181122'}
json message: {'_id': '04946e55-f0c0-4eb0-96be-6ab2230d140f','_date': '2022-03-27T11: 37: 34.935639','sec': '965 6.217099','X':'- 0.923721','Y':'-0.126785','Z': '0.217346'}
json message: {'_id': '1c056ea8-44d1-4f18-b89e-671eabc242df','_date': '2022-03-27T11: 37: 35.936760','sec': '965 6.226533','X':'- 0.905609','Y':'-0.090561','Z': '0.144897'}
```


Press Ctrl + C to stop the program.


[Back to Table of Contents](./contents_en.md)
