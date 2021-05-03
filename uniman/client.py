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
    client: GenericUniFiClient

    def __init__(self, client: GenericUniFiClient):
        self.client = client

    def login(self, username: str, password: str) -> uniman.model.login.Login:
        return self.client.login(username, password)

    def query_logins(self) -> uniman.model.login.Login:
        return self.client.query(Endpoints.LOGIN.value, uniman.model.login.Login)

    def delete_login(self, uid: str) -> uniman.model.login.Login:
        return self.client.delete(Endpoints.LOGIN.value, uniman.model.login.Login, uid)

    def update_login(self, data) -> uniman.model.login.Login:
        return self.client.update(Endpoints.LOGIN.value, uniman.model.login.Login, data)

    def create_login(self, data) -> uniman.model.login.Login:
        return self.client.create(Endpoints.LOGIN.value, uniman.model.login.Login, data)

    def query_devices(self) -> uniman.model.device.Device:
        return self.client.query(Endpoints.DEVICE.value, uniman.model.device.Device)

    def delete_device(self, uid: str) -> uniman.model.device.Device:
        return self.client.delete(Endpoints.DEVICE.value, uniman.model.device.Device, uid)

    def update_device(self, data) -> uniman.model.device.Device:
        return self.client.update(Endpoints.DEVICE.value, uniman.model.device.Device, data)

    def create_device(self, data) -> uniman.model.device.Device:
        return self.client.create(Endpoints.DEVICE.value, uniman.model.device.Device, data)

    def query_dhcp_options(self) -> uniman.model.dhcp_option.DhcpOption:
        return self.client.query(Endpoints.DHCP_OPTION.value, uniman.model.dhcp_option.DhcpOption)

    def delete_dhcp_option(self, uid: str) -> uniman.model.dhcp_option.DhcpOption:
        return self.client.delete(Endpoints.DHCP_OPTION.value, uniman.model.dhcp_option.DhcpOption, uid)

    def update_dhcp_option(self, data) -> uniman.model.dhcp_option.DhcpOption:
        return self.client.update(Endpoints.DHCP_OPTION.value, uniman.model.dhcp_option.DhcpOption, data)

    def create_dhcp_option(self, data) -> uniman.model.dhcp_option.DhcpOption:
        return self.client.create(Endpoints.DHCP_OPTION.value, uniman.model.dhcp_option.DhcpOption, data)

    def query_firewall_groups(self) -> uniman.model.firewall_group.FirewallGroup:
        return self.client.query(Endpoints.FIREWALL_GROUP.value, uniman.model.firewall_group.FirewallGroup)

    def delete_firewall_group(self, uid: str) -> uniman.model.firewall_group.FirewallGroup:
        return self.client.delete(Endpoints.FIREWALL_GROUP.value, uniman.model.firewall_group.FirewallGroup, uid)

    def update_firewall_group(self, data) -> uniman.model.firewall_group.FirewallGroup:
        return self.client.update(Endpoints.FIREWALL_GROUP.value, uniman.model.firewall_group.FirewallGroup, data)

    def create_firewall_group(self, data) -> uniman.model.firewall_group.FirewallGroup:
        return self.client.create(Endpoints.FIREWALL_GROUP.value, uniman.model.firewall_group.FirewallGroup, data)

    def query_firewall_rules(self) -> uniman.model.firewall_rule.FirewallRule:
        return self.client.query(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule)

    def delete_firewall_rule(self, uid: str) -> uniman.model.firewall_rule.FirewallRule:
        return self.client.delete(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule, uid)

    def update_firewall_rule(self, data) -> uniman.model.firewall_rule.FirewallRule:
        return self.client.update(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule, data)

    def create_firewall_rule(self, data) -> uniman.model.firewall_rule.FirewallRule:
        return self.client.create(Endpoints.FIREWALL_RULE.value, uniman.model.firewall_rule.FirewallRule, data)

    def query_network_confs(self) -> uniman.model.network_conf.NetworkConf:
        return self.client.query(Endpoints.NETWORK_CONF.value, uniman.model.network_conf.NetworkConf)

    def delete_network_conf(self, uid: str) -> uniman.model.network_conf.NetworkConf:
        return self.client.delete(Endpoints.NETWORK_CONF.value, uniman.model.network_conf.NetworkConf, uid)

    def update_network_conf(self, data) -> uniman.model.network_conf.NetworkConf:
        return self.client.update(Endpoints.NETWORK_CONF.value, uniman.model.network_conf.NetworkConf, data)

    def create_network_conf(self, data) -> uniman.model.network_conf.NetworkConf:
        return self.client.create(Endpoints.NETWORK_CONF.value, uniman.model.network_conf.NetworkConf, data)

    def query_routings(self) -> uniman.model.routing.Routing:
        return self.client.query(Endpoints.ROUTING.value, uniman.model.routing.Routing)

    def delete_routing(self, uid: str) -> uniman.model.routing.Routing:
        return self.client.delete(Endpoints.ROUTING.value, uniman.model.routing.Routing, uid)

    def update_routing(self, data) -> uniman.model.routing.Routing:
        return self.client.update(Endpoints.ROUTING.value, uniman.model.routing.Routing, data)

    def create_routing(self, data) -> uniman.model.routing.Routing:
        return self.client.create(Endpoints.ROUTING.value, uniman.model.routing.Routing, data)

    def query_sys_infos(self) -> uniman.model.sys_info.SysInfo:
        return self.client.query(Endpoints.SYS_INFO.value, uniman.model.sys_info.SysInfo)

    def delete_sys_info(self, uid: str) -> uniman.model.sys_info.SysInfo:
        return self.client.delete(Endpoints.SYS_INFO.value, uniman.model.sys_info.SysInfo, uid)

    def update_sys_info(self, data) -> uniman.model.sys_info.SysInfo:
        return self.client.update(Endpoints.SYS_INFO.value, uniman.model.sys_info.SysInfo, data)

    def create_sys_info(self, data) -> uniman.model.sys_info.SysInfo:
        return self.client.create(Endpoints.SYS_INFO.value, uniman.model.sys_info.SysInfo, data)

    def query_user_groups(self) -> uniman.model.user_group.UserGroup:
        return self.client.query(Endpoints.USER_GROUP.value, uniman.model.user_group.UserGroup)

    def delete_user_group(self, uid: str) -> uniman.model.user_group.UserGroup:
        return self.client.delete(Endpoints.USER_GROUP.value, uniman.model.user_group.UserGroup, uid)

    def update_user_group(self, data) -> uniman.model.user_group.UserGroup:
        return self.client.update(Endpoints.USER_GROUP.value, uniman.model.user_group.UserGroup, data)

    def create_user_group(self, data) -> uniman.model.user_group.UserGroup:
        return self.client.create(Endpoints.USER_GROUP.value, uniman.model.user_group.UserGroup, data)

    def query_wlan_confs(self) -> uniman.model.wlan_conf.WlanConf:
        return self.client.query(Endpoints.WLAN_CONF.value, uniman.model.wlan_conf.WlanConf)

    def delete_wlan_conf(self, uid: str) -> uniman.model.wlan_conf.WlanConf:
        return self.client.delete(Endpoints.WLAN_CONF.value, uniman.model.wlan_conf.WlanConf, uid)

    def update_wlan_conf(self, data) -> uniman.model.wlan_conf.WlanConf:
        return self.client.update(Endpoints.WLAN_CONF.value, uniman.model.wlan_conf.WlanConf, data)

    def create_wlan_conf(self, data) -> uniman.model.wlan_conf.WlanConf:
        return self.client.create(Endpoints.WLAN_CONF.value, uniman.model.wlan_conf.WlanConf, data)
