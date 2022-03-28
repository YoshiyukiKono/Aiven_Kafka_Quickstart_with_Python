"""Smilulator of Kafka Producer

    Example:
        ::

            $python producer.py

    Attributes:
        None
"""

from kafka import KafkaProducer
import json
import time
import uuid
import datetime
import csv

class ProducerSimulator(KafkaProducer):
    """kafka-python package `KafkaProducer` inheritance class

    Attributes:
        input_file (str): the path of a csv file having the three columns, i.e. time(sec), X(G), Y(G), Z(G)
        topic (str): Kafka topic name
    """

    def __init__(self, input_file, topic, **kwargs):
        """Constructor of `ProducerSimulator` class

        Args:
            input_file (str): the path of a csv file having the three columns, i.e. time(sec), X(G), Y(G), Z(G)
            topic (str): Kafka topic name
            kwargs: Paremeters for the parent class, `KafkaProducer`
        """

        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def simulate(self):
        """Run the simulation of a Kafka producer"""

        input_file = open(self.input_file, 'r')
        f = csv.reader(input_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        try:
            while True:
                print("Simulation running")
                for row in f:
                    row_dict = dict()
                    gen_id = str(uuid.uuid4())
                    dt_now = datetime.datetime.now().isoformat()
                    row_dict["_id"] = gen_id
                    row_dict["_date"] = dt_now
                    row_dict["sec"] = row[0]
                    row_dict["X"] = row[1]
                    row_dict["Y"] = row[2]
                    row_dict["Z"] = row[3]
                    print(f"json message: {row_dict}")
                    self.send(self.topic, row_dict)

                    time.sleep(1)
        except KeyboardInterrupt as e:
            print("Shutting down")


def main():
    """Entry point of this module"""

    cert_folder = "."
    producer_simulator = ProducerSimulator("./HASC1001.csv", 
                                     "sensor", bootstrap_servers=['YOUR_SERVICE_NAME.aivencloud.com:10779'],
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                     security_protocol="SSL",
                                     ssl_cafile=cert_folder+'/ca.pem',
                                     ssl_certfile=cert_folder+'/service.cert',
                                     ssl_keyfile=cert_folder+'/service.key',
                                    )
    producer_simulator.simulate()

if __name__ == "__main__":
    main()
