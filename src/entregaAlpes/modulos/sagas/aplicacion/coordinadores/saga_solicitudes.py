from entregaAlpes.modulos.envios.infraestructura.fabricas import FabricaRepositorio
from entregaAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from entregaAlpes.seedwork.dominio.eventos import EventoDominio

from entregaAlpes.modulos.solicitudes.aplicacion.comandos.pagar_solicitud import PagarSolicitud
from entregaAlpes.modulos.solicitudes.aplicacion.comandos.crear_solicitud import CrearSolicitud
from entregaAlpes.modulos.solicitudes.dominio.eventos import SolicitudCreada, SolicitudPagada
from entregaAlpes.modulos.solicitudes.infraestructura.repositorios import RepositorioEventosSolicitudes


class CoordinadorSolicitudes(CoordinadorOrquestacion):

    fabrica_repositorio = FabricaRepositorio()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearSolicitud, evento=SolicitudCreada, error=Exception, compensacion=None),
            Transaccion(index=2, comando=PagarSolicitud, evento=SolicitudPagada, error=Exception, compensacion=None),
            Fin(index=3)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioEventosSolicitudes)
        repositorio.agregar(mensaje)

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es EnvioCreada y el tipo_comando es PagarEnvio
        # Debemos usar los atributos de EnvioCreada para crear el comando PagarEnvio
        print(f"########### PROCESANDO {evento} #############")
        if isinstance(evento, SolicitudCreada) and tipo_comando is PagarSolicitud:
            comando = PagarSolicitud(
                fecha_creacion=evento.fecha_creacion,
                fecha_actualizacion=evento.fecha_actualizacion,
                id=evento.id,
                monto=evento.monto,
                id_cliente=evento.id_cliente,
                id_solicitud=evento.id_solicitud
            )
            return comando



# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(evento):
    if isinstance(evento, EventoDominio):
        coordinador = CoordinadorSolicitudes()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(evento)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")