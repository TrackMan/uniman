from typing import TypeVar

{% macro endpoint_package(endpoint) -%}
uniman.model.{{ endpoint.name.lower() }}
{%- endmacro -%}

{%- macro endpoint_class(endpoint) -%}
{{ endpoint_package(endpoint) }}.{{ endpoint.name.title().replace('_', '') }}
{%- endmacro -%}

{%- for endpoint in endpoints -%}
import {{ endpoint_package(endpoint) }}
{% endfor -%}
from uniman.endpoints import Endpoints
from uniman.generic_client import GenericUniFiClient


class UniFiClient:
    T = TypeVar('T')
    client: GenericUniFiClient

    def __init__(self, client: GenericUniFiClient):
        self.client = client

    def login(self, username: str, password: str, T=uniman.model.login.Login) -> T:
        return self.client.login(username, password, T)
{% for endpoint in endpoints %}
    def query_{{ endpoint.name.lower() }}s(self, T={{ endpoint_class(endpoint) }}) -> T:
        return self.client.query(Endpoints.{{ endpoint.name }}, T)

    def delete_{{ endpoint.name.lower() }}(self, uid: str, T={{ endpoint_class(endpoint) }}) -> T:
        return self.client.delete(Endpoints.{{ endpoint.name }}, uid, T)

    def update_{{ endpoint.name.lower() }}(self, data, T={{ endpoint_class(endpoint) }}) -> T:
        return self.client.update(Endpoints.{{ endpoint.name }}, data, T)

    def create_{{ endpoint.name.lower() }}(self, data, T={{ endpoint_class(endpoint) }}) -> T:
        return self.client.create(Endpoints.{{ endpoint.name }}, data, T)
{% endfor %}
