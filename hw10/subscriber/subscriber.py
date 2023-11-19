import pika
from myproto_pb2 import MyRequest, MyResponse, IdMessage

conn_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

def callback(ch, method, properties, body):
    message = IdMessage()
    message.ParseFromString(body)
    print("body = ", message.id, message.hash)

channel.basic_consume(on_message_callback = callback, queue='first-queue', auto_ack=True)

channel.start_consuming()
