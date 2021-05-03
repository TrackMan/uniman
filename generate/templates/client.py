{%- macro endpoint_package(endpoint) -%}
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
    client: GenericUniFiClient

    def __init__(self, client: GenericUniFiClient):
        self.client = client

    def login(self, username: str, password: str) -> uniman.model.login.Login:
        return self.client.login(username, password)
{% for endpoint in endpoints %}
    def query_{{ endpoint.name.lower() }}s(self) -> {{ endpoint_class(endpoint) }}:
        return self.client.query(Endpoints.{{ endpoint.name }}.value, {{ endpoint_class(endpoint) }})

    def delete_{{ endpoint.name.lower() }}(self, uid: str) -> {{ endpoint_class(endpoint) }}:
        return self.client.delete(Endpoints.{{ endpoint.name }}.value, {{ endpoint_class(endpoint) }}, uid)

    def update_{{ endpoint.name.lower() }}(self, data) -> {{ endpoint_class(endpoint) }}:
        return self.client.update(Endpoints.{{ endpoint.name }}.value, {{ endpoint_class(endpoint) }}, data)

    def create_{{ endpoint.name.lower() }}(self, data) -> {{ endpoint_class(endpoint) }}:
        return self.client.create(Endpoints.{{ endpoint.name }}.value, {{ endpoint_class(endpoint) }}, data)
{% endfor %}
