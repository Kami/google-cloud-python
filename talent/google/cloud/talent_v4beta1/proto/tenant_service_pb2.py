# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/tenant_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.talent_v4beta1.proto import (
    common_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2,
)
from google.cloud.talent_v4beta1.proto import (
    tenant_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/tenant_service.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.talent.v4beta1B\022TenantServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS"
    ),
    serialized_pb=_b(
        '\n6google/cloud/talent_v4beta1/proto/tenant_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/talent_v4beta1/proto/common.proto\x1a.google/cloud/talent_v4beta1/proto/tenant.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"d\n\x13\x43reateTenantRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x38\n\x06tenant\x18\x02 \x01(\x0b\x32#.google.cloud.talent.v4beta1.TenantB\x03\xe0\x41\x02"%\n\x10GetTenantRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02"\x80\x01\n\x13UpdateTenantRequest\x12\x38\n\x06tenant\x18\x01 \x01(\x0b\x32#.google.cloud.talent.v4beta1.TenantB\x03\xe0\x41\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask"(\n\x13\x44\x65leteTenantRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02"P\n\x12ListTenantsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\xa5\x01\n\x13ListTenantsResponse\x12\x34\n\x07tenants\x18\x01 \x03(\x0b\x32#.google.cloud.talent.v4beta1.Tenant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12?\n\x08metadata\x18\x03 \x01(\x0b\x32-.google.cloud.talent.v4beta1.ResponseMetadata2\xf0\x06\n\rTenantService\x12\x96\x01\n\x0c\x43reateTenant\x12\x30.google.cloud.talent.v4beta1.CreateTenantRequest\x1a#.google.cloud.talent.v4beta1.Tenant"/\x82\xd3\xe4\x93\x02)"$/v4beta1/{parent=projects/*}/tenants:\x01*\x12\x8d\x01\n\tGetTenant\x12-.google.cloud.talent.v4beta1.GetTenantRequest\x1a#.google.cloud.talent.v4beta1.Tenant",\x82\xd3\xe4\x93\x02&\x12$/v4beta1/{name=projects/*/tenants/*}\x12\x9d\x01\n\x0cUpdateTenant\x12\x30.google.cloud.talent.v4beta1.UpdateTenantRequest\x1a#.google.cloud.talent.v4beta1.Tenant"6\x82\xd3\xe4\x93\x02\x30\x32+/v4beta1/{tenant.name=projects/*/tenants/*}:\x01*\x12\x86\x01\n\x0c\x44\x65leteTenant\x12\x30.google.cloud.talent.v4beta1.DeleteTenantRequest\x1a\x16.google.protobuf.Empty",\x82\xd3\xe4\x93\x02&*$/v4beta1/{name=projects/*/tenants/*}\x12\x9e\x01\n\x0bListTenants\x12/.google.cloud.talent.v4beta1.ListTenantsRequest\x1a\x30.google.cloud.talent.v4beta1.ListTenantsResponse",\x82\xd3\xe4\x93\x02&\x12$/v4beta1/{parent=projects/*}/tenants\x1al\xca\x41\x13jobs.googleapis.com\xd2\x41Shttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsB\x80\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x12TenantServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_CREATETENANTREQUEST = _descriptor.Descriptor(
    name="CreateTenantRequest",
    full_name="google.cloud.talent.v4beta1.CreateTenantRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.CreateTenantRequest.parent",
            index=0,
            number=1,
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
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="tenant",
            full_name="google.cloud.talent.v4beta1.CreateTenantRequest.tenant",
            index=1,
            number=2,
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
            serialized_options=_b("\340A\002"),
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
    serialized_start=334,
    serialized_end=434,
)


_GETTENANTREQUEST = _descriptor.Descriptor(
    name="GetTenantRequest",
    full_name="google.cloud.talent.v4beta1.GetTenantRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.GetTenantRequest.name",
            index=0,
            number=1,
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
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=436,
    serialized_end=473,
)


_UPDATETENANTREQUEST = _descriptor.Descriptor(
    name="UpdateTenantRequest",
    full_name="google.cloud.talent.v4beta1.UpdateTenantRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="tenant",
            full_name="google.cloud.talent.v4beta1.UpdateTenantRequest.tenant",
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
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="google.cloud.talent.v4beta1.UpdateTenantRequest.update_mask",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=476,
    serialized_end=604,
)


_DELETETENANTREQUEST = _descriptor.Descriptor(
    name="DeleteTenantRequest",
    full_name="google.cloud.talent.v4beta1.DeleteTenantRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.DeleteTenantRequest.name",
            index=0,
            number=1,
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
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=606,
    serialized_end=646,
)


_LISTTENANTSREQUEST = _descriptor.Descriptor(
    name="ListTenantsRequest",
    full_name="google.cloud.talent.v4beta1.ListTenantsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.ListTenantsRequest.parent",
            index=0,
            number=1,
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
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.talent.v4beta1.ListTenantsRequest.page_token",
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
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.talent.v4beta1.ListTenantsRequest.page_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
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
    serialized_start=648,
    serialized_end=728,
)


_LISTTENANTSRESPONSE = _descriptor.Descriptor(
    name="ListTenantsResponse",
    full_name="google.cloud.talent.v4beta1.ListTenantsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="tenants",
            full_name="google.cloud.talent.v4beta1.ListTenantsResponse.tenants",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.cloud.talent.v4beta1.ListTenantsResponse.next_page_token",
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
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.talent.v4beta1.ListTenantsResponse.metadata",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=731,
    serialized_end=896,
)

_CREATETENANTREQUEST.fields_by_name[
    "tenant"
].message_type = google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2._TENANT
_UPDATETENANTREQUEST.fields_by_name[
    "tenant"
].message_type = google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2._TENANT
_UPDATETENANTREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTTENANTSRESPONSE.fields_by_name[
    "tenants"
].message_type = google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2._TENANT
_LISTTENANTSRESPONSE.fields_by_name[
    "metadata"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2._RESPONSEMETADATA
)
DESCRIPTOR.message_types_by_name["CreateTenantRequest"] = _CREATETENANTREQUEST
DESCRIPTOR.message_types_by_name["GetTenantRequest"] = _GETTENANTREQUEST
DESCRIPTOR.message_types_by_name["UpdateTenantRequest"] = _UPDATETENANTREQUEST
DESCRIPTOR.message_types_by_name["DeleteTenantRequest"] = _DELETETENANTREQUEST
DESCRIPTOR.message_types_by_name["ListTenantsRequest"] = _LISTTENANTSREQUEST
DESCRIPTOR.message_types_by_name["ListTenantsResponse"] = _LISTTENANTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateTenantRequest = _reflection.GeneratedProtocolMessageType(
    "CreateTenantRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CREATETENANTREQUEST,
        __module__="google.cloud.talent_v4beta1.proto.tenant_service_pb2",
        __doc__="""The Request of the CreateTenant method.
  
  
  Attributes:
      parent:
          Required. Resource name of the project under which the tenant
          is created.  The format is "projects/{project\_id}", for
          example, "projects/foo".
      tenant:
          Required. The tenant to be created.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.CreateTenantRequest)
    ),
)
_sym_db.RegisterMessage(CreateTenantRequest)

GetTenantRequest = _reflection.GeneratedProtocolMessageType(
    "GetTenantRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GETTENANTREQUEST,
        __module__="google.cloud.talent_v4beta1.proto.tenant_service_pb2",
        __doc__="""Request for getting a tenant by name.
  
  
  Attributes:
      name:
          Required. The resource name of the tenant to be retrieved.
          The format is "projects/{project\_id}/tenants/{tenant\_id}",
          for example, "projects/foo/tenants/bar".
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.GetTenantRequest)
    ),
)
_sym_db.RegisterMessage(GetTenantRequest)

UpdateTenantRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateTenantRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_UPDATETENANTREQUEST,
        __module__="google.cloud.talent_v4beta1.proto.tenant_service_pb2",
        __doc__="""Request for updating a specified tenant.
  
  
  Attributes:
      tenant:
          Required. The tenant resource to replace the current resource
          in the system.
      update_mask:
          Strongly recommended for the best service experience.  If [upd
          ate\_mask][google.cloud.talent.v4beta1.UpdateTenantRequest.upd
          ate\_mask] is provided, only the specified fields in [tenant][
          google.cloud.talent.v4beta1.UpdateTenantRequest.tenant] are
          updated. Otherwise all the fields are updated.  A field mask
          to specify the tenant fields to be updated. Only top level
          fields of [Tenant][google.cloud.talent.v4beta1.Tenant] are
          supported.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.UpdateTenantRequest)
    ),
)
_sym_db.RegisterMessage(UpdateTenantRequest)

DeleteTenantRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteTenantRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELETETENANTREQUEST,
        __module__="google.cloud.talent_v4beta1.proto.tenant_service_pb2",
        __doc__="""Request to delete a tenant.
  
  
  Attributes:
      name:
          Required. The resource name of the tenant to be deleted.  The
          format is "projects/{project\_id}/tenants/{tenant\_id}", for
          example, "projects/foo/tenants/bar".
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.DeleteTenantRequest)
    ),
)
_sym_db.RegisterMessage(DeleteTenantRequest)

ListTenantsRequest = _reflection.GeneratedProtocolMessageType(
    "ListTenantsRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTTENANTSREQUEST,
        __module__="google.cloud.talent_v4beta1.proto.tenant_service_pb2",
        __doc__="""List tenants for which the client has ACL visibility.
  
  
  Attributes:
      parent:
          Required. Resource name of the project under which the tenant
          is created.  The format is "projects/{project\_id}", for
          example, "projects/foo".
      page_token:
          The starting indicator from which to return results.
      page_size:
          The maximum number of tenants to be returned, at most 100.
          Default is 100 if a non-positive number is provided.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListTenantsRequest)
    ),
)
_sym_db.RegisterMessage(ListTenantsRequest)

ListTenantsResponse = _reflection.GeneratedProtocolMessageType(
    "ListTenantsResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTTENANTSRESPONSE,
        __module__="google.cloud.talent_v4beta1.proto.tenant_service_pb2",
        __doc__="""The List tenants response object.
  
  
  Attributes:
      tenants:
          Tenants for the current client.
      next_page_token:
          A token to retrieve the next page of results.
      metadata:
          Additional information for the API invocation, such as the
          request tracking id.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListTenantsResponse)
    ),
)
_sym_db.RegisterMessage(ListTenantsResponse)


DESCRIPTOR._options = None
_CREATETENANTREQUEST.fields_by_name["parent"]._options = None
_CREATETENANTREQUEST.fields_by_name["tenant"]._options = None
_GETTENANTREQUEST.fields_by_name["name"]._options = None
_UPDATETENANTREQUEST.fields_by_name["tenant"]._options = None
_DELETETENANTREQUEST.fields_by_name["name"]._options = None
_LISTTENANTSREQUEST.fields_by_name["parent"]._options = None

_TENANTSERVICE = _descriptor.ServiceDescriptor(
    name="TenantService",
    full_name="google.cloud.talent.v4beta1.TenantService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A\023jobs.googleapis.com\322AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs"
    ),
    serialized_start=899,
    serialized_end=1779,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateTenant",
            full_name="google.cloud.talent.v4beta1.TenantService.CreateTenant",
            index=0,
            containing_service=None,
            input_type=_CREATETENANTREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2._TENANT,
            serialized_options=_b(
                '\202\323\344\223\002)"$/v4beta1/{parent=projects/*}/tenants:\001*'
            ),
        ),
        _descriptor.MethodDescriptor(
            name="GetTenant",
            full_name="google.cloud.talent.v4beta1.TenantService.GetTenant",
            index=1,
            containing_service=None,
            input_type=_GETTENANTREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2._TENANT,
            serialized_options=_b(
                "\202\323\344\223\002&\022$/v4beta1/{name=projects/*/tenants/*}"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="UpdateTenant",
            full_name="google.cloud.talent.v4beta1.TenantService.UpdateTenant",
            index=2,
            containing_service=None,
            input_type=_UPDATETENANTREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_tenant__pb2._TENANT,
            serialized_options=_b(
                "\202\323\344\223\00202+/v4beta1/{tenant.name=projects/*/tenants/*}:\001*"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="DeleteTenant",
            full_name="google.cloud.talent.v4beta1.TenantService.DeleteTenant",
            index=3,
            containing_service=None,
            input_type=_DELETETENANTREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=_b(
                "\202\323\344\223\002&*$/v4beta1/{name=projects/*/tenants/*}"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="ListTenants",
            full_name="google.cloud.talent.v4beta1.TenantService.ListTenants",
            index=4,
            containing_service=None,
            input_type=_LISTTENANTSREQUEST,
            output_type=_LISTTENANTSRESPONSE,
            serialized_options=_b(
                "\202\323\344\223\002&\022$/v4beta1/{parent=projects/*}/tenants"
            ),
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_TENANTSERVICE)

DESCRIPTOR.services_by_name["TenantService"] = _TENANTSERVICE

# @@protoc_insertion_point(module_scope)
