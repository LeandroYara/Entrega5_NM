from aeroalpes.seedwork.aplicacion.handlers import Handler
from aeroalpes.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReservaPayload
from aeroalpes.modulos.vuelos.infraestructura.mapeadores import MapeadorReserva

class HandlerReservaComando(Handler):
    @staticmethod
    def handle_comando_crear_reserva(comando: ComandoCrearReservaPayload):
        """
        Comando viene de la capa de infrastructura, creo que se debe transformar a 
        comando CrearReserva de la capa de aplicacion y luego ejecutarlo
        """
        print('##################### COMANDO ####################')
        mapper = MapeadorReserva()

        itinerarios = []
        for itinerario in comando.itinerarios:
            itinerarios .extend(mapper._procesar_itinerario(itinerario))
        print('##################### COMANDO ####################')
        print(itinerarios)
        print(itinerarios[0].__dict__)
        comando = CrearReserva(
            id="",
            fecha_creacion=comando.time,
            fecha_actualizacion=comando.time,
            itinerarios=itinerarios
        )
        ejecutar_commando(comando)