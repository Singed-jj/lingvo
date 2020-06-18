# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lingvo/core/ops/record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lingvo/core/ops/record.proto',
  package='tensorflow.lingvo',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1clingvo/core/ops/record.proto\x12\x11tensorflow.lingvo\x1a&tensorflow/core/framework/tensor.proto\"\x87\x01\n\x06Record\x12\x35\n\x06\x66ields\x18\x01 \x03(\x0b\x32%.tensorflow.lingvo.Record.FieldsEntry\x1a\x46\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow.TensorProto:\x02\x38\x01')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,])




_RECORD_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='tensorflow.lingvo.Record.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.lingvo.Record.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.lingvo.Record.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=227,
)

_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='tensorflow.lingvo.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='tensorflow.lingvo.Record.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RECORD_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=227,
)

_RECORD_FIELDSENTRY.fields_by_name['value'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_RECORD_FIELDSENTRY.containing_type = _RECORD
_RECORD.fields_by_name['fields'].message_type = _RECORD_FIELDSENTRY
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RECORD_FIELDSENTRY,
    '__module__' : 'lingvo.core.ops.record_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.lingvo.Record.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'lingvo.core.ops.record_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.lingvo.Record)
  })
_sym_db.RegisterMessage(Record)
_sym_db.RegisterMessage(Record.FieldsEntry)


_RECORD_FIELDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
