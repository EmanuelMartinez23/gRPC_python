# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: helloworld.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'helloworld.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"7\n\x0bRequestDate\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\"5\n\tReplyDate\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\"K\n\rRequestAddDay\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\x10\n\x08\x64\x61yToAdd\x18\x04 \x01(\x05\"\x07\n\x05\x45mpty\"$\n\x13\x43\x65ntroDianaResponse\x12\r\n\x05speed\x18\x01 \x01(\x01\"@\n\x0e\x44isparoRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x61ngle\x18\x02 \x01(\x01\x12\r\n\x05speed\x18\x03 \x01(\x01\"%\n\x0f\x44isparoResponse\x12\x12\n\ndifference\x18\x01 \x01(\x01\"7\n\x14MejorDisparoResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x02 \x01(\x01\x32\xa0\x03\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12<\n\x08NextDate\x12\x17.helloworld.RequestDate\x1a\x15.helloworld.ReplyDate\"\x00\x12\x41\n\x0b\x41\x64\x64\x44\x61ysDate\x12\x19.helloworld.RequestAddDay\x1a\x15.helloworld.ReplyDate\"\x00\x12\x45\n\x0f\x44imeCentroDiana\x12\x11.helloworld.Empty\x1a\x1f.helloworld.CentroDianaResponse\x12H\n\rDisparaCannon\x12\x1a.helloworld.DisparoRequest\x1a\x1b.helloworld.DisparoResponse\x12\x43\n\x0cMejorDisparo\x12\x11.helloworld.Empty\x1a .helloworld.MejorDisparoResponseB6\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _globals['_HELLOREQUEST']._serialized_start=32
  _globals['_HELLOREQUEST']._serialized_end=60
  _globals['_HELLOREPLY']._serialized_start=62
  _globals['_HELLOREPLY']._serialized_end=91
  _globals['_REQUESTDATE']._serialized_start=93
  _globals['_REQUESTDATE']._serialized_end=148
  _globals['_REPLYDATE']._serialized_start=150
  _globals['_REPLYDATE']._serialized_end=203
  _globals['_REQUESTADDDAY']._serialized_start=205
  _globals['_REQUESTADDDAY']._serialized_end=280
  _globals['_EMPTY']._serialized_start=282
  _globals['_EMPTY']._serialized_end=289
  _globals['_CENTRODIANARESPONSE']._serialized_start=291
  _globals['_CENTRODIANARESPONSE']._serialized_end=327
  _globals['_DISPAROREQUEST']._serialized_start=329
  _globals['_DISPAROREQUEST']._serialized_end=393
  _globals['_DISPARORESPONSE']._serialized_start=395
  _globals['_DISPARORESPONSE']._serialized_end=432
  _globals['_MEJORDISPARORESPONSE']._serialized_start=434
  _globals['_MEJORDISPARORESPONSE']._serialized_end=489
  _globals['_GREETER']._serialized_start=492
  _globals['_GREETER']._serialized_end=908
# @@protoc_insertion_point(module_scope)
