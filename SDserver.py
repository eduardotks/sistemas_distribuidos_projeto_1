from concurrent import futures
from msvcrt import kbhit
import time
import grpc
import SDpb2
import SDpb2_grpc
import RWLock
import ast
import threading
import datetime
import logging
lock = RWLock.RWLock()

class GreeterServicer(SDpb2_grpc.GreeterServicer):
    def set(self, request, context):            
        lock.writer_acquire()

        try: 
            if request.chave in dicionario:
                return SDpb2.MessageReply(e='ERROR')
            else:
                dicionario[request.chave] = (1)
                print(dicionario)

                return SDpb2.MessageReply(e='SUCCESS', id = dicionario[request.chave][0])
        finally:
            lock.writer_release()


    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = SDpb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply
    

def menu():
    while True:
        channel = grpc.insecure_channel('localhost:50051')
        stub = SDpb2_grpc.GreeterServicer(channel)

        print("1 - Cadastrar cliente")
        #print("2 - ParrotSaysHello - Server Side Streaming")
        print("0 - Sair do programa")

        inp = input("Escolha a opcao: ")

        if inp.lower() == '0':
            break
        if inp == "1":
            valor_digitado = input("Digite o valor: ")
            response = stub.set(SDpb2_grpc.HelloRequest(chave = valor_digitado))
            print("Inserção: " + response.e + " - " + str(response.id))
        else:
            print('Opção inválida!')
            print('\n')



#realiza leitura do arquivo
def read_db():
    lock.writer_acquire
    try:
        f = open('file.txt','r')
        global dicionario
        dicionario = ast.literal_eval(f.read())
        
    finally:
        lock.writer_release

#realiza escrita no arquivo
def write_db(t):
    while True:
        time.sleep(t)
        lock.writer_acquire()
        try:
            f = open('file.txt','w')
            f.write(str(dicionario))
            f.close()
            
        finally:
            lock.writer_release()

class ThreadWrite(threading.Thread):
    def __init__(self,counter):
        threading.Thread.__init__(self)
        self.counter = counter
    def run(self):
        print('Starting ThreadWrite')
        write_db(self.counter)

class ThreadRead (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)

   def run(self):
      print ("Starting ThreadRead")
      read_db()
      print ("Exiting ThreadRead")


#***************************************************************************************

def open_serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SDpb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    menu()
    logging.basicConfig()
    thread_read = ThreadRead()
    