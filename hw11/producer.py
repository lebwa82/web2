# pylint: disable=missing-module-docstring
import pika
from myproto_pb2 import IdMessage # pylint: disable=no-name-in-module

conn_params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

message = IdMessage(id = 123, hash = "12321")
message22 = message.SerializeToString()
channel.basic_publish(exchange='', routing_key='first-queue', body=message22)
#print("sent ", message)
print('send')
connection.close()
