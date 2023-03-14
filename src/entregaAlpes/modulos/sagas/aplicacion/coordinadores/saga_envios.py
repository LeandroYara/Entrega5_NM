from entregaAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.seedwork.dominio.eventos import EventoDominio

# from entregaAlpes.modulos.sagas.aplicacion.comandos.cliente import RegistrarUsuario, ValidarUsuario
# from entregaAlpes.modulos.sagas.aplicacion.comandos.pagos import PagarEnvio, RevertirPago
# from entregaAlpes.modulos.sagas.aplicacion.comandos.gds import ConfirmarEnvio, RevertirConfirmacion
from entregaAlpes.modulos.envios.aplicacion.comandos.crear_envio import CrearEnvio
from entregaAlpes.modulos.envios.aplicacion.comandos.definir_courier import DefinirCourier
from entregaAlpes.modulos.envios.aplicacion.comandos.confirmar_courier import ConfirmarCourier
from entregaAlpes.modulos.envios.dominio.eventos import EnvioCreado, EnvioCourierConfirmada, EnvioCourierDefinido
# from entregaAlpes.modulos.sagas.dominio.eventos.pagos import EnvioPagada, PagoRevertido
# from entregaAlpes.modulos.sagas.dominio.eventos.gds import EnvioGDSConfirmada, ConfirmacionGDSRevertida, ConfirmacionFallida


class CoordinadorEnvios(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearEnvio, evento=EnvioCreado, error=Exception, compensacion=None),
            Transaccion(index=2, comando=DefinirCourier, evento=EnvioCourierDefinido, error=Exception, compensacion=None),
            Transaccion(index=3, comando=ConfirmarCourier, evento=EnvioCourierConfirmada, error=Exception, compensacion=None),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es EnvioCreada y el tipo_comando es PagarEnvio
        # Debemos usar los atributos de EnvioCreada para crear el comando PagarEnvio
        print(f"########### PROCESANDO {evento} #############")
        if isinstance(evento, EnvioCreado) and tipo_comando is DefinirCourier:
            comando = DefinirCourier(
                fecha_creacion=evento.fecha_creacion,
                fecha_actualizacion=evento.fecha_actualizacion,
                id=evento.id,
                facilitaciones=evento.facilitaciones,
                destino=evento.destino
            )  # TODO: pasar valores
            return comando



# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(evento):
    if isinstance(evento, EventoDominio):
        coordinador = CoordinadorEnvios()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(evento)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")