import entregaAlpes.seedwork.presentacion.api as api
import json
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO
from entregaAlpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from entregaAlpes.modulos.envios.aplicacion.mapeadores import MapeadorEnvioDTOJson
from entregaAlpes.modulos.envios.aplicacion.comandos.enviar_envio import EnviarEnvio
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('envios', '/envios')

@bp.route('/envio-comando', methods=('POST',))
def enviar_asincrona():
    try:
        envio_dict = request.json

        map_envio = MapeadorEnvioDTOJson()
        envio_dto = map_envio.externo_a_dto(envio_dict)

        comando = EnviarEnvio(
            envio_dto.fecha_creacion, envio_dto.fecha_actualizacion, envio_dto.id,
            envio_dto.facilitaciones, envio_dto.destino)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
