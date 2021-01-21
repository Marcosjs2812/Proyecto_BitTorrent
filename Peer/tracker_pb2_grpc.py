# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tracker_pb2 as tracker__pb2


class SwarmStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSwarm = channel.unary_unary(
                '/Swarm/CreateSwarm',
                request_serializer=tracker__pb2.SwarmNode.SerializeToString,
                response_deserializer=tracker__pb2.Status.FromString,
                )
        self.RequestSwarm = channel.unary_unary(
                '/Swarm/RequestSwarm',
                request_serializer=tracker__pb2.SwarmData.SerializeToString,
                response_deserializer=tracker__pb2.Seeders.FromString,
                )
        self.AddToSwarm = channel.unary_unary(
                '/Swarm/AddToSwarm',
                request_serializer=tracker__pb2.SwarmNode.SerializeToString,
                response_deserializer=tracker__pb2.Status.FromString,
                )


class SwarmServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSwarm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestSwarm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToSwarm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SwarmServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSwarm': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSwarm,
                    request_deserializer=tracker__pb2.SwarmNode.FromString,
                    response_serializer=tracker__pb2.Status.SerializeToString,
            ),
            'RequestSwarm': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestSwarm,
                    request_deserializer=tracker__pb2.SwarmData.FromString,
                    response_serializer=tracker__pb2.Seeders.SerializeToString,
            ),
            'AddToSwarm': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToSwarm,
                    request_deserializer=tracker__pb2.SwarmNode.FromString,
                    response_serializer=tracker__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Swarm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Swarm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSwarm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Swarm/CreateSwarm',
            tracker__pb2.SwarmNode.SerializeToString,
            tracker__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestSwarm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Swarm/RequestSwarm',
            tracker__pb2.SwarmData.SerializeToString,
            tracker__pb2.Seeders.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToSwarm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Swarm/AddToSwarm',
            tracker__pb2.SwarmNode.SerializeToString,
            tracker__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)