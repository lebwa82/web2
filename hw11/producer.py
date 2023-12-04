import pika
import myproto_pb2
# time.sleep(5)
conn_params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

message = myproto_pb2.IdMessage(id = 123, hash = "12321")
message22 = message.SerializeToString()
channel.basic_publish(exchange='', routing_key='first-queue', body=message22)
#print("sent ", message)
print('send')
connection.close()
