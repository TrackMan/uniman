import uniman.model.firewall_rule
import uniman.model.sys_info
from uniman.client import UniFiClient
from uniman.endpoints import Endpoints
from uniman.generic_client import GenericUniFiClient

if __name__ == '__main__':
    host = 'example.com'
    port = 443
    username = 'joe'
    password = 'Secure1'
    site = 'default'

    # Use a generic client

    generic_client = GenericUniFiClient(host, port, site)
    login = generic_client.login(username, password)

    sys_info = generic_client.query(Endpoints.SYS_INFO.value, uniman.model.sys_info.SysInfo)
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

    created = generic_client.create(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule, new_rule)
    rule_id = created.data[0]._id

    rules = generic_client.query(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule)
    rule = next(r for r in rules.data if rule_id == r._id)
    rule.name = 'Hello World'

    updated = generic_client.update(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule, rule)
    assert rule.name == updated.data[0].name

    deleted = generic_client.delete(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule, rule_id)
    assert 'ok' == deleted.meta.rc

    # Use a type-safe client

    client = UniFiClient(generic_client)
    client.login(username, password)

    sys_info = client.query_sys_infos()
    print(sys_info.data[0].name)

    firewall_rule = uniman.model.firewall_rule.DataItem(new_rule)

    created = client.create_firewall_rule(firewall_rule)
    rule_id = created.data[0]._id

    rules = client.query_firewall_rules()
    rule = next(r for r in rules.data if rule_id == r._id)
    rule.name = 'Hello World'

    updated = client.update_firewall_rule(rule)
    assert rule.name == updated.data[0].name

    deleted = client.delete_firewall_rule(rule_id)
    assert 'ok' == deleted.meta.rc
