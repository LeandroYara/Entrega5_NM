
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    reservas: typing.List[Solicitud] = strawberry.field(resolver=obtener_solicitudes)