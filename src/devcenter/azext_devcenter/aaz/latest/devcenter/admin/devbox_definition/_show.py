# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "devcenter admin devbox-definition show",
)
class Show(AAZCommand):
    """Get a dev box definition

    :example: Get dev center dev box definition
        az devcenter admin devbox-definition show --name "WebDevBox" --dev-center-name "Contoso" --resource-group "rg1"

    :example: Get project dev box definition
        az devcenter admin devbox-definition show --name "WebDevBox" --project-name "ContosoProject" --resource-group "rg1"
    """

    _aaz_info = {
        "version": "2023-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devcenter/devcenters/{}/devboxdefinitions/{}", "2023-04-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devcenter/projects/{}/devboxdefinitions/{}", "2023-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.dev_box_definition_name = AAZStrArg(
            options=["-n", "--name", "--dev-box-definition-name"],
            help="The name of the Dev Box definition.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.dev_center_name = AAZStrArg(
            options=["-d", "--dev-center", "--dev-center-name"],
            help="The name of the dev center. Use `az configure -d dev-center=<dev_center_name>` to configure a default.",
            id_part="name",
        )
        _args_schema.project_name = AAZStrArg(
            options=["--project", "--project-name"],
            help="The name of the project. Use `az configure -d project=<project_name>` to configure a default.",
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.dev_box_definition_name) and has_value(self.ctx.args.project_name) and has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.args.dev_box_definition_name) and has_value(self.ctx.args.dev_center_name) and has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        if condition_1:
            self.DevBoxDefinitionsGet(ctx=self.ctx)()
        elif condition_0:
            self.DevBoxDefinitionsGetByProject(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DevBoxDefinitionsGetByProject(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/devboxdefinitions/{devBoxDefinitionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "devBoxDefinitionName", self.ctx.args.dev_box_definition_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "projectName", self.ctx.args.project_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.active_image_reference = AAZObjectType(
                serialized_name="activeImageReference",
            )
            _ShowHelper._build_schema_image_reference_read(properties.active_image_reference)
            properties.hibernate_support = AAZStrType(
                serialized_name="hibernateSupport",
            )
            properties.image_reference = AAZObjectType(
                serialized_name="imageReference",
                flags={"required": True},
            )
            _ShowHelper._build_schema_image_reference_read(properties.image_reference)
            properties.image_validation_error_details = AAZObjectType(
                serialized_name="imageValidationErrorDetails",
            )
            properties.image_validation_status = AAZStrType(
                serialized_name="imageValidationStatus",
            )
            properties.os_storage_type = AAZStrType(
                serialized_name="osStorageType",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sku = AAZObjectType(
                flags={"required": True},
            )

            image_validation_error_details = cls._schema_on_200.properties.image_validation_error_details
            image_validation_error_details.code = AAZStrType()
            image_validation_error_details.message = AAZStrType()

            sku = cls._schema_on_200.properties.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class DevBoxDefinitionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}/devboxdefinitions/{devBoxDefinitionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "devBoxDefinitionName", self.ctx.args.dev_box_definition_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "devCenterName", self.ctx.args.dev_center_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.active_image_reference = AAZObjectType(
                serialized_name="activeImageReference",
            )
            _ShowHelper._build_schema_image_reference_read(properties.active_image_reference)
            properties.hibernate_support = AAZStrType(
                serialized_name="hibernateSupport",
            )
            properties.image_reference = AAZObjectType(
                serialized_name="imageReference",
                flags={"required": True},
            )
            _ShowHelper._build_schema_image_reference_read(properties.image_reference)
            properties.image_validation_error_details = AAZObjectType(
                serialized_name="imageValidationErrorDetails",
            )
            properties.image_validation_status = AAZStrType(
                serialized_name="imageValidationStatus",
            )
            properties.os_storage_type = AAZStrType(
                serialized_name="osStorageType",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sku = AAZObjectType(
                flags={"required": True},
            )

            image_validation_error_details = cls._schema_on_200.properties.image_validation_error_details
            image_validation_error_details.code = AAZStrType()
            image_validation_error_details.message = AAZStrType()

            sku = cls._schema_on_200.properties.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_image_reference_read = None

    @classmethod
    def _build_schema_image_reference_read(cls, _schema):
        if cls._schema_image_reference_read is not None:
            _schema.exact_version = cls._schema_image_reference_read.exact_version
            _schema.id = cls._schema_image_reference_read.id
            return

        cls._schema_image_reference_read = _schema_image_reference_read = AAZObjectType()

        image_reference_read = _schema_image_reference_read
        image_reference_read.exact_version = AAZStrType(
            serialized_name="exactVersion",
            flags={"read_only": True},
        )
        image_reference_read.id = AAZStrType()

        _schema.exact_version = cls._schema_image_reference_read.exact_version
        _schema.id = cls._schema_image_reference_read.id


__all__ = ["Show"]