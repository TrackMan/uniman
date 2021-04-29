import model.firewall_rule
import model.sys_info
from client.endpoints import Endpoints
from client.generic_client import GenericUniFiClient

if __name__ == '__main__':
    host = 'example.com'
    port = 443
    username = 'joe'
    password = 'Secure1'
    site = 'default'

    client = GenericUniFiClient(host, port, site)
    login = client.login(username, password)
    sys_info = client.query(Endpoints.SYS_INFO.value, model.sys_info.SysInfo)
    print(sys_info.data[0].name)

    new_rule = {
        'ruleset': 'WAN_LOCAL',
        'rule_index': 2002,
        'name': 'Example Firewall Rule',
        'enabled': False,
        'action': 'accept',
        'protocol_match_excepted': False,
        'logging': False,
        'state_new': False,
        'state_established': False,
        'state_invalid': False,
        'state_related': False,
        'ipsec': '',
        'src_firewallgroup_ids': [],
        'src_mac_address': '',
        'dst_firewallgroup_ids': [],
        'dst_address': '',
        'src_address': '',
        'protocol': 'tcp_udp',
        'icmp_typename': '',
        'src_networkconf_id': '',
        'src_networkconf_type': 'NETv4',
        'dst_networkconf_id': '',
        'dst_networkconf_type': 'NETv4'
    }

    # Or use JSON directly
    firewall_rule = model.firewall_rule.DataItem(new_rule)

    created = client.create(Endpoints.FIREWALL_RULE.value, model.firewall_rule.FirewallRule, firewall_rule)
    rule_id = created.data[0]._id

    rules = client.query(Endpoints.FIREWALL_RULE.value, model.firewall_rule.FirewallRule)
    rule = next(r for r in rules.data if rule_id == r._id)
    rule.name = 'Hello World'

    updated = client.update(Endpoints.FIREWALL_RULE.value, model.firewall_rule.FirewallRule, rule)
    assert rule.name == updated.data[0].name

    deleted = client.delete(Endpoints.FIREWALL_RULE.value, model.firewall_rule.FirewallRule, rule_id)
    assert 'ok' == deleted.meta.rc
