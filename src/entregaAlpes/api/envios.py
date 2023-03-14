import entregaAlpes.seedwork.presentacion.api as api
import json
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO
from entregaAlpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from entregaAlpes.modulos.envios.aplicacion.mapeadores import MapeadorEnvioDTOJson
from entregaAlpes.modulos.envios.aplicacion.comandos.crear_envio import CrearEnvio
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando
# from entregaAlpes.modulos.envios.infraestructura.despachadores import Despachador
# from entregaAlpes.modulos.envios.dominio.eventos import EnvioCreado
# from pydispatch import dispatcher


bp = api.crear_blueprint('envios', '/envios')

@bp.route('/envio-comando', methods=('POST',))
def enviar_asincrona():
    try:
        envio_dict = request.json

        map_envio = MapeadorEnvioDTOJson()
        envio_dto = map_envio.externo_a_dto(envio_dict)

        comando = CrearEnvio(
            envio_dto.fecha_creacion, envio_dto.fecha_actualizacion, envio_dto.id,
            envio_dto.facilitaciones, envio_dto.destino, envio_dto.id_pedido)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        # evento = EnvioCreado(envio_dto.id, envio_dto.fecha_creacion, envio_dto.id_pedido,
        # envio_dto.fecha_actualizacion, envio_dto.fecha_creacion, envio_dto.facilitaciones, envio_dto.destino)
        # dispatcher.send(signal=f'{type(evento).__name__}Dominio', mensaje=evento)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
