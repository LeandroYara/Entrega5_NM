from entregaAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.seedwork.dominio.eventos import EventoDominio
from entregaAlpes.modulos.bodega.aplicación.comandos.crear_reserva import CrearOrden
from entregaAlpes.modulos.bodega.dominio.eventos import OrdenCreada
class CoordinadorEnvios(CoordinadorOrquestacion):
    def __init__(self):
        self.inicializar_pasos()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearOrden, evento=OrdenCreada, error=Exception, compensacion=None),
            #Transaccion(index=2, comando=DefinirCourier, evento=EnvioCourierDefinido, error=Exception, compensacion=None),
            #Transaccion(index=3, comando=ConfirmarCourier, evento=EnvioCourierConfirmada, error=Exception, compensacion=None),
            Fin(index=1)
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
        print(evento, tipo_comando)


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorEnvios()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")