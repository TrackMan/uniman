from typing import TypeVar

import uniman.model.login
import uniman.model.device
import uniman.model.dhcp_option
import uniman.model.firewall_group
import uniman.model.firewall_rule
import uniman.model.network_conf
import uniman.model.routing
import uniman.model.sys_info
import uniman.model.user_group
import uniman.model.wlan_conf
from uniman.endpoints import Endpoints
from uniman.generic_client import GenericUniFiClient


class UniFiClient:
    T = TypeVar('T')
    client: GenericUniFiClient

    def __init__(self, client: GenericUniFiClient):
        self.client = client

    def login(self, username: str, password: str, T=uniman.model.login.Login) -> T:
        return self.client.login(username, password, T)

    def query_logins(self, T=uniman.model.login.Login) -> T:
        return self.client.query(Endpoints.LOGIN, T)

    def delete_login(self, uid: str, T=uniman.model.login.Login) -> T:
        return self.client.delete(Endpoints.LOGIN, uid, T)

    def update_login(self, data, T=uniman.model.login.Login) -> T:
        return self.client.update(Endpoints.LOGIN, data, T)

    def create_login(self, data, T=uniman.model.login.Login) -> T:
        return self.client.create(Endpoints.LOGIN, data, T)

    def query_devices(self, T=uniman.model.device.Device) -> T:
        return self.client.query(Endpoints.DEVICE, T)

    def delete_device(self, uid: str, T=uniman.model.device.Device) -> T:
        return self.client.delete(Endpoints.DEVICE, uid, T)

    def update_device(self, data, T=uniman.model.device.Device) -> T:
        return self.client.update(Endpoints.DEVICE, data, T)

    def create_device(self, data, T=uniman.model.device.Device) -> T:
        return self.client.create(Endpoints.DEVICE, data, T)

    def query_dhcp_options(self, T=uniman.model.dhcp_option.DhcpOption) -> T:
        return self.client.query(Endpoints.DHCP_OPTION, T)

    def delete_dhcp_option(self, uid: str, T=uniman.model.dhcp_option.DhcpOption) -> T:
        return self.client.delete(Endpoints.DHCP_OPTION, uid, T)

    def update_dhcp_option(self, data, T=uniman.model.dhcp_option.DhcpOption) -> T:
        return self.client.update(Endpoints.DHCP_OPTION, data, T)

    def create_dhcp_option(self, data, T=uniman.model.dhcp_option.DhcpOption) -> T:
        return self.client.create(Endpoints.DHCP_OPTION, data, T)

    def query_firewall_groups(self, T=uniman.model.firewall_group.FirewallGroup) -> T:
        return self.client.query(Endpoints.FIREWALL_GROUP, T)

    def delete_firewall_group(self, uid: str, T=uniman.model.firewall_group.FirewallGroup) -> T:
        return self.client.delete(Endpoints.FIREWALL_GROUP, uid, T)

    def update_firewall_group(self, data, T=uniman.model.firewall_group.FirewallGroup) -> T:
        return self.client.update(Endpoints.FIREWALL_GROUP, data, T)

    def create_firewall_group(self, data, T=uniman.model.firewall_group.FirewallGroup) -> T:
        return self.client.create(Endpoints.FIREWALL_GROUP, data, T)

    def query_firewall_rules(self, T=uniman.model.firewall_rule.FirewallRule) -> T:
        return self.client.query(Endpoints.FIREWALL_RULE, T)

    def delete_firewall_rule(self, uid: str, T=uniman.model.firewall_rule.FirewallRule) -> T:
        return self.client.delete(Endpoints.FIREWALL_RULE, uid, T)

    def update_firewall_rule(self, data, T=uniman.model.firewall_rule.FirewallRule) -> T:
        return self.client.update(Endpoints.FIREWALL_RULE, data, T)

    def create_firewall_rule(self, data, T=uniman.model.firewall_rule.FirewallRule) -> T:
        return self.client.create(Endpoints.FIREWALL_RULE, data, T)

    def query_network_confs(self, T=uniman.model.network_conf.NetworkConf) -> T:
        return self.client.query(Endpoints.NETWORK_CONF, T)

    def delete_network_conf(self, uid: str, T=uniman.model.network_conf.NetworkConf) -> T:
        return self.client.delete(Endpoints.NETWORK_CONF, uid, T)

    def update_network_conf(self, data, T=uniman.model.network_conf.NetworkConf) -> T:
        return self.client.update(Endpoints.NETWORK_CONF, data, T)

    def create_network_conf(self, data, T=uniman.model.network_conf.NetworkConf) -> T:
        return self.client.create(Endpoints.NETWORK_CONF, data, T)

    def query_routings(self, T=uniman.model.routing.Routing) -> T:
        return self.client.query(Endpoints.ROUTING, T)

    def delete_routing(self, uid: str, T=uniman.model.routing.Routing) -> T:
        return self.client.delete(Endpoints.ROUTING, uid, T)

    def update_routing(self, data, T=uniman.model.routing.Routing) -> T:
        return self.client.update(Endpoints.ROUTING, data, T)

    def create_routing(self, data, T=uniman.model.routing.Routing) -> T:
        return self.client.create(Endpoints.ROUTING, data, T)

    def query_sys_infos(self, T=uniman.model.sys_info.SysInfo) -> T:
        return self.client.query(Endpoints.SYS_INFO, T)

    def delete_sys_info(self, uid: str, T=uniman.model.sys_info.SysInfo) -> T:
        return self.client.delete(Endpoints.SYS_INFO, uid, T)

    def update_sys_info(self, data, T=uniman.model.sys_info.SysInfo) -> T:
        return self.client.update(Endpoints.SYS_INFO, data, T)

    def create_sys_info(self, data, T=uniman.model.sys_info.SysInfo) -> T:
        return self.client.create(Endpoints.SYS_INFO, data, T)

    def query_user_groups(self, T=uniman.model.user_group.UserGroup) -> T:
        return self.client.query(Endpoints.USER_GROUP, T)

    def delete_user_group(self, uid: str, T=uniman.model.user_group.UserGroup) -> T:
        return self.client.delete(Endpoints.USER_GROUP, uid, T)

    def update_user_group(self, data, T=uniman.model.user_group.UserGroup) -> T:
        return self.client.update(Endpoints.USER_GROUP, data, T)

    def create_user_group(self, data, T=uniman.model.user_group.UserGroup) -> T:
        return self.client.create(Endpoints.USER_GROUP, data, T)

    def query_wlan_confs(self, T=uniman.model.wlan_conf.WlanConf) -> T:
        return self.client.query(Endpoints.WLAN_CONF, T)

    def delete_wlan_conf(self, uid: str, T=uniman.model.wlan_conf.WlanConf) -> T:
        return self.client.delete(Endpoints.WLAN_CONF, uid, T)

    def update_wlan_conf(self, data, T=uniman.model.wlan_conf.WlanConf) -> T:
        return self.client.update(Endpoints.WLAN_CONF, data, T)

    def create_wlan_conf(self, data, T=uniman.model.wlan_conf.WlanConf) -> T:
        return self.client.create(Endpoints.WLAN_CONF, data, T)
