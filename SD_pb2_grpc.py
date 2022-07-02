# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import SD_pb2 as SD__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.insert_client = channel.unary_unary(
                '/SD.Greeter/insert_client',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.update_client = channel.unary_unary(
                '/SD.Greeter/update_client',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.recovery_client = channel.unary_unary(
                '/SD.Greeter/recovery_client',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.delete_client = channel.unary_unary(
                '/SD.Greeter/delete_client',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.insert_task = channel.unary_unary(
                '/SD.Greeter/insert_task',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.update_task = channel.unary_unary(
                '/SD.Greeter/update_task',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.list_task = channel.unary_unary(
                '/SD.Greeter/list_task',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )
        self.delete_task = channel.unary_unary(
                '/SD.Greeter/delete_task',
                request_serializer=SD__pb2.HelloRequest.SerializeToString,
                response_deserializer=SD__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def insert_client(self, request, context):
        """Servidor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_client(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recovery_client(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_client(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insert_task(self, request, context):
        """Cliente
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_task(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list_task(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_task(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'insert_client': grpc.unary_unary_rpc_method_handler(
                    servicer.insert_client,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'update_client': grpc.unary_unary_rpc_method_handler(
                    servicer.update_client,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'recovery_client': grpc.unary_unary_rpc_method_handler(
                    servicer.recovery_client,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'delete_client': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_client,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'insert_task': grpc.unary_unary_rpc_method_handler(
                    servicer.insert_task,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'update_task': grpc.unary_unary_rpc_method_handler(
                    servicer.update_task,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'list_task': grpc.unary_unary_rpc_method_handler(
                    servicer.list_task,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
            'delete_task': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_task,
                    request_deserializer=SD__pb2.HelloRequest.FromString,
                    response_serializer=SD__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SD.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def insert_client(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/insert_client',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_client(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/update_client',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recovery_client(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/recovery_client',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_client(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/delete_client',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insert_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/insert_task',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/update_task',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/list_task',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SD.Greeter/delete_task',
            SD__pb2.HelloRequest.SerializeToString,
            SD__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
