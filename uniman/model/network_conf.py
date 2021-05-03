from typing import Any, List

from statham.schema.constants import Maybe
from statham.schema.elements import (
    Array,
    Boolean,
    Element,
    Integer,
    Object,
    String,
)
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class WanProviderCapabilities(Object):

    upload_kilobits_per_second: int = Property(Integer(), required=True)

    download_kilobits_per_second: int = Property(Integer(), required=True)


class DataItem(Object):

    _id: Maybe[str] = Property(String())

    attr_no_delete: Maybe[bool] = Property(Boolean())

    attr_hidden_id: Maybe[str] = Property(String())

    wan_networkgroup: Maybe[str] = Property(String())

    site_id: Maybe[str] = Property(String())

    purpose: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    wan_type: Maybe[str] = Property(String())

    wan_provider_capabilities: Maybe[WanProviderCapabilities] = Property(WanProviderCapabilities)

    report_wan_event: Maybe[bool] = Property(Boolean())

    wan_ip_aliases: Maybe[List[Any]] = Property(Array(Element()))

    wan_type_v6: Maybe[str] = Property(String())

    wan_load_balance_type: Maybe[str] = Property(String())

    wan_load_balance_weight: Maybe[int] = Property(Integer())

    wan_egress_qos: Maybe[str] = Property(String())

    wan_dhcp_options: Maybe[List[Any]] = Property(Array(Element()))

    wan_dns1: Maybe[str] = Property(String())

    vlan_enabled: Maybe[bool] = Property(Boolean())

    ip_subnet: Maybe[str] = Property(String())

    ipv6_interface_type: Maybe[str] = Property(String())

    domain_name: Maybe[str] = Property(String())

    is_nat: Maybe[bool] = Property(Boolean())

    dhcpd_enabled: Maybe[bool] = Property(Boolean())

    dhcpd_start: Maybe[str] = Property(String())

    dhcpd_stop: Maybe[str] = Property(String())

    dhcpdv6_enabled: Maybe[bool] = Property(Boolean())

    ipv6_ra_enabled: Maybe[bool] = Property(Boolean())

    lte_lan_enabled: Maybe[bool] = Property(Boolean())

    networkgroup: Maybe[str] = Property(String())

    dhcpd_leasetime: Maybe[int] = Property(Integer())

    dhcpd_dns_enabled: Maybe[bool] = Property(Boolean())

    dhcpd_gateway_enabled: Maybe[bool] = Property(Boolean())

    dhcpd_time_offset_enabled: Maybe[bool] = Property(Boolean())

    ipv6_pd_start: Maybe[str] = Property(String())

    ipv6_pd_stop: Maybe[str] = Property(String())

    gateway_type: Maybe[str] = Property(String())

    enabled: Maybe[bool] = Property(Boolean())

    dhcp_relay_enabled: Maybe[bool] = Property(Boolean())

    nat_outbound_ip_addresses: Maybe[List[Any]] = Property(Array(Element()))

    dpi_enabled: Maybe[bool] = Property(Boolean())

    dpigroup_id: Maybe[str] = Property(String())

    dhcpd_dns_1: Maybe[str] = Property(String())

    dhcpd_dns_2: Maybe[str] = Property(String())

    ipsec_interface: Maybe[str] = Property(String())

    vpn_type: Maybe[str] = Property(String())

    route_distance: Maybe[int] = Property(Integer())

    ipsec_profile: Maybe[str] = Property(String())

    remote_vpn_subnets: Maybe[List[str]] = Property(Array(String()))

    ipsec_key_exchange: Maybe[str] = Property(String())

    ipsec_encryption: Maybe[str] = Property(String())

    ipsec_hash: Maybe[str] = Property(String())

    ipsec_dh_group: Maybe[int] = Property(Integer())

    ipsec_ike_dh_group: Maybe[int] = Property(Integer())

    ipsec_esp_dh_group: Maybe[int] = Property(Integer())

    ipsec_pfs: Maybe[bool] = Property(Boolean())

    ipsec_dynamic_routing: Maybe[bool] = Property(Boolean())

    x_ipsec_pre_shared_key: Maybe[str] = Property(String())

    ipsec_local_ip: Maybe[str] = Property(String())

    ipsec_peer_ip: Maybe[str] = Property(String())

    ifname: Maybe[str] = Property(String())


class NetworkConf(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
