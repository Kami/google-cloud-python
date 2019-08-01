# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/mutation_record.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/mutation_record.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\023MutationRecordProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3"
    ),
    serialized_pb=_b(
        '\n6google/cloud/monitoring_v3/proto/mutation_record.proto\x12\x14google.monitoring.v3\x1a\x1fgoogle/protobuf/timestamp.proto"U\n\x0eMutationRecord\x12/\n\x0bmutate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nmutated_by\x18\x02 \x01(\tB\xab\x01\n\x18\x63om.google.monitoring.v3B\x13MutationRecordProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3'
    ),
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR],
)


_MUTATIONRECORD = _descriptor.Descriptor(
    name="MutationRecord",
    full_name="google.monitoring.v3.MutationRecord",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="mutate_time",
            full_name="google.monitoring.v3.MutationRecord.mutate_time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="mutated_by",
            full_name="google.monitoring.v3.MutationRecord.mutated_by",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=113,
    serialized_end=198,
)

_MUTATIONRECORD.fields_by_name[
    "mutate_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name["MutationRecord"] = _MUTATIONRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MutationRecord = _reflection.GeneratedProtocolMessageType(
    "MutationRecord",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MUTATIONRECORD,
        __module__="google.cloud.monitoring_v3.proto.mutation_record_pb2",
        __doc__="""Describes a change made to a configuration.
  
  
  Attributes:
      mutate_time:
          When the change occurred.
      mutated_by:
          The email address of the user making the change.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.MutationRecord)
    ),
)
_sym_db.RegisterMessage(MutationRecord)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
