from typing import Any, List

from statham.schema.constants import Maybe
from statham.schema.elements import Array, Element, Object, String
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class DhcpOption(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[Any]] = Property(Array(Element(required=[])))
