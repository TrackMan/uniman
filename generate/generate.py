import json
import os

import json_ref_dict
import statham
import statham.schema.parser
import statham.titles
from genson import SchemaBuilder
from json_ref_dict import RefDict
from requests import Session
from statham.serializers import serialize_python

from client.endpoints import Endpoints


def generate():
    host = os.environ['UNIFI_HOST']
    port = int(os.environ['UNIFI_PORT'])
    username = os.environ['UNIFI_USER']
    password = os.environ['UNIFI_PASS']
    site = os.environ['UNIFI_SITE']

    payloads = {
        Endpoints.LOGIN.name: {'username': username, 'password': password}
    }

    session = Session()

    for endpoint in Endpoints:
        request = endpoint.value.to_request(host, port, site, payload=payloads.get(endpoint.name, {}))
        response = session.send(session.prepare_request(request), verify=False)

        builder = SchemaBuilder()
        builder.add_object(response.json())
        builder.add_schema({'required': []})
        builder.add_schema({'properties': {'data': {'items': {'required': []}}}})
        schema = json.loads(builder.to_json())

        schema_path = 'schema' + os.path.sep + endpoint.name.lower() + '.schema.json'
        schema_file = open(schema_path, 'w')
        schema_file.write(json.dumps(schema, indent=4))
        schema_file.close()

        json_schema = json_ref_dict.materialize(
            RefDict.from_uri(schema_path), context_labeller=statham.titles.title_labeller()
        )

        parsed_schema = statham.schema.parser.parse(json_schema)
        python_class = serialize_python(*parsed_schema)

        python_class_file = open('model' + os.path.sep + endpoint.name.lower() + '.py', 'w')
        python_class_file.write(python_class)
        python_class_file.close()


if __name__ == '__main__':
    generate()
