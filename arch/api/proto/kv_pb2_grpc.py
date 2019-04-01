#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import kv_pb2 as kv__pb2


class KVServiceStub(object):
  """service for actual storage operation
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.createIfAbsent = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/createIfAbsent',
        request_serializer=kv__pb2.CreateTableInfo.SerializeToString,
        response_deserializer=kv__pb2.CreateTableInfo.FromString,
        )
    self.put = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/put',
        request_serializer=kv__pb2.Operand.SerializeToString,
        response_deserializer=kv__pb2.Empty.FromString,
        )
    self.putIfAbsent = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/putIfAbsent',
        request_serializer=kv__pb2.Operand.SerializeToString,
        response_deserializer=kv__pb2.Operand.FromString,
        )
    self.putAll = channel.stream_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/putAll',
        request_serializer=kv__pb2.Operand.SerializeToString,
        response_deserializer=kv__pb2.Empty.FromString,
        )
    self.delete = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/delete',
        request_serializer=kv__pb2.Operand.SerializeToString,
        response_deserializer=kv__pb2.Operand.FromString,
        )
    self.get = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/get',
        request_serializer=kv__pb2.Operand.SerializeToString,
        response_deserializer=kv__pb2.Operand.FromString,
        )
    self.iterate = channel.unary_stream(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/iterate',
        request_serializer=kv__pb2.Range.SerializeToString,
        response_deserializer=kv__pb2.Operand.FromString,
        )
    self.destroy = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/destroy',
        request_serializer=kv__pb2.Empty.SerializeToString,
        response_deserializer=kv__pb2.Empty.FromString,
        )
    self.destroyAll = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/destroyAll',
        request_serializer=kv__pb2.Empty.SerializeToString,
        response_deserializer=kv__pb2.Empty.FromString,
        )
    self.count = channel.unary_unary(
        '/com.webank.ai.fate.api.eggroll.storage.KVService/count',
        request_serializer=kv__pb2.Empty.SerializeToString,
        response_deserializer=kv__pb2.Count.FromString,
        )


class KVServiceServicer(object):
  """service for actual storage operation
  """

  def createIfAbsent(self, request, context):
    """create a table
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def put(self, request, context):
    """put an entry to table
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def putIfAbsent(self, request, context):
    """put an entry to table if absent
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def putAll(self, request_iterator, context):
    """put entries to table (entries will be streaming in)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    """delete an entry from table
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request, context):
    """get an entry from table
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def iterate(self, request, context):
    """iterate through a table. Response entries are ordered
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def destroy(self, request, context):
    """destroy a table
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def destroyAll(self, request, context):
    """destroy multiple tables
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def count(self, request, context):
    """count record amount of a table
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KVServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'createIfAbsent': grpc.unary_unary_rpc_method_handler(
          servicer.createIfAbsent,
          request_deserializer=kv__pb2.CreateTableInfo.FromString,
          response_serializer=kv__pb2.CreateTableInfo.SerializeToString,
      ),
      'put': grpc.unary_unary_rpc_method_handler(
          servicer.put,
          request_deserializer=kv__pb2.Operand.FromString,
          response_serializer=kv__pb2.Empty.SerializeToString,
      ),
      'putIfAbsent': grpc.unary_unary_rpc_method_handler(
          servicer.putIfAbsent,
          request_deserializer=kv__pb2.Operand.FromString,
          response_serializer=kv__pb2.Operand.SerializeToString,
      ),
      'putAll': grpc.stream_unary_rpc_method_handler(
          servicer.putAll,
          request_deserializer=kv__pb2.Operand.FromString,
          response_serializer=kv__pb2.Empty.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=kv__pb2.Operand.FromString,
          response_serializer=kv__pb2.Operand.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=kv__pb2.Operand.FromString,
          response_serializer=kv__pb2.Operand.SerializeToString,
      ),
      'iterate': grpc.unary_stream_rpc_method_handler(
          servicer.iterate,
          request_deserializer=kv__pb2.Range.FromString,
          response_serializer=kv__pb2.Operand.SerializeToString,
      ),
      'destroy': grpc.unary_unary_rpc_method_handler(
          servicer.destroy,
          request_deserializer=kv__pb2.Empty.FromString,
          response_serializer=kv__pb2.Empty.SerializeToString,
      ),
      'destroyAll': grpc.unary_unary_rpc_method_handler(
          servicer.destroyAll,
          request_deserializer=kv__pb2.Empty.FromString,
          response_serializer=kv__pb2.Empty.SerializeToString,
      ),
      'count': grpc.unary_unary_rpc_method_handler(
          servicer.count,
          request_deserializer=kv__pb2.Empty.FromString,
          response_serializer=kv__pb2.Count.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.eggroll.storage.KVService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))