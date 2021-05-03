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


class Extras(Object):

    pass


class GroupsItem(Object):

    unique_id: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    up_id: str = Property(String(), required=True)

    up_ids: List[Any] = Property(Array(Element()), required=True)

    system_name: str = Property(String(), required=True)

    create_time: str = Property(String(), required=True)


class RolesItem(Object):

    unique_id: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    system_role: bool = Property(Boolean(), required=True)

    system_key: str = Property(String(), required=True)

    level: int = Property(Integer(), required=True)


class Permissions(Object):

    access_full_stop_management: List[str] = Property(Array(String()), required=True, source='access.management')

    connect_full_stop_management: List[str] = Property(Array(String()), required=True, source='connect.management')

    led_full_stop_management: List[str] = Property(Array(String()), required=True, source='led.management')

    network_full_stop_management: List[str] = Property(Array(String()), required=True, source='network.management')

    protect_full_stop_management: List[str] = Property(Array(String()), required=True, source='protect.management')

    system_full_stop_management_full_stop_location: List[str] = Property(Array(String()), required=True, source='system.management.location')

    system_full_stop_management_full_stop_user: List[str] = Property(Array(String()), required=True, source='system.management.user')

    talk_full_stop_management: List[str] = Property(Array(String()), required=True, source='talk.management')


class Login(Object):

    unique_id: Maybe[str] = Property(String())

    first_name: Maybe[str] = Property(String())

    last_name: Maybe[str] = Property(String())

    full_name: Maybe[str] = Property(String())

    email: Maybe[str] = Property(String())

    email_status: Maybe[str] = Property(String())

    phone: Maybe[str] = Property(String())

    avatar_relative_path: Maybe[str] = Property(String())

    avatar_rpath2: Maybe[str] = Property(String())

    status: Maybe[str] = Property(String())

    employee_number: Maybe[str] = Property(String())

    create_time: Maybe[int] = Property(Integer())

    extras: Maybe[Extras] = Property(Extras)

    username: Maybe[str] = Property(String())

    local_account_exist: Maybe[bool] = Property(Boolean())

    password_revision: Maybe[int] = Property(Integer())

    sso_account: Maybe[str] = Property(String())

    sso_uuid: Maybe[str] = Property(String())

    sso_username: Maybe[str] = Property(String())

    sso_picture: Maybe[str] = Property(String())

    uid_sso_id: Maybe[str] = Property(String())

    uid_sso_account: Maybe[str] = Property(String())

    groups: Maybe[List[GroupsItem]] = Property(Array(GroupsItem))

    roles: Maybe[List[RolesItem]] = Property(Array(RolesItem))

    permissions: Maybe[Permissions] = Property(Permissions)

    scopes: Maybe[List[str]] = Property(Array(String()))

    cloud_access_granted: Maybe[bool] = Property(Boolean())

    update_time: Maybe[int] = Property(Integer())

    avatar: Maybe[str] = Property(String())

    nfc_token: Maybe[str] = Property(String())

    nfc_display_id: Maybe[str] = Property(String())

    nfc_card_type: Maybe[str] = Property(String())

    nfc_card_status: Maybe[str] = Property(String())

    id: Maybe[str] = Property(String())

    isOwner: Maybe[bool] = Property(Boolean())

    isSuperAdmin: Maybe[bool] = Property(Boolean())

    data: Maybe[Any] = Property(Element(items=Element(required=[])))
