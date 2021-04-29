from enum import Enum

from requests import Request

template_site = "https://{host}:{port}/proxy/network/api/s/{site}/{endpoint}{path}"
template_auth = "https://{host}:{port}/api/{endpoint}"


class Endpoint:
    endpoint: str
    method: str
    template: str

    def __init__(self, endpoint, method, template=template_site):
        self.endpoint = endpoint
        self.method = method
        self.template = template

    def to_request(self, host, port, site, path=None, payload=None, method=None):
        if payload is None:
            payload = {}

        if path is None:
            actual_path = ''
        else:
            actual_path = '/' + path

        return Request(
            url=self.template.format(
                host=host,
                port=port,
                site=site,
                endpoint=self.endpoint,
                path=actual_path),
            method=method or self.method,
            json=payload
        )


class Endpoints(Enum):
    LOGIN = Endpoint('auth/login', 'POST', template_auth)
    # Keep LOGIN as the first item
    DEVICE = Endpoint('stat/device', 'GET')
    DHCP_OPTION = Endpoint('rest/dhcpoption', 'GET')
    FIREWALL_GROUP = Endpoint('rest/firewallgroup', 'GET')
    FIREWALL_RULE = Endpoint('rest/firewallrule', 'GET')
    NETWORK_CONF = Endpoint('rest/networkconf', 'GET')
    ROUTING = Endpoint('rest/routing', 'GET')
    SELF = Endpoint('self', 'GET')
    SYS_INFO = Endpoint('stat/sysinfo', 'GET')
    USER_GROUP = Endpoint('rest/usergroup', 'GET')
    WLAN_CONF = Endpoint('rest/wlanconf', 'GET')
