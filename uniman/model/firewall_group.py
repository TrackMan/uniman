from typing import List

from statham.schema.constants import Maybe
from statham.schema.elements import Array, Object, String
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class DataItem(Object):

    _id: Maybe[str] = Property(String())

    group_type: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    group_members: Maybe[List[str]] = Property(Array(String()))

    site_id: Maybe[str] = Property(String())


class FirewallGroup(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
