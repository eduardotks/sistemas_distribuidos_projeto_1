# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import SDpb2 as greet__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        self.set = channel.unary_unary(
                '/projeto.Greeter/set',
                request_serializer=projeto__pb2.ChaveValor.SerializeToString,
                response_deserializer=projeto__pb2.MessageReply.FromString,
        )
        self.SayHello = channel.unary_unary(
                '/greet.Greeter/SayHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )



class GreeterServicer(object):
    """The greeting service definition.
    """
    def set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def SayHello(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')



def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'set': grpc.unary_unary_rpc_method_handler(
                servicer.set,
                request_deserializer=projeto__pb2.ChaveValor.FromString,
                response_serializer=projeto__pb2.MessageReply.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """
    @staticmethod
    def set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/projeto.Greeter/set',
            projeto__pb2.ChaveValor.SerializeToString,
            projeto__pb2.MessageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/SayHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


