import grpc
from myproto_pb2 import MyRequest, MyResponse, IdMessage
from myproto_pb2_grpc import TodoServiceStub

channel = grpc.insecure_channel("localhost:50051")
client = TodoServiceStub(channel)
request = MyRequest(
    content = ['123', "abc"], id_request=IdMessage(id = 2, hash = "asdsa"), count=1
 ) 
response = client.SendMessage(request)
print(response.content)
print(response.id_response)