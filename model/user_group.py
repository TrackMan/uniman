from typing import List

from statham.schema.constants import Maybe
from statham.schema.elements import Array, Boolean, Integer, Object, String
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class DataItem(Object):

    _id: Maybe[str] = Property(String())

    site_id: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    attr_hidden_id: Maybe[str] = Property(String())

    attr_no_delete: Maybe[bool] = Property(Boolean())

    qos_rate_max_up: Maybe[int] = Property(Integer())

    qos_rate_max_down: Maybe[int] = Property(Integer())


class UserGroup(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))
