import attr
import base64
import typing
import karrio.lib as lib
import karrio.core as core


class Settings(core.Settings):
    """TGE connection settings."""

    api_key: str
    username: str
    password: str
    auth_username: str
    auth_password: str
    my_toll_token: str
    my_toll_identity: str
    account_code: str = None
    channel: str = None
    call_id: str = None

    @property
    def carrier_name(self):
        return "tge"

    @property
    def server_url(self):
        return self.connection_config.server_url.state or "https://tge.3plapi.com"

    @property
    def auth(self):
        pair = "%s:%s" % (self.auth_username, self.auth_password)
        return base64.b64encode(pair.encode("utf-8")).decode("ascii")

    @property
    def authorization(self):
        pair = "%s:%s" % (self.username, self.password)
        return base64.b64encode(pair.encode("utf-8")).decode("ascii")

    @property
    def connection_config(self) -> lib.units.Options:
        from karrio.providers.tge.units import ConnectionConfig

        return lib.to_connection_config(
            self.config or {},
            option_type=ConnectionConfig,
        )


def parse_response(response: str) -> dict:
    _response = lib.failsafe(lambda: lib.to_dict(response))

    if _response is None:
        _error = response[: response.find(": {")].strip()
        return dict(
            message=_error if any(_error) else response,
            is_error=True,
        )

    return _response
