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


class DataItem(Object):

    timezone: Maybe[str] = Property(String())

    autobackup: Maybe[bool] = Property(Boolean())

    build: Maybe[str] = Property(String())

    version: Maybe[str] = Property(String())

    previous_version: Maybe[str] = Property(String())

    debug_mgmt: Maybe[str] = Property(String())

    debug_system: Maybe[str] = Property(String())

    debug_device: Maybe[str] = Property(String())

    debug_sdn: Maybe[str] = Property(String())

    data_retention_days: Maybe[int] = Property(Integer())

    data_retention_time_in_hours_for_5minutes_scale: Maybe[int] = Property(Integer())

    data_retention_time_in_hours_for_hourly_scale: Maybe[int] = Property(Integer())

    data_retention_time_in_hours_for_daily_scale: Maybe[int] = Property(Integer())

    data_retention_time_in_hours_for_monthly_scale: Maybe[int] = Property(Integer())

    data_retention_time_in_hours_for_others: Maybe[int] = Property(Integer())

    update_available: Maybe[bool] = Property(Boolean())

    update_downloaded: Maybe[bool] = Property(Boolean())

    live_chat: Maybe[str] = Property(String())

    store_enabled: Maybe[str] = Property(String())

    hostname: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    ip_addrs: Maybe[List[str]] = Property(Array(String()))

    inform_port: Maybe[int] = Property(Integer())

    https_port: Maybe[int] = Property(Integer())

    override_inform_host: Maybe[bool] = Property(Boolean())

    image_maps_use_google_engine: Maybe[bool] = Property(Boolean())

    radius_disconnect_running: Maybe[bool] = Property(Boolean())

    facebook_wifi_registered: Maybe[bool] = Property(Boolean())

    sso_app_id: Maybe[str] = Property(String())

    sso_app_sec: Maybe[str] = Property(String())

    uptime: Maybe[int] = Property(Integer())

    anonymous_controller_id: Maybe[str] = Property(String())

    ubnt_device_type: Maybe[str] = Property(String())

    udm_version: Maybe[str] = Property(String())

    unsupported_device_count: Maybe[int] = Property(Integer())

    unsupported_device_list: Maybe[List[Any]] = Property(Array(Element()))

    unifi_go_enabled: Maybe[bool] = Property(Boolean())

    default_site_device_auth_password_alert: Maybe[bool] = Property(Boolean())


class SysInfo(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
