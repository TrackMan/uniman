from typing import List

from statham.schema.constants import Maybe
from statham.schema.elements import Array, Boolean, Integer, Object, String
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class DataItem(Object):

    _id: Maybe[str] = Property(String())

    ruleset: Maybe[str] = Property(String())

    rule_index: Maybe[int] = Property(Integer())

    name: Maybe[str] = Property(String())

    enabled: Maybe[bool] = Property(Boolean())

    action: Maybe[str] = Property(String())

    protocol_match_excepted: Maybe[bool] = Property(Boolean())

    logging: Maybe[bool] = Property(Boolean())

    state_new: Maybe[bool] = Property(Boolean())

    state_established: Maybe[bool] = Property(Boolean())

    state_invalid: Maybe[bool] = Property(Boolean())

    state_related: Maybe[bool] = Property(Boolean())

    ipsec: Maybe[str] = Property(String())

    src_firewallgroup_ids: Maybe[List[str]] = Property(Array(String()))

    src_mac_address: Maybe[str] = Property(String())

    dst_firewallgroup_ids: Maybe[List[str]] = Property(Array(String()))

    dst_address: Maybe[str] = Property(String())

    src_address: Maybe[str] = Property(String())

    protocol: Maybe[str] = Property(String())

    icmp_typename: Maybe[str] = Property(String())

    src_networkconf_id: Maybe[str] = Property(String())

    src_networkconf_type: Maybe[str] = Property(String())

    dst_networkconf_id: Maybe[str] = Property(String())

    dst_networkconf_type: Maybe[str] = Property(String())

    site_id: Maybe[str] = Property(String())


class FirewallRule(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
