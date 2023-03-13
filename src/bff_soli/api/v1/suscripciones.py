import asyncio
import strawberry
from strawberry.types import Info

from .auth import authenticate_token
from .esquemas import *

@strawberry.type
class Suscripcion:
    @strawberry.subscription
    async def eventos_solicitud(self, info: Info, id_correlacion: str) -> Solicitud:
        connection_params: dict = info.context.get("connection_params")
        token: str = connection_params.get("authToken") 
        if not authenticate_token(token):
            raise Exception("Forbidden!")
        for i in range(id_correlacion):
            yield i
            await asyncio.sleep(0.5)
        ...
