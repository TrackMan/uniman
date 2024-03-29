from typing import TypeVar

from requests import Session, Request, Response
from statham.schema.constants import NotPassed

from uniman.endpoints import Endpoints


class GenericUniFiClient:
    T = TypeVar('T')

    session: Session
    host: str
    port: int
    site: str

    def __init__(self, host: str, port: int, site: str):
        self.host = host
        self.port = port
        self.site = site
        self.csrf_token = None

    def login(self, username: str, password: str, T=dict) -> T:
        self.session = Session()

        request = Endpoints.LOGIN.value.to_request(
            self.host, self.port, self.site,
            payload={'username': username, 'password': password}
        )

        response = self._send(request)
        self.csrf_token = response.headers.get('X-CSRF-Token')

        return T(response.json())

    def query(self, endpoint: Endpoints, T=dict) -> T:
        self._csrf()

        request = endpoint.value.to_request(
            self.host, self.port, self.site
        )

        return T(self._send(request).json())

    def delete(self, endpoint: Endpoints, id: str, T=dict) -> T:
        self._csrf()

        request = endpoint.value.to_request(
            self.host, self.port, self.site, method='DELETE', path=id
        )

        return T(self._send(request).json())

    def update(self, endpoint: Endpoints, data, T=dict) -> T:
        self._csrf()

        request = endpoint.value.to_request(
            self.host, self.port, self.site, method='PUT', path=data['_id'] or data._id,
            payload=self.__payload(self, data)
        )

        return T(self._send(request).json())

    def create(self, endpoint: Endpoints, data, T=dict) -> T:
        self._csrf()

        request = endpoint.value.to_request(
            self.host, self.port, self.site, method='POST',
            payload=self.__payload(self, data)
        )

        return T(self._send(request).json())

    def _csrf(self):
        self.session.headers.update({'x-csrf-token': self.csrf_token})

    def _send(self, request: Request) -> Response:
        return self.session.send(self.session.prepare_request(request), verify=False)

    # There must be a better way to do this

    @staticmethod
    def __payload(self, data) -> dict:
        dictionary = data if isinstance(data, dict) else data.__dict__
        return dict(filter(self.__filter_criteria, dictionary.items()))

    @staticmethod
    def __filter_criteria(item) -> bool:
        return not isinstance(item[1], NotPassed) and item[0] not in ('_dict', '__len__')
