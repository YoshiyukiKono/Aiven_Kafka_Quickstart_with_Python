from kafka import KafkaProducer
import json
import time
import uuid
import datetime

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        input_file = open(self.input_file, 'r')
        json_load = json.load(input_file)
        for v in json_load:
            message = self.dict_to_binary(v)
            gen_id = str(uuid.uuid4())
            print(f"uuid: {gen_id}")
            print(f"message: {message}")

            #temporary#self.send(self.topic, v)

            #self.send(self.topic, message)
            time.sleep(1)
        #with open(self.input_file) as f:
        #    for line in f:
        #        message = self.dict_to_binary(line)
        #        # TODO send the correct data
        #        self.send()
        #        time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')

def main():
    gen_id = str(uuid.uuid4())
    print(f"uuid: {gen_id}")
    dt_now = datetime.datetime.now()
    print(f"dt_now: {dt_now}")

    cert_folder = "."
    producer_server = ProducerServer("./police-department-calls-for-service.json", 
                                     #"police-department-calls-for-service", bootstrap_servers=['localhost:9092'],
                                     "police-department-calls-for-service", bootstrap_servers=['kafka-test-yoshiyuki-e281.aivencloud.com:10779'],
                                     #value_serializer=lambda m: json.dumps(m).encode('ascii')
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                     security_protocol="SSL",
                                     ssl_cafile=cert_folder+'/ca.pem',
                                     ssl_certfile=cert_folder+'/service.cert',
                                     ssl_keyfile=cert_folder+'/service.key',
                                    )
    producer_server.generate_data()
    
if __name__ == "__main__":
    main()