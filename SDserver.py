from concurrent import futures
import time

import grpc
import SDpb2
import SDpb2_grpc

class GreeterServicer(SDpb2_grpc.GreeterServicer):


    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = SDpb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply
    

def menu():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = SDpb2_grpc.GreeterStub(channel)
        print("1. Cadastrar cliente")
        #print("2. ParrotSaysHello - Server Side Streaming")

        rpc_call = input("Escolha a opcao: ")

        if rpc_call == "1":
            print("Vamos então cadastrar o cliente:")
            open_serve()
#***************************************************************************************

def open_serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SDpb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    menu()
    