from typing import Any, List, Union

from statham.schema.constants import Maybe
from statham.schema.elements import (
    AnyOf,
    Array,
    Boolean,
    Element,
    Integer,
    Null,
    Number,
    Object,
    String,
)
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class ConfigNetwork(Object):

    type: str = Property(String(), required=True)

    ip: str = Property(String(), required=True)


class ConfigNetworkLan(Object):

    cidr: str = Property(String(), required=True)

    dhcp_enabled: bool = Property(Boolean(), required=True)

    dhcp_range_start: str = Property(String(), required=True)

    dhcp_range_stop: str = Property(String(), required=True)

    vlan: int = Property(Integer(), required=True)


class AntennaTableItem(Object):

    default: bool = Property(Boolean(), required=True)

    id: int = Property(Integer(), required=True)

    name: str = Property(String(), required=True)

    ra0_gain: int = Property(Integer(), required=True)

    rai0_gain: int = Property(Integer(), required=True)


class RadioTableItem(Object):

    radio: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    channel: str = Property(String(), required=True)

    ht: str = Property(String(), required=True)

    max_txpower: int = Property(Integer(), required=True)

    min_txpower: int = Property(Integer(), required=True)

    nss: int = Property(Integer(), required=True)

    min_rssi_enabled: bool = Property(Boolean(), required=True)

    sens_level_enabled: bool = Property(Boolean(), required=True)

    vwire_enabled: bool = Property(Boolean(), required=True)

    radio_caps: int = Property(Integer(), required=True)

    builtin_antenna: bool = Property(Boolean(), required=True)

    builtin_ant_gain: int = Property(Integer(), required=True)

    loadbalance_enabled: bool = Property(Boolean(), required=True)

    current_antenna_gain: int = Property(Integer(), required=True)

    radio_caps2: int = Property(Integer(), required=True)

    is_11ac: Maybe[bool] = Property(Boolean())

    has_dfs: Maybe[bool] = Property(Boolean())

    has_fccdfs: Maybe[bool] = Property(Boolean())

    has_ht160: Maybe[bool] = Property(Boolean())


class EthernetTableItem(Object):

    mac: str = Property(String(), required=True)

    num_port: int = Property(Integer(), required=True)

    name: str = Property(String(), required=True)


class PortDelta(Object):

    time_delta: int = Property(Integer(), required=True)

    time_delta_activity: int = Property(Integer(), required=True)


class MacTableItem(Object):

    age: int = Property(Integer(), required=True)

    authorized: bool = Property(Boolean(), required=True)

    hostname: str = Property(String(), required=True)

    ip: str = Property(String(), required=True)

    lastReachable: int = Property(Integer(), required=True)

    mac: str = Property(String(), required=True)


class PortTableItem(Object):

    port_idx: int = Property(Integer(), required=True)

    media: str = Property(String(), required=True)

    port_poe: bool = Property(Boolean(), required=True)

    speed_caps: int = Property(Integer(), required=True)

    op_mode: str = Property(String(), required=True)

    portconf_id: str = Property(String(), required=True)

    autoneg: bool = Property(Boolean(), required=True)

    enable: bool = Property(Boolean(), required=True)

    flowctrl_rx: bool = Property(Boolean(), required=True)

    flowctrl_tx: bool = Property(Boolean(), required=True)

    full_duplex: bool = Property(Boolean(), required=True)

    is_uplink: bool = Property(Boolean(), required=True)

    mac: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    num_port: int = Property(Integer(), required=True)

    rx_broadcast: int = Property(Integer(), required=True)

    rx_bytes: int = Property(Integer(), required=True)

    rx_dropped: int = Property(Integer(), required=True)

    rx_errors: int = Property(Integer(), required=True)

    rx_multicast: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    rx_rate: int = Property(Integer(), required=True)

    rx_rate_max: int = Property(Integer(), required=True, source='rx_rate-max')

    speed: int = Property(Integer(), required=True)

    tx_broadcast: int = Property(Integer(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    tx_dropped: int = Property(Integer(), required=True)

    tx_errors: int = Property(Integer(), required=True)

    tx_multicast: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)

    tx_rate: int = Property(Integer(), required=True)

    tx_rate_max: int = Property(Integer(), required=True, source='tx_rate-max')

    type: str = Property(String(), required=True)

    up: bool = Property(Boolean(), required=True)

    ifname: str = Property(String(), required=True)

    ip: str = Property(String(), required=True)

    netmask: Maybe[str] = Property(String())

    tx_bytes_r: int = Property(Integer(), required=True, source='tx_bytes-r')

    rx_bytes_r: int = Property(Integer(), required=True, source='rx_bytes-r')

    bytes_r: int = Property(Integer(), required=True, source='bytes-r')

    port_delta: Maybe[PortDelta] = Property(PortDelta)

    network_name: str = Property(String(), required=True)

    masked: bool = Property(Boolean(), required=True)

    aggregated_by: bool = Property(Boolean(), required=True)

    mac_table: Maybe[List[MacTableItem]] = Property(Array(MacTableItem))

    dns: Maybe[List[str]] = Property(Array(String()))


class EthernetOverridesItem(Object):

    ifname: str = Property(String(), required=True)

    networkgroup: str = Property(String(), required=True)


class SwitchCaps(Object):

    max_mirror_sessions: int = Property(Integer(), required=True)

    max_aggregate_sessions: int = Property(Integer(), required=True)


class TemperaturesItem(Object):

    name: str = Property(String(), required=True)

    type: str = Property(String(), required=True)

    value: float = Property(Number(), required=True)


class StorageItem(Object):

    mount_point: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    size: int = Property(Integer(), required=True)

    type: str = Property(String(), required=True)

    used: int = Property(Integer(), required=True)


class RulesetInterfaces(Object):

    br0: str = Property(String(), required=True)

    eth4: str = Property(String(), required=True)


class UnifiCare(Object):

    state: str = Property(String(), required=True)

    registration: int = Property(Integer(), required=True)

    activation_end: None = Property(Null(), required=True)

    activation_url: None = Property(Null(), required=True)

    coverage_start: None = Property(Null(), required=True)

    coverage_end: None = Property(Null(), required=True)

    rma_url: None = Property(Null(), required=True)

    tracking_url: None = Property(Null(), required=True)

    activation_dismissed: None = Property(Null(), required=True)


class SysStats(Object):

    loadavg_1: str = Property(String(), required=True)

    loadavg_15: str = Property(String(), required=True)

    loadavg_5: str = Property(String(), required=True)

    mem_buffer: int = Property(Integer(), required=True)

    mem_total: int = Property(Integer(), required=True)

    mem_used: int = Property(Integer(), required=True)


class SystemStats(Object):

    cpu: str = Property(String(), required=True)

    mem: str = Property(String(), required=True)

    uptime: str = Property(String(), required=True)


class LldpTableItem(Object):

    chassis_id: str = Property(String(), required=True)

    is_wired: bool = Property(Boolean(), required=True)

    local_port_idx: int = Property(Integer(), required=True)

    local_port_name: str = Property(String(), required=True)

    port_id: str = Property(String(), required=True)


class WAN(Object):

    availability: float = Property(Number(), required=True)

    latency_average: int = Property(Integer(), required=True)

    time_period: int = Property(Integer(), required=True)


class UptimeStats(Object):

    WAN: WAN = Property(WAN, required=True)


class WAN_1(Object):

    accuracy: float = Property(Number(), required=True)

    address: str = Property(String(), required=True)

    asn: int = Property(Integer(), required=True)

    city: str = Property(String(), required=True)

    continent_code: str = Property(String(), required=True)

    country_code: str = Property(String(), required=True)

    country_name: str = Property(String(), required=True)

    isp_name: str = Property(String(), required=True)

    isp_organization: str = Property(String(), required=True)

    latitude: float = Property(Number(), required=True)

    longitude: float = Property(Number(), required=True)

    timezone: str = Property(String(), required=True)


class GeoInfo(Object):

    WAN: WAN_1 = Property(WAN_1, required=True)


class LedState(Object):

    pattern: str = Property(String(), required=True)

    tempo: int = Property(Integer(), required=True)


class RadioTableStatsItem(Object):

    name: str = Property(String(), required=True)

    channel: int = Property(Integer(), required=True)

    radio: str = Property(String(), required=True)

    ast_txto: None = Property(Null(), required=True)

    ast_cst: None = Property(Null(), required=True)

    ast_be_xmit: Union[int, None] = Property(AnyOf(Integer(), Null()), required=True)

    cu_total: int = Property(Integer(), required=True)

    cu_self_rx: int = Property(Integer(), required=True)

    cu_self_tx: int = Property(Integer(), required=True)

    gain: int = Property(Integer(), required=True)

    satisfaction: int = Property(Integer(), required=True)

    state: str = Property(String(), required=True)

    extchannel: int = Property(Integer(), required=True)

    tx_power: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)

    tx_retries: int = Property(Integer(), required=True)

    num_sta: int = Property(Integer(), required=True)

    guest_num_sta: int = Property(Integer(), required=True, source='guest-num_sta')

    user_num_sta: int = Property(Integer(), required=True, source='user-num_sta')


class Server(Object):

    cc: str = Property(String(), required=True)

    city: str = Property(String(), required=True)

    country: str = Property(String(), required=True)

    lat: float = Property(Number(), required=True)

    lon: float = Property(Number(), required=True)

    provider: str = Property(String(), required=True)

    provider_url: str = Property(String(), required=True)


class SpeedtestStatus(Object):

    latency: int = Property(Integer(), required=True)

    rundate: int = Property(Integer(), required=True)

    runtime: int = Property(Integer(), required=True)

    server: Server = Property(Server, required=True)

    source_interface: str = Property(String(), required=True)

    status_download: int = Property(Integer(), required=True)

    status_ping: int = Property(Integer(), required=True)

    status_summary: int = Property(Integer(), required=True)

    status_upload: int = Property(Integer(), required=True)

    xput_download: float = Property(Number(), required=True)

    xput_upload: float = Property(Number(), required=True)


class Wan1(Object):

    max_speed: int = Property(Integer(), required=True)

    type: str = Property(String(), required=True)

    autoneg: bool = Property(Boolean(), required=True)

    enable: bool = Property(Boolean(), required=True)

    flowctrl_rx: bool = Property(Boolean(), required=True)

    flowctrl_tx: bool = Property(Boolean(), required=True)

    full_duplex: bool = Property(Boolean(), required=True)

    is_uplink: bool = Property(Boolean(), required=True)

    mac: str = Property(String(), required=True)

    mac_table: List[MacTableItem] = Property(Array(MacTableItem), required=True)

    media: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    num_port: int = Property(Integer(), required=True)

    port_idx: int = Property(Integer(), required=True)

    port_poe: bool = Property(Boolean(), required=True)

    rx_broadcast: int = Property(Integer(), required=True)

    rx_bytes: int = Property(Integer(), required=True)

    rx_dropped: int = Property(Integer(), required=True)

    rx_errors: int = Property(Integer(), required=True)

    rx_multicast: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    rx_rate: int = Property(Integer(), required=True)

    rx_rate_max: int = Property(Integer(), required=True, source='rx_rate-max')

    speed: int = Property(Integer(), required=True)

    speed_caps: int = Property(Integer(), required=True)

    tx_broadcast: int = Property(Integer(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    tx_dropped: int = Property(Integer(), required=True)

    tx_errors: int = Property(Integer(), required=True)

    tx_multicast: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)

    tx_rate: int = Property(Integer(), required=True)

    tx_rate_max: int = Property(Integer(), required=True, source='tx_rate-max')

    up: bool = Property(Boolean(), required=True)

    ifname: str = Property(String(), required=True)

    ip: str = Property(String(), required=True)

    netmask: str = Property(String(), required=True)

    tx_bytes_r: int = Property(Integer(), required=True, source='tx_bytes-r')

    rx_bytes_r: int = Property(Integer(), required=True, source='rx_bytes-r')

    bytes_r: int = Property(Integer(), required=True, source='bytes-r')

    dns: List[str] = Property(Array(String()), required=True)


class Uplink(Object):

    drops: int = Property(Integer(), required=True)

    ip: str = Property(String(), required=True)

    latency: int = Property(Integer(), required=True)

    name: str = Property(String(), required=True)

    nameservers: List[str] = Property(Array(String()), required=True)

    netmask: str = Property(String(), required=True)

    num_port: int = Property(Integer(), required=True)

    rx_bytes: int = Property(Integer(), required=True)

    rx_dropped: int = Property(Integer(), required=True)

    rx_errors: int = Property(Integer(), required=True)

    rx_multicast: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    speedtest_lastrun: int = Property(Integer(), required=True)

    speedtest_ping: int = Property(Integer(), required=True)

    speedtest_status: str = Property(String(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    tx_dropped: int = Property(Integer(), required=True)

    tx_errors: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)

    up: bool = Property(Boolean(), required=True)

    uptime: int = Property(Integer(), required=True)

    xput_down: float = Property(Number(), required=True)

    xput_up: float = Property(Number(), required=True)

    port_idx: int = Property(Integer(), required=True)

    media: str = Property(String(), required=True)

    rx_rate: int = Property(Integer(), required=True)

    tx_rate: int = Property(Integer(), required=True)

    max_speed: int = Property(Integer(), required=True)

    type: str = Property(String(), required=True)

    speed: int = Property(Integer(), required=True)

    full_duplex: bool = Property(Boolean(), required=True)

    tx_bytes_r: int = Property(Integer(), required=True, source='tx_bytes-r')

    rx_bytes_r: int = Property(Integer(), required=True, source='rx_bytes-r')


class AnomaliesBarChart(Object):

    high_dns_latency: int = Property(Integer(), required=True)

    high_icmp_rtt: int = Property(Integer(), required=True)

    high_tcp_latency: int = Property(Integer(), required=True)

    high_tcp_packet_loss: int = Property(Integer(), required=True)

    high_wifi_latency: int = Property(Integer(), required=True)

    high_wifi_retries: int = Property(Integer(), required=True)

    low_phy_rate: int = Property(Integer(), required=True)

    poor_stream_eff: int = Property(Integer(), required=True)

    sleepy_client: int = Property(Integer(), required=True)

    sta_arp_timeout: int = Property(Integer(), required=True)

    sta_dns_timeout: int = Property(Integer(), required=True)

    sta_ip_timeout: int = Property(Integer(), required=True)

    weak_signal: int = Property(Integer(), required=True)


class AnomaliesBarChartNow(Object):

    high_dns_latency: int = Property(Integer(), required=True)

    high_icmp_rtt: int = Property(Integer(), required=True)

    high_tcp_latency: int = Property(Integer(), required=True)

    high_tcp_packet_loss: int = Property(Integer(), required=True)

    high_wifi_latency: int = Property(Integer(), required=True)

    high_wifi_retries: int = Property(Integer(), required=True)

    low_phy_rate: int = Property(Integer(), required=True)

    poor_stream_eff: int = Property(Integer(), required=True)

    sleepy_client: int = Property(Integer(), required=True)

    sta_arp_timeout: int = Property(Integer(), required=True)

    sta_dns_timeout: int = Property(Integer(), required=True)

    sta_ip_timeout: int = Property(Integer(), required=True)

    weak_signal: int = Property(Integer(), required=True)


class ReasonsBarChart(Object):

    phy_rate: int = Property(Integer(), required=True)

    signal: int = Property(Integer(), required=True)

    sleepy_client: int = Property(Integer(), required=True)

    sta_arp_timeout: int = Property(Integer(), required=True)

    sta_dns_latency: int = Property(Integer(), required=True)

    sta_dns_timeout: int = Property(Integer(), required=True)

    sta_icmp_rtt: int = Property(Integer(), required=True)

    sta_ip_timeout: int = Property(Integer(), required=True)

    stream_eff: int = Property(Integer(), required=True)

    tcp_latency: int = Property(Integer(), required=True)

    tcp_packet_loss: int = Property(Integer(), required=True)

    wifi_latency: int = Property(Integer(), required=True)

    wifi_retries: int = Property(Integer(), required=True)


class ReasonsBarChartNow(Object):

    phy_rate: int = Property(Integer(), required=True)

    signal: int = Property(Integer(), required=True)

    sleepy_client: int = Property(Integer(), required=True)

    sta_arp_timeout: int = Property(Integer(), required=True)

    sta_dns_latency: int = Property(Integer(), required=True)

    sta_dns_timeout: int = Property(Integer(), required=True)

    sta_icmp_rtt: int = Property(Integer(), required=True)

    sta_ip_timeout: int = Property(Integer(), required=True)

    stream_eff: int = Property(Integer(), required=True)

    tcp_latency: int = Property(Integer(), required=True)

    tcp_packet_loss: int = Property(Integer(), required=True)

    wifi_latency: int = Property(Integer(), required=True)

    wifi_retries: int = Property(Integer(), required=True)


class RxTcpStats(Object):

    goodbytes: int = Property(Integer(), required=True)

    lat_avg: int = Property(Integer(), required=True)

    lat_max: int = Property(Integer(), required=True)

    lat_min: int = Property(Integer(), required=True)

    lat_samples: int = Property(Integer(), required=True)

    lat_sum: int = Property(Integer(), required=True)

    stalls: int = Property(Integer(), required=True)


class TxTcpStats(Object):

    goodbytes: int = Property(Integer(), required=True)

    lat_avg: int = Property(Integer(), required=True)

    lat_max: int = Property(Integer(), required=True)

    lat_min: int = Property(Integer(), required=True)

    lat_samples: int = Property(Integer(), required=True)

    lat_sum: int = Property(Integer(), required=True)

    stalls: int = Property(Integer(), required=True)


class VapTableItem(Object):

    anomalies_bar_chart: AnomaliesBarChart = Property(AnomaliesBarChart, required=True)

    anomalies_bar_chart_now: AnomaliesBarChartNow = Property(AnomaliesBarChartNow, required=True)

    avg_client_signal: int = Property(Integer(), required=True)

    bssid: str = Property(String(), required=True)

    bw: int = Property(Integer(), required=True)

    ccq: int = Property(Integer(), required=True)

    channel: int = Property(Integer(), required=True)

    dns_avg_latency: int = Property(Integer(), required=True)

    essid: str = Property(String(), required=True)

    extchannel: Maybe[int] = Property(Integer())

    icmp_avg_rtt: int = Property(Integer(), required=True)

    id: str = Property(String(), required=True)

    mac_filter_rejections: int = Property(Integer(), required=True)

    name: str = Property(String(), required=True)

    num_satisfaction_sta: int = Property(Integer(), required=True)

    num_sta: int = Property(Integer(), required=True)

    radio: str = Property(String(), required=True)

    radio_name: str = Property(String(), required=True)

    reasons_bar_chart: ReasonsBarChart = Property(ReasonsBarChart, required=True)

    reasons_bar_chart_now: ReasonsBarChartNow = Property(ReasonsBarChartNow, required=True)

    rx_bytes: int = Property(Integer(), required=True)

    rx_crypts: int = Property(Integer(), required=True)

    rx_dropped: int = Property(Integer(), required=True)

    rx_errors: int = Property(Integer(), required=True)

    rx_frags: int = Property(Integer(), required=True)

    rx_nwids: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    rx_tcp_stats: RxTcpStats = Property(RxTcpStats, required=True)

    satisfaction: int = Property(Integer(), required=True)

    satisfaction_now: int = Property(Integer(), required=True)

    satisfaction_real: int = Property(Integer(), required=True)

    state: str = Property(String(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    tx_combined_retries: int = Property(Integer(), required=True)

    tx_data_mpdu_bytes: int = Property(Integer(), required=True)

    tx_dropped: int = Property(Integer(), required=True)

    tx_errors: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)

    tx_power: int = Property(Integer(), required=True)

    tx_retries: int = Property(Integer(), required=True)

    tx_rts_retries: int = Property(Integer(), required=True)

    tx_success: int = Property(Integer(), required=True)

    tx_tcp_stats: TxTcpStats = Property(TxTcpStats, required=True)

    tx_total: int = Property(Integer(), required=True)

    up: bool = Property(Boolean(), required=True)

    usage: str = Property(String(), required=True)

    wifi_tx_attempts: int = Property(Integer(), required=True)

    wifi_tx_dropped: int = Property(Integer(), required=True)

    t: str = Property(String(), required=True)

    wlanconf_id: str = Property(String(), required=True)

    is_guest: bool = Property(Boolean(), required=True)

    is_wep: bool = Property(Boolean(), required=True)

    ap_mac: str = Property(String(), required=True)

    map_id: None = Property(Null(), required=True)

    site_id: str = Property(String(), required=True)


class VwireVapTableItem(Object):

    state: str = Property(String(), required=True)

    radio: str = Property(String(), required=True)

    radio_name: str = Property(String(), required=True)

    bssid: str = Property(String(), required=True)


class ByCatItem(Object):

    cat: int = Property(Integer(), required=True)

    apps: List[int] = Property(Array(Integer()), required=True)

    rx_bytes: int = Property(Integer(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)


class ClientsItem(Object):

    mac: str = Property(String(), required=True)

    rx_bytes: int = Property(Integer(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)


class ByAppItem(Object):

    app: int = Property(Integer(), required=True)

    cat: int = Property(Integer(), required=True)

    clients: List[ClientsItem] = Property(Array(ClientsItem), required=True)

    known_clients: int = Property(Integer(), required=True)

    rx_bytes: int = Property(Integer(), required=True)

    tx_bytes: int = Property(Integer(), required=True)

    rx_packets: int = Property(Integer(), required=True)

    tx_packets: int = Property(Integer(), required=True)


class DpistatsTable(Object):

    last_updated: int = Property(Integer(), required=True)

    by_cat: List[ByCatItem] = Property(Array(ByCatItem), required=True)

    by_app: List[ByAppItem] = Property(Array(ByAppItem), required=True)


class NetworkTableItem(Object):

    _id: str = Property(String(), required=True)

    attr_no_delete: Maybe[bool] = Property(Boolean())

    attr_hidden_id: Maybe[str] = Property(String())

    name: str = Property(String(), required=True)

    site_id: str = Property(String(), required=True)

    vlan_enabled: Maybe[bool] = Property(Boolean())

    purpose: str = Property(String(), required=True)

    ip_subnet: Maybe[str] = Property(String())

    ipv6_interface_type: Maybe[str] = Property(String())

    domain_name: Maybe[str] = Property(String())

    is_nat: bool = Property(Boolean(), required=True)

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

    enabled: bool = Property(Boolean(), required=True)

    dhcp_relay_enabled: Maybe[bool] = Property(Boolean())

    nat_outbound_ip_addresses: Maybe[List[Any]] = Property(Array(Element()))

    dpi_enabled: Maybe[bool] = Property(Boolean())

    dpigroup_id: Maybe[str] = Property(String())

    dhcpd_dns_1: Maybe[str] = Property(String())

    dhcpd_dns_2: Maybe[str] = Property(String())

    is_guest: bool = Property(Boolean(), required=True)

    ip: Union[None, str] = Property(AnyOf(Null(), String()), required=True)

    mac: Maybe[str] = Property(String())

    up: Union[bool, str] = Property(AnyOf(Boolean(), String()), required=True)

    active_dhcp_lease_count: Maybe[int] = Property(Integer())

    gateway_interface_name: Maybe[str] = Property(String())

    dpistats_table: Maybe[DpistatsTable] = Property(DpistatsTable)

    num_sta: Maybe[int] = Property(Integer())

    rx_bytes: Maybe[int] = Property(Integer())

    rx_packets: Maybe[int] = Property(Integer())

    tx_bytes: Maybe[int] = Property(Integer())

    tx_packets: Maybe[int] = Property(Integer())

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


class Ap(Object):

    site_id: str = Property(String(), required=True)

    o: str = Property(String(), required=True)

    oid: str = Property(String(), required=True)

    ap: str = Property(String(), required=True)

    time: int = Property(Integer(), required=True)

    datetime: str = Property(String(), required=True)

    user_rai0_rx_packets: float = Property(Number(), required=True, source='user-rai0-rx_packets')

    user_ra0_rx_packets: float = Property(Number(), required=True, source='user-ra0-rx_packets')

    user_rx_packets: float = Property(Number(), required=True, source='user-rx_packets')

    guest_rx_packets: float = Property(Number(), required=True, source='guest-rx_packets')

    ra0_rx_packets: float = Property(Number(), required=True, source='ra0-rx_packets')

    rai0_rx_packets: float = Property(Number(), required=True, source='rai0-rx_packets')

    rx_packets: float = Property(Number(), required=True)

    user_rai0_rx_bytes: float = Property(Number(), required=True, source='user-rai0-rx_bytes')

    user_ra0_rx_bytes: float = Property(Number(), required=True, source='user-ra0-rx_bytes')

    user_rx_bytes: float = Property(Number(), required=True, source='user-rx_bytes')

    guest_rx_bytes: float = Property(Number(), required=True, source='guest-rx_bytes')

    ra0_rx_bytes: float = Property(Number(), required=True, source='ra0-rx_bytes')

    rai0_rx_bytes: float = Property(Number(), required=True, source='rai0-rx_bytes')

    rx_bytes: float = Property(Number(), required=True)

    user_rai0_rx_errors: float = Property(Number(), required=True, source='user-rai0-rx_errors')

    user_ra0_rx_errors: float = Property(Number(), required=True, source='user-ra0-rx_errors')

    user_rx_errors: float = Property(Number(), required=True, source='user-rx_errors')

    guest_rx_errors: float = Property(Number(), required=True, source='guest-rx_errors')

    ra0_rx_errors: float = Property(Number(), required=True, source='ra0-rx_errors')

    rai0_rx_errors: float = Property(Number(), required=True, source='rai0-rx_errors')

    rx_errors: float = Property(Number(), required=True)

    user_rai0_rx_dropped: float = Property(Number(), required=True, source='user-rai0-rx_dropped')

    user_ra0_rx_dropped: float = Property(Number(), required=True, source='user-ra0-rx_dropped')

    user_rx_dropped: float = Property(Number(), required=True, source='user-rx_dropped')

    guest_rx_dropped: float = Property(Number(), required=True, source='guest-rx_dropped')

    ra0_rx_dropped: float = Property(Number(), required=True, source='ra0-rx_dropped')

    rai0_rx_dropped: float = Property(Number(), required=True, source='rai0-rx_dropped')

    rx_dropped: float = Property(Number(), required=True)

    user_rai0_rx_crypts: float = Property(Number(), required=True, source='user-rai0-rx_crypts')

    user_ra0_rx_crypts: float = Property(Number(), required=True, source='user-ra0-rx_crypts')

    user_rx_crypts: float = Property(Number(), required=True, source='user-rx_crypts')

    guest_rx_crypts: float = Property(Number(), required=True, source='guest-rx_crypts')

    ra0_rx_crypts: float = Property(Number(), required=True, source='ra0-rx_crypts')

    rai0_rx_crypts: float = Property(Number(), required=True, source='rai0-rx_crypts')

    rx_crypts: float = Property(Number(), required=True)

    user_rai0_rx_frags: float = Property(Number(), required=True, source='user-rai0-rx_frags')

    user_ra0_rx_frags: float = Property(Number(), required=True, source='user-ra0-rx_frags')

    user_rx_frags: float = Property(Number(), required=True, source='user-rx_frags')

    guest_rx_frags: float = Property(Number(), required=True, source='guest-rx_frags')

    ra0_rx_frags: float = Property(Number(), required=True, source='ra0-rx_frags')

    rai0_rx_frags: float = Property(Number(), required=True, source='rai0-rx_frags')

    rx_frags: float = Property(Number(), required=True)

    user_rai0_tx_packets: float = Property(Number(), required=True, source='user-rai0-tx_packets')

    user_ra0_tx_packets: float = Property(Number(), required=True, source='user-ra0-tx_packets')

    user_tx_packets: float = Property(Number(), required=True, source='user-tx_packets')

    guest_tx_packets: float = Property(Number(), required=True, source='guest-tx_packets')

    ra0_tx_packets: float = Property(Number(), required=True, source='ra0-tx_packets')

    rai0_tx_packets: float = Property(Number(), required=True, source='rai0-tx_packets')

    tx_packets: float = Property(Number(), required=True)

    user_rai0_tx_bytes: float = Property(Number(), required=True, source='user-rai0-tx_bytes')

    user_ra0_tx_bytes: float = Property(Number(), required=True, source='user-ra0-tx_bytes')

    user_tx_bytes: float = Property(Number(), required=True, source='user-tx_bytes')

    guest_tx_bytes: float = Property(Number(), required=True, source='guest-tx_bytes')

    ra0_tx_bytes: float = Property(Number(), required=True, source='ra0-tx_bytes')

    rai0_tx_bytes: float = Property(Number(), required=True, source='rai0-tx_bytes')

    tx_bytes: float = Property(Number(), required=True)

    user_rai0_tx_errors: float = Property(Number(), required=True, source='user-rai0-tx_errors')

    user_ra0_tx_errors: float = Property(Number(), required=True, source='user-ra0-tx_errors')

    user_tx_errors: float = Property(Number(), required=True, source='user-tx_errors')

    guest_tx_errors: float = Property(Number(), required=True, source='guest-tx_errors')

    ra0_tx_errors: float = Property(Number(), required=True, source='ra0-tx_errors')

    rai0_tx_errors: float = Property(Number(), required=True, source='rai0-tx_errors')

    tx_errors: float = Property(Number(), required=True)

    user_rai0_tx_dropped: float = Property(Number(), required=True, source='user-rai0-tx_dropped')

    user_ra0_tx_dropped: float = Property(Number(), required=True, source='user-ra0-tx_dropped')

    user_tx_dropped: float = Property(Number(), required=True, source='user-tx_dropped')

    guest_tx_dropped: float = Property(Number(), required=True, source='guest-tx_dropped')

    ra0_tx_dropped: float = Property(Number(), required=True, source='ra0-tx_dropped')

    rai0_tx_dropped: float = Property(Number(), required=True, source='rai0-tx_dropped')

    tx_dropped: float = Property(Number(), required=True)

    user_rai0_tx_retries: float = Property(Number(), required=True, source='user-rai0-tx_retries')

    user_ra0_tx_retries: float = Property(Number(), required=True, source='user-ra0-tx_retries')

    user_tx_retries: float = Property(Number(), required=True, source='user-tx_retries')

    guest_tx_retries: float = Property(Number(), required=True, source='guest-tx_retries')

    ra0_tx_retries: float = Property(Number(), required=True, source='ra0-tx_retries')

    rai0_tx_retries: float = Property(Number(), required=True, source='rai0-tx_retries')

    tx_retries: float = Property(Number(), required=True)

    user_rai0_mac_filter_rejections: float = Property(Number(), required=True, source='user-rai0-mac_filter_rejections')

    user_ra0_mac_filter_rejections: float = Property(Number(), required=True, source='user-ra0-mac_filter_rejections')

    user_mac_filter_rejections: float = Property(Number(), required=True, source='user-mac_filter_rejections')

    guest_mac_filter_rejections: float = Property(Number(), required=True, source='guest-mac_filter_rejections')

    ra0_mac_filter_rejections: float = Property(Number(), required=True, source='ra0-mac_filter_rejections')

    rai0_mac_filter_rejections: float = Property(Number(), required=True, source='rai0-mac_filter_rejections')

    mac_filter_rejections: float = Property(Number(), required=True)

    user_rai0_wifi_tx_attempts: float = Property(Number(), required=True, source='user-rai0-wifi_tx_attempts')

    user_ra0_wifi_tx_attempts: float = Property(Number(), required=True, source='user-ra0-wifi_tx_attempts')

    user_wifi_tx_attempts: float = Property(Number(), required=True, source='user-wifi_tx_attempts')

    guest_wifi_tx_attempts: float = Property(Number(), required=True, source='guest-wifi_tx_attempts')

    ra0_wifi_tx_attempts: float = Property(Number(), required=True, source='ra0-wifi_tx_attempts')

    rai0_wifi_tx_attempts: float = Property(Number(), required=True, source='rai0-wifi_tx_attempts')

    wifi_tx_attempts: float = Property(Number(), required=True)

    user_rai0_wifi_tx_dropped: float = Property(Number(), required=True, source='user-rai0-wifi_tx_dropped')

    user_ra0_wifi_tx_dropped: float = Property(Number(), required=True, source='user-ra0-wifi_tx_dropped')

    user_wifi_tx_dropped: float = Property(Number(), required=True, source='user-wifi_tx_dropped')

    guest_wifi_tx_dropped: float = Property(Number(), required=True, source='guest-wifi_tx_dropped')

    ra0_wifi_tx_dropped: float = Property(Number(), required=True, source='ra0-wifi_tx_dropped')

    rai0_wifi_tx_dropped: float = Property(Number(), required=True, source='rai0-wifi_tx_dropped')

    wifi_tx_dropped: float = Property(Number(), required=True)

    bytes: float = Property(Number(), required=True)

    duration: float = Property(Number(), required=True)


class Sw(Object):

    site_id: str = Property(String(), required=True)

    o: str = Property(String(), required=True)

    oid: str = Property(String(), required=True)

    sw: str = Property(String(), required=True)

    time: int = Property(Integer(), required=True)

    datetime: str = Property(String(), required=True)

    rx_packets: float = Property(Number(), required=True)

    rx_bytes: float = Property(Number(), required=True)

    rx_errors: float = Property(Number(), required=True)

    rx_dropped: float = Property(Number(), required=True)

    rx_crypts: float = Property(Number(), required=True)

    rx_frags: float = Property(Number(), required=True)

    tx_packets: float = Property(Number(), required=True)

    tx_bytes: float = Property(Number(), required=True)

    tx_errors: float = Property(Number(), required=True)

    tx_dropped: float = Property(Number(), required=True)

    tx_retries: float = Property(Number(), required=True)

    rx_multicast: float = Property(Number(), required=True)

    rx_broadcast: float = Property(Number(), required=True)

    tx_multicast: float = Property(Number(), required=True)

    tx_broadcast: float = Property(Number(), required=True)

    bytes: float = Property(Number(), required=True)

    duration: float = Property(Number(), required=True)

    port_3_tx_packets: float = Property(Number(), required=True, source='port_3-tx_packets')

    port_3_tx_bytes: float = Property(Number(), required=True, source='port_3-tx_bytes')

    port_3_tx_multicast: float = Property(Number(), required=True, source='port_3-tx_multicast')

    port_3_tx_broadcast: float = Property(Number(), required=True, source='port_3-tx_broadcast')

    port_4_rx_packets: float = Property(Number(), required=True, source='port_4-rx_packets')

    port_4_rx_bytes: float = Property(Number(), required=True, source='port_4-rx_bytes')

    port_4_tx_packets: float = Property(Number(), required=True, source='port_4-tx_packets')

    port_4_tx_bytes: float = Property(Number(), required=True, source='port_4-tx_bytes')

    port_4_tx_multicast: float = Property(Number(), required=True, source='port_4-tx_multicast')

    port_4_tx_broadcast: float = Property(Number(), required=True, source='port_4-tx_broadcast')

    port_3_rx_packets: float = Property(Number(), required=True, source='port_3-rx_packets')

    port_3_rx_bytes: float = Property(Number(), required=True, source='port_3-rx_bytes')

    port_3_rx_multicast: float = Property(Number(), required=True, source='port_3-rx_multicast')

    port_4_rx_multicast: float = Property(Number(), required=True, source='port_4-rx_multicast')

    port_4_rx_broadcast: float = Property(Number(), required=True, source='port_4-rx_broadcast')

    port_3_rx_broadcast: float = Property(Number(), required=True, source='port_3-rx_broadcast')

    port_2_rx_packets: float = Property(Number(), required=True, source='port_2-rx_packets')

    port_2_rx_bytes: float = Property(Number(), required=True, source='port_2-rx_bytes')

    port_2_tx_packets: float = Property(Number(), required=True, source='port_2-tx_packets')

    port_2_tx_bytes: float = Property(Number(), required=True, source='port_2-tx_bytes')

    port_2_rx_multicast: float = Property(Number(), required=True, source='port_2-rx_multicast')

    port_2_rx_broadcast: float = Property(Number(), required=True, source='port_2-rx_broadcast')

    port_2_tx_multicast: float = Property(Number(), required=True, source='port_2-tx_multicast')

    port_2_tx_broadcast: float = Property(Number(), required=True, source='port_2-tx_broadcast')


class Gw(Object):

    site_id: str = Property(String(), required=True)

    o: str = Property(String(), required=True)

    oid: str = Property(String(), required=True)

    gw: str = Property(String(), required=True)

    time: int = Property(Integer(), required=True)

    datetime: str = Property(String(), required=True)

    duration: float = Property(Number(), required=True)


class Stat(Object):

    ap: Ap = Property(Ap, required=True)

    sw: Sw = Property(Sw, required=True)

    gw: Gw = Property(Gw, required=True)


class DataItem(Object):

    _id: Maybe[str] = Property(String())

    ip: Maybe[str] = Property(String())

    mac: Maybe[str] = Property(String())

    model: Maybe[str] = Property(String())

    model_in_lts: Maybe[bool] = Property(Boolean())

    model_in_eol: Maybe[bool] = Property(Boolean())

    type: Maybe[str] = Property(String())

    version: Maybe[str] = Property(String())

    adopted: Maybe[bool] = Property(Boolean())

    site_id: Maybe[str] = Property(String())

    x_authkey: Maybe[str] = Property(String())

    cfgversion: Maybe[str] = Property(String())

    syslog_key: Maybe[str] = Property(String())

    config_network: Maybe[ConfigNetwork] = Property(ConfigNetwork)

    x_vwirekey: Maybe[str] = Property(String())

    vwire_table: Maybe[List[Any]] = Property(Array(Element()))

    dot1x_portctrl_enabled: Maybe[bool] = Property(Boolean())

    jumboframe_enabled: Maybe[bool] = Property(Boolean())

    flowctrl_enabled: Maybe[bool] = Property(Boolean())

    stp_version: Maybe[str] = Property(String())

    stp_priority: Maybe[str] = Property(String())

    power_source_ctrl_enabled: Maybe[bool] = Property(Boolean())

    license_state: Maybe[str] = Property(String())

    x_fingerprint: Maybe[str] = Property(String())

    inform_url: Maybe[str] = Property(String())

    inform_ip: Maybe[str] = Property(String())

    x_aes_gcm: Maybe[bool] = Property(Boolean())

    config_network_lan: Maybe[ConfigNetworkLan] = Property(ConfigNetworkLan)

    required_version: Maybe[str] = Property(String())

    kernel_version: Maybe[str] = Property(String())

    architecture: Maybe[str] = Property(String())

    board_rev: Maybe[int] = Property(Integer())

    manufacturer_id: Maybe[int] = Property(Integer())

    model_incompatible: Maybe[bool] = Property(Boolean())

    internet: Maybe[bool] = Property(Boolean())

    antenna_table: Maybe[List[AntennaTableItem]] = Property(Array(AntennaTableItem))

    radio_table: Maybe[List[RadioTableItem]] = Property(Array(RadioTableItem))

    scan_radio_table: Maybe[List[Any]] = Property(Array(Element()))

    ethernet_table: Maybe[List[EthernetTableItem]] = Property(Array(EthernetTableItem))

    port_table: Maybe[List[PortTableItem]] = Property(Array(PortTableItem))

    ethernet_overrides: Maybe[List[EthernetOverridesItem]] = Property(Array(EthernetOverridesItem))

    usg_caps: Maybe[int] = Property(Integer())

    has_speaker: Maybe[bool] = Property(Boolean())

    has_eth1: Maybe[bool] = Property(Boolean())

    fw_caps: Maybe[int] = Property(Integer())

    hw_caps: Maybe[int] = Property(Integer())

    wifi_caps: Maybe[int] = Property(Integer())

    switch_caps: Maybe[SwitchCaps] = Property(SwitchCaps)

    has_fan: Maybe[bool] = Property(Boolean())

    has_temperature: Maybe[bool] = Property(Boolean())

    temperatures: Maybe[List[TemperaturesItem]] = Property(Array(TemperaturesItem))

    storage: Maybe[List[StorageItem]] = Property(Array(StorageItem))

    ruleset_interfaces: Maybe[RulesetInterfaces] = Property(RulesetInterfaces)

    country_code: Maybe[int] = Property(Integer())

    countrycode_table: Maybe[List[Any]] = Property(Array(Element()))

    connected_at: Maybe[int] = Property(Integer())

    provisioned_at: Maybe[int] = Property(Integer())

    setup_provision_completed: Maybe[bool] = Property(Boolean())

    setup_provision_tracking: Maybe[bool] = Property(Boolean())

    unifi_care: Maybe[UnifiCare] = Property(UnifiCare)

    unsupported: Maybe[bool] = Property(Boolean())

    unsupported_reason: Maybe[int] = Property(Integer())

    wlangroup_id_na: Maybe[str] = Property(String())

    wlangroup_id_ng: Maybe[str] = Property(String())

    bandsteering_mode: Maybe[str] = Property(String())

    atf_enabled: Maybe[bool] = Property(Boolean())

    two_phase_adopt: Maybe[bool] = Property(Boolean())

    serial: Maybe[str] = Property(String())

    hash_id: Maybe[str] = Property(String())

    anon_id: Maybe[str] = Property(String())

    device_id: Maybe[str] = Property(String())

    state: Maybe[int] = Property(Integer())

    start_disconnected_millis: Maybe[int] = Property(Integer())

    x_inform_authkey: Maybe[str] = Property(String())

    last_seen: Maybe[int] = Property(Integer())

    upgradable: Maybe[bool] = Property(Boolean())

    adoptable_when_upgraded: Maybe[bool] = Property(Boolean())

    rollupgrade: Maybe[bool] = Property(Boolean())

    known_cfgversion: Maybe[str] = Property(String())

    uptime: Maybe[int] = Property(Integer())

    _uptime: Maybe[int] = Property(Integer())

    locating: Maybe[bool] = Property(Boolean())

    start_connected_millis: Maybe[int] = Property(Integer())

    sys_stats: Maybe[SysStats] = Property(SysStats)

    system_stats: Maybe[SystemStats] = Property(SystemStats, source='system-stats')

    lldp_table: Maybe[List[LldpTableItem]] = Property(Array(LldpTableItem))

    guest_kicks: Maybe[int] = Property(Integer())

    guest_token: Maybe[str] = Property(String())

    scanning: Maybe[bool] = Property(Boolean())

    spectrum_scanning: Maybe[bool] = Property(Boolean())

    meshv3_peer_mac: Maybe[str] = Property(String())

    element_peer_mac: Maybe[str] = Property(String())

    satisfaction: Maybe[int] = Property(Integer())

    uptime_stats: Maybe[UptimeStats] = Property(UptimeStats)

    overheating: Maybe[bool] = Property(Boolean())

    geo_info: Maybe[GeoInfo] = Property(GeoInfo)

    led_state: Maybe[LedState] = Property(LedState)

    isolated: Maybe[bool] = Property(Boolean())

    radio_table_stats: Maybe[List[RadioTableStatsItem]] = Property(Array(RadioTableStatsItem))

    speedtest_status: Maybe[SpeedtestStatus] = Property(SpeedtestStatus, source='speedtest-status')

    speedtest_status_saved: Maybe[bool] = Property(Boolean(), source='speedtest-status-saved')

    wan1: Maybe[Wan1] = Property(Wan1)

    uplink: Maybe[Uplink] = Property(Uplink)

    vap_table: Maybe[List[VapTableItem]] = Property(Array(VapTableItem))

    ap_downlink_table: Maybe[List[Any]] = Property(Array(Element()))

    vwire_vap_table: Maybe[List[VwireVapTableItem]] = Property(Array(VwireVapTableItem))

    bytes_d: Maybe[int] = Property(Integer(), source='bytes-d')

    tx_bytes_d: Maybe[int] = Property(Integer(), source='tx_bytes-d')

    rx_bytes_d: Maybe[int] = Property(Integer(), source='rx_bytes-d')

    bytes_r: Maybe[int] = Property(Integer(), source='bytes-r')

    downlink_table: Maybe[List[Any]] = Property(Array(Element()))

    network_table: Maybe[List[NetworkTableItem]] = Property(Array(NetworkTableItem))

    connect_request_ip: Maybe[str] = Property(String())

    connect_request_port: Maybe[str] = Property(String())

    prev_non_busy_state: Maybe[int] = Property(Integer())

    next_interval: Maybe[int] = Property(Integer())

    next_heartbeat_at: Maybe[int] = Property(Integer())

    considered_lost_at: Maybe[int] = Property(Integer())

    stat: Maybe[Stat] = Property(Stat)

    tx_bytes: Maybe[int] = Property(Integer())

    rx_bytes: Maybe[int] = Property(Integer())

    bytes: Maybe[int] = Property(Integer())

    vwireEnabled: Maybe[bool] = Property(Boolean())

    uplink_table: Maybe[List[Any]] = Property(Array(Element()))

    num_sta: Maybe[int] = Property(Integer())

    wlan_num_sta: Maybe[int] = Property(Integer(), source='wlan-num_sta')

    lan_num_sta: Maybe[int] = Property(Integer(), source='lan-num_sta')

    user_wlan_num_sta: Maybe[int] = Property(Integer(), source='user-wlan-num_sta')

    user_lan_num_sta: Maybe[int] = Property(Integer(), source='user-lan-num_sta')

    user_num_sta: Maybe[int] = Property(Integer(), source='user-num_sta')

    guest_wlan_num_sta: Maybe[int] = Property(Integer(), source='guest-wlan-num_sta')

    guest_lan_num_sta: Maybe[int] = Property(Integer(), source='guest-lan-num_sta')

    guest_num_sta: Maybe[int] = Property(Integer(), source='guest-num_sta')

    num_desktop: Maybe[int] = Property(Integer())

    num_mobile: Maybe[int] = Property(Integer())

    num_handheld: Maybe[int] = Property(Integer())

    x_has_ssh_hostkey: Maybe[bool] = Property(Boolean())


class Device(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
