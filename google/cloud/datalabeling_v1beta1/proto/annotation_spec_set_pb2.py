# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling_v1beta1/proto/annotation_spec_set.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/datalabeling_v1beta1/proto/annotation_spec_set.proto",
    package="google.cloud.datalabeling.v1beta1",
    syntax="proto3",
    serialized_options=b"\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling",
    serialized_pb=b'\nAgoogle/cloud/datalabeling_v1beta1/proto/annotation_spec_set.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto"\xa6\x02\n\x11\x41nnotationSpecSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12K\n\x10\x61nnotation_specs\x18\x04 \x03(\x0b\x32\x31.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12\x1a\n\x12\x62locking_resources\x18\x05 \x03(\t:o\xea\x41l\n-datalabeling.googleapis.com/AnnotationSpecSet\x12;projects/{project}/annotationSpecSets/{annotation_spec_set}";\n\x0e\x41nnotationSpec\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\tBx\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabelingb\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
    ],
)


_ANNOTATIONSPECSET = _descriptor.Descriptor(
    name="AnnotationSpecSet",
    full_name="google.cloud.datalabeling.v1beta1.AnnotationSpecSet",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpecSet.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpecSet.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpecSet.description",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="annotation_specs",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpecSet.annotation_specs",
            index=3,
            number=4,
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
            name="blocking_resources",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpecSet.blocking_resources",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\352Al\n-datalabeling.googleapis.com/AnnotationSpecSet\022;projects/{project}/annotationSpecSets/{annotation_spec_set}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=162,
    serialized_end=456,
)


_ANNOTATIONSPEC = _descriptor.Descriptor(
    name="AnnotationSpec",
    full_name="google.cloud.datalabeling.v1beta1.AnnotationSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpec.display_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.datalabeling.v1beta1.AnnotationSpec.description",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
    serialized_start=458,
    serialized_end=517,
)

_ANNOTATIONSPECSET.fields_by_name["annotation_specs"].message_type = _ANNOTATIONSPEC
DESCRIPTOR.message_types_by_name["AnnotationSpecSet"] = _ANNOTATIONSPECSET
DESCRIPTOR.message_types_by_name["AnnotationSpec"] = _ANNOTATIONSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnnotationSpecSet = _reflection.GeneratedProtocolMessageType(
    "AnnotationSpecSet",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANNOTATIONSPECSET,
        "__module__": "google.cloud.datalabeling_v1beta1.proto.annotation_spec_set_pb2",
        "__doc__": """An AnnotationSpecSet is a collection of label definitions.
  For example, in image classification tasks, you define a set of possible
  labels for images as an AnnotationSpecSet. An AnnotationSpecSet is
  immutable upon creation.
  
  
  Attributes:
      name:
          Output only. The AnnotationSpecSet resource name in the
          following format:  “projects/{project_id}/annotationSpecSets/{
          annotation_spec_set_id}”
      display_name:
          Required. The display name for AnnotationSpecSet that you
          define when you create it. Maximum of 64 characters.
      description:
          Optional. User-provided description of the annotation
          specification set. The description can be up to 10,000
          characters long.
      annotation_specs:
          Required. The array of AnnotationSpecs that you define when
          you create the AnnotationSpecSet. These are the possible
          labels for the labeling task.
      blocking_resources:
          Output only. The names of any related resources that are
          blocking changes to the annotation spec set.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.AnnotationSpecSet)
    },
)
_sym_db.RegisterMessage(AnnotationSpecSet)

AnnotationSpec = _reflection.GeneratedProtocolMessageType(
    "AnnotationSpec",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANNOTATIONSPEC,
        "__module__": "google.cloud.datalabeling_v1beta1.proto.annotation_spec_set_pb2",
        "__doc__": """Container of information related to one possible annotation that can be
  used in a labeling task. For example, an image classification task where
  images are labeled as ``dog`` or ``cat`` must reference an
  AnnotationSpec for ``dog`` and an AnnotationSpec for ``cat``.
  
  
  Attributes:
      display_name:
          Required. The display name of the AnnotationSpec. Maximum of
          64 characters.
      description:
          Optional. User-provided description of the annotation
          specification. The description can be up to 10,000 characters
          long.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.AnnotationSpec)
    },
)
_sym_db.RegisterMessage(AnnotationSpec)


DESCRIPTOR._options = None
_ANNOTATIONSPECSET._options = None
# @@protoc_insertion_point(module_scope)
