# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tracker.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rtracker.proto\"O\n\tSwarmNode\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x10\n\x08seederIP\x18\x02 \x01(\t\x12\x12\n\nseederPort\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\t\"\x19\n\x06Status\x12\x0f\n\x07\x64\x65tails\x18\x01 \x01(\t\"Q\n\tSwarmData\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x11\n\tleecherIP\x18\x02 \x01(\t\x12\x13\n\x0bleecherPort\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t2y\n\x05Swarm\x12$\n\x0b\x43reateSwarm\x12\n.SwarmNode\x1a\x07.Status\"\x00\x12%\n\x0cRequestSwarm\x12\n.SwarmData\x1a\x07.Status\"\x00\x12#\n\nAddToSwarm\x12\n.SwarmNode\x1a\x07.Status\"\x00\x62\x06proto3'
)




_SWARMNODE = _descriptor.Descriptor(
  name='SwarmNode',
  full_name='SwarmNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='SwarmNode.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seederIP', full_name='SwarmNode.seederIP', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seederPort', full_name='SwarmNode.seederPort', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='SwarmNode.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=96,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='Status.details', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=123,
)


_SWARMDATA = _descriptor.Descriptor(
  name='SwarmData',
  full_name='SwarmData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='SwarmData.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leecherIP', full_name='SwarmData.leecherIP', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leecherPort', full_name='SwarmData.leecherPort', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='SwarmData.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['SwarmNode'] = _SWARMNODE
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['SwarmData'] = _SWARMDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SwarmNode = _reflection.GeneratedProtocolMessageType('SwarmNode', (_message.Message,), {
  'DESCRIPTOR' : _SWARMNODE,
  '__module__' : 'tracker_pb2'
  # @@protoc_insertion_point(class_scope:SwarmNode)
  })
_sym_db.RegisterMessage(SwarmNode)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'tracker_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  })
_sym_db.RegisterMessage(Status)

SwarmData = _reflection.GeneratedProtocolMessageType('SwarmData', (_message.Message,), {
  'DESCRIPTOR' : _SWARMDATA,
  '__module__' : 'tracker_pb2'
  # @@protoc_insertion_point(class_scope:SwarmData)
  })
_sym_db.RegisterMessage(SwarmData)



_SWARM = _descriptor.ServiceDescriptor(
  name='Swarm',
  full_name='Swarm',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=208,
  serialized_end=329,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateSwarm',
    full_name='Swarm.CreateSwarm',
    index=0,
    containing_service=None,
    input_type=_SWARMNODE,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestSwarm',
    full_name='Swarm.RequestSwarm',
    index=1,
    containing_service=None,
    input_type=_SWARMDATA,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddToSwarm',
    full_name='Swarm.AddToSwarm',
    index=2,
    containing_service=None,
    input_type=_SWARMNODE,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SWARM)

DESCRIPTOR.services_by_name['Swarm'] = _SWARM

# @@protoc_insertion_point(module_scope)
