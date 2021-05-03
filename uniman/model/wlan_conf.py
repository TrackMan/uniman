from typing import List

from statham.schema.constants import Maybe
from statham.schema.elements import Array, Boolean, Integer, Object, String
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class DataItem(Object):

    _id: Maybe[str] = Property(String())

    enabled: Maybe[bool] = Property(Boolean())

    name: Maybe[str] = Property(String())

    security: Maybe[str] = Property(String())

    wpa_enc: Maybe[str] = Property(String())

    wpa_mode: Maybe[str] = Property(String())

    x_passphrase: Maybe[str] = Property(String())

    site_id: Maybe[str] = Property(String())

    usergroup_id: Maybe[str] = Property(String())

    x_iapp_key: Maybe[str] = Property(String())

    no2ghz_oui: Maybe[bool] = Property(Boolean())

    minrate_ng_enabled: Maybe[bool] = Property(Boolean())

    minrate_ng_beacon_rate_kbps: Maybe[int] = Property(Integer())

    minrate_ng_data_rate_kbps: Maybe[int] = Property(Integer())

    pmf_mode: Maybe[str] = Property(String())

    b_supported: Maybe[bool] = Property(Boolean())

    ap_group_ids: Maybe[List[str]] = Property(Array(String()))

    wlan_band: Maybe[str] = Property(String())

    networkconf_id: Maybe[str] = Property(String())

    iapp_enabled: Maybe[bool] = Property(Boolean())


class WlanConf(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
