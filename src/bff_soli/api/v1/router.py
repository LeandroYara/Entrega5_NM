from strawberry.fastapi import GraphQLRouter
from .consultas import Query
from .mutaciones import Mutation
from .suscripciones import Suscripcion

import strawberry


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Suscripcion)
router = GraphQLRouter(schema)