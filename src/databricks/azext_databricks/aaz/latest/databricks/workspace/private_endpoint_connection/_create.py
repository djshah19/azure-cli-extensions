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
    "databricks workspace private-endpoint-connection create",
)
class Create(AAZCommand):
    """Create the status of a private endpoint connection with the specified name
    """

    _aaz_info = {
        "version": "2023-02-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databricks/workspaces/{}/privateendpointconnections/{}", "2023-02-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the private endpoint connection",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=3,
            ),
        )

        # define Arg Group "Private Link Service Connection State"

        _args_schema = cls._args_schema
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Private Link Service Connection State",
            help="The description for the current state of a private endpoint connection",
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Private Link Service Connection State",
            help="The status of a private endpoint connection",
            required=True,
            enum={"Approved": "Approved", "Disconnected": "Disconnected", "Pending": "Pending", "Rejected": "Rejected"},
        )

        # define Arg Group "PrivateLinkServiceConnectionState"

        _args_schema = cls._args_schema
        _args_schema.actions_required = AAZStrArg(
            options=["--actions-required"],
            arg_group="PrivateLinkServiceConnectionState",
            help="Actions required for a private endpoint connection",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.group_ids = AAZListArg(
            options=["--group-ids"],
            arg_group="Properties",
            help="GroupIds from the private link service resource.",
        )

        group_ids = cls._args_schema.group_ids
        group_ids.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.PrivateEndpointConnectionsCreate(ctx=self.ctx)()
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

    class PrivateEndpointConnectionsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateEndpointConnectionName", self.ctx.args.name,
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
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-02-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("groupIds", AAZListType, ".group_ids")
                properties.set_prop("privateLinkServiceConnectionState", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            group_ids = _builder.get(".properties.groupIds")
            if group_ids is not None:
                group_ids.set_elements(AAZStrType, ".")

            private_link_service_connection_state = _builder.get(".properties.privateLinkServiceConnectionState")
            if private_link_service_connection_state is not None:
                private_link_service_connection_state.set_prop("actionsRequired", AAZStrType, ".actions_required")
                private_link_service_connection_state.set_prop("description", AAZStrType, ".description")
                private_link_service_connection_state.set_prop("status", AAZStrType, ".status", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

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
            _CreateHelper._build_schema_private_endpoint_connection_read(cls._schema_on_200)

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""

    _schema_private_endpoint_connection_read = None

    @classmethod
    def _build_schema_private_endpoint_connection_read(cls, _schema):
        if cls._schema_private_endpoint_connection_read is not None:
            _schema.id = cls._schema_private_endpoint_connection_read.id
            _schema.name = cls._schema_private_endpoint_connection_read.name
            _schema.properties = cls._schema_private_endpoint_connection_read.properties
            _schema.type = cls._schema_private_endpoint_connection_read.type
            return

        cls._schema_private_endpoint_connection_read = _schema_private_endpoint_connection_read = AAZObjectType()

        private_endpoint_connection_read = _schema_private_endpoint_connection_read
        private_endpoint_connection_read.id = AAZStrType(
            flags={"read_only": True},
        )
        private_endpoint_connection_read.name = AAZStrType(
            flags={"read_only": True},
        )
        private_endpoint_connection_read.properties = AAZObjectType(
            flags={"required": True},
        )
        private_endpoint_connection_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_private_endpoint_connection_read.properties
        properties.group_ids = AAZListType(
            serialized_name="groupIds",
        )
        properties.private_endpoint = AAZObjectType(
            serialized_name="privateEndpoint",
        )
        properties.private_link_service_connection_state = AAZObjectType(
            serialized_name="privateLinkServiceConnectionState",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        group_ids = _schema_private_endpoint_connection_read.properties.group_ids
        group_ids.Element = AAZStrType()

        private_endpoint = _schema_private_endpoint_connection_read.properties.private_endpoint
        private_endpoint.id = AAZStrType(
            flags={"read_only": True},
        )

        private_link_service_connection_state = _schema_private_endpoint_connection_read.properties.private_link_service_connection_state
        private_link_service_connection_state.actions_required = AAZStrType(
            serialized_name="actionsRequired",
        )
        private_link_service_connection_state.description = AAZStrType()
        private_link_service_connection_state.status = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_private_endpoint_connection_read.id
        _schema.name = cls._schema_private_endpoint_connection_read.name
        _schema.properties = cls._schema_private_endpoint_connection_read.properties
        _schema.type = cls._schema_private_endpoint_connection_read.type


__all__ = ["Create"]