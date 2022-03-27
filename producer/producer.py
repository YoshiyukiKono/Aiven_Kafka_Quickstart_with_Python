from kafka import KafkaProducer
import json
import time
import uuid
import datetime
import csv

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    # generating a dummy data
    def generate_data(self):
        input_file = open(self.input_file, 'r')
        json_load = json.load(input_file)
        for v in json_load:
            print(f"org json: {v}")


            gen_id = str(uuid.uuid4())
            dt_now = datetime.datetime.now()
            print(f"uuid: {gen_id}")
            print(f"message: {message}")
            v.put("_id",gen_id)
            v.put("_date",dt_now)
            print(f"new json: {v}")

            message = self.dict_to_binary(v)
            #temporary#self.send(self.topic, v)

            #self.send(self.topic, message)
            time.sleep(1)

    # to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')

    def simulate(self):
        input_file = open(self.input_file, 'r')
        f = csv.reader(input_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        try:
            while True:
                print("Simulation running")
                for row in f:
                    print(row)
                    row_dict = dict()
                    gen_id = str(uuid.uuid4())
                    dt_now = datetime.datetime.now().isoformat()
                    row_dict["_id"] = gen_id
                    row_dict["_date"] = dt_now
                    row_dict["sec"] = row[0]
                    row_dict["X"] = row[1]
                    row_dict["Y"] = row[2]
                    row_dict["Z"] = row[3]
                    print(f"new json: {row_dict}")
                    self.send(self.topic, row_dict)

                    #self.send(self.topic, message)
                    time.sleep(1)
        except KeyboardInterrupt as e:
            print("Shutting down")


def main():

    cert_folder = "."
    producer_server = ProducerServer("./HASC1001.csv", 
                                     "sensor", bootstrap_servers=['kafka-test-yoshiyuki-e281.aivencloud.com:10779'],
                                     #value_serializer=lambda m: json.dumps(m).encode('ascii')
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                     security_protocol="SSL",
                                     ssl_cafile=cert_folder+'/ca.pem',
                                     ssl_certfile=cert_folder+'/service.cert',
                                     ssl_keyfile=cert_folder+'/service.key',
                                    )
    producer_server.generate_data()
    producer_server.simulate()

if __name__ == "__main__":
    main()