import pika
from myproto_pb2 import MyRequest, MyResponse, IdMessage
import time 

print("i am sub")
time.sleep(5)
conn_params = pika.ConnectionParameters('rabbitmq')
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

#channel.queue_declare(queue='first-queue')

def callback(ch, method, properties, body):
    message = IdMessage()
    message.ParseFromString(body)
    print("body = ", message.id, message.hash)

print("присоединился к каналу")
channel.basic_consume(on_message_callback = callback, queue='first-queue', auto_ack=True)
print("начал слушать")
channel.start_consuming()
print("слушаю...")
