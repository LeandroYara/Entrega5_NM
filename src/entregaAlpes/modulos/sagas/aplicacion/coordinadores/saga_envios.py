from entregaAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.seedwork.dominio.eventos import EventoDominio

from entregaAlpes.modulos.envios.aplicacion.comandos.crear_envio import CrearEnvio
from entregaAlpes.modulos.envios.aplicacion.comandos.definir_courier import DefinirCourier
from entregaAlpes.modulos.envios.aplicacion.comandos.confirmar_courier import ConfirmarCourier
from entregaAlpes.modulos.envios.aplicacion.comandos.revertir_asignacion_courier import RevertirAsignacionCourier
from entregaAlpes.modulos.envios.aplicacion.comandos.cancelar_envio_courier import CancelarEnvioCourier
from entregaAlpes.modulos.envios.dominio.eventos import (
    EnvioCreado, EnvioCourierConfirmada, EnvioCourierDefinido,
    CreacionEnvioFallido, AsignacionDeCourierFallida, ConfirmacionDeCourierFallida
)
from entregaAlpes.modulos.envios.infraestructura.fabricas import FabricaRepositorio
from entregaAlpes.modulos.envios.infraestructura.repositorios import RepositorioEventosEnvios


class CoordinadorEnvios(CoordinadorOrquestacion):

    fabrica_repositorio = FabricaRepositorio()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearEnvio, evento=EnvioCreado, error=CreacionEnvioFallido, compensacion=None),
            Transaccion(index=2, comando=DefinirCourier, evento=EnvioCourierDefinido, error=AsignacionDeCourierFallida, compensacion=RevertirAsignacionCourier),
            Transaccion(index=3, comando=ConfirmarCourier, evento=EnvioCourierConfirmada, error=ConfirmacionDeCourierFallida, compensacion=CancelarEnvioCourier),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self, evento):
        print("############### TERMINANDO SAGA DE ENVIOS CON EXITO ####################")
        print(evento)
        self.persistir_en_saga_log(evento)

    def persistir_en_saga_log(self, mensaje):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioEventosEnvios)
        repositorio.agregar(mensaje)

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        print(f"########### PROCESANDO {evento} ############# CON COMANDO ######################## {tipo_comando}")
        self.persistir_en_saga_log(evento)
        if isinstance(evento, EnvioCreado) and tipo_comando is DefinirCourier:
            comando = DefinirCourier(
                fecha_creacion=evento.fecha_creacion,
                fecha_actualizacion=evento.fecha_actualizacion,
                id=evento.id,
                facilitaciones=evento.facilitaciones,
                destino=evento.destino,
                id_pedido=evento.id_pedido
            )
            return comando
        if isinstance(evento, EnvioCourierDefinido) and tipo_comando is ConfirmarCourier:
            comando = ConfirmarCourier(
                id=evento.id,
                facilitaciones=evento.facilitaciones,
                destino=evento.destino,
                id_pedido=evento.id_pedido,
                courier=evento.courier
            )
            return comando
        if isinstance(evento, EnvioCourierConfirmada):
            comando = ConfirmarCourier(
                id=evento.id,
                id_pedido=evento.id_pedido,
                courier=evento.courier
            )
            return comando
        if isinstance(evento, ConfirmacionDeCourierFallida) and tipo_comando is CancelarEnvioCourier:
            comando = CancelarEnvioCourier(
                id=evento.id,
                id_pedido=evento.id_pedido,
                courier=evento.courier
            )
            return comando
        if isinstance(evento, AsignacionDeCourierFallida) and tipo_comando is RevertirAsignacionCourier:
            comando = RevertirAsignacionCourier(
                id=evento.id,
                id_pedido=evento.id_pedido,
                courier=evento.courier
            )
            return comando


# Listener/Handler para que se puedan redireccionar eventos de dominio agregado en
# __init__.py file del modulo de Sagas
def oir_mensaje(evento):
    if isinstance(evento, EventoDominio):
        coordinador = CoordinadorEnvios()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(evento)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")