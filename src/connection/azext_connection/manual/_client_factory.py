# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.cli.core._profile import Profile


def cf_connection_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_connection.vendored_sdks.connection import MicrosoftServiceLinker

    # Hack: set custom header for testing, and the header will be removed when release
    profile = Profile(cli_ctx=cli_ctx)
    creds, _, _ = profile.get_raw_token()

    client = get_mgmt_service_client(cli_ctx, MicrosoftServiceLinker)
    client._client._config.headers_policy._headers['x-ms-cupertino-test-token'] = creds[1]
    return client


def cf_linker(cli_ctx, *_):
    return cf_connection_cl(cli_ctx).linker