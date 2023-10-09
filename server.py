import grpc
from concurrent import futures
import myproto_pb2
from myproto_pb2 import MyRequest, MyResponse, IdMessage
import myproto_pb2_grpc

class MyService(myproto_pb2_grpc.TodoServiceServicer):
    def SendMessage(self, request, context):
        response = myproto_pb2.MyResponse(id_response = IdMessage(id = 2, hash = "fghgf"), content = ['1', '2', '3'])
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myproto_pb2_grpc.add_TodoServiceServicer_to_server(
        MyService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()