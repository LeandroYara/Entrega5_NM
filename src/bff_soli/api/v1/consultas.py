
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    solicitudes: typing.List[Solicitud] = strawberry.field(resolver=obtener_solicitudes)