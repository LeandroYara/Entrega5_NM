# Entrega 4 

## Estructura del proyecto

El servicio de manejo de bodegas se encuentra en el módulo **bodegas**, junto a la respectiva implementación de este.
El microservicio de manejo de solicitudes entrantes se encuentra en el módulo “solicitudes”. Este cuenta con fábricas, dtos, eventos y comandos para manejar el broker de eventos.


## Escenarios de calidad 

Escenario 1: Interoperabilidad
En este escenario se busca hacer uso de envíos por terceros cuando la flota actual de EDA no puede soportar el volumen de envíos porque es muy alto. Para esto queremos orquestar los eventos de dominio relacionados al gestión de envío de pedidos, este componente será capaz de enrutar los eventos a los microservicios de envío de terceros y manejar las fallas. Se busca versionar los eventos y comandos para sobre todo la integración con terceros.  


Escenario 2: Escalabilidad
En este escenario, se busca administrar la recepción de peticiones para crearlas dentro del microservicio y tener lista la información para comunicarla al servicio de administración de paquetes. Se espera que escale el servicio hasta 350000 peticiones por día mientras el sistema funciona con mayor tráfico por la llegada de clientes externos. Para este escenario se usa una arquitectura de comunicación asíncrona por eventos junto al patrón de event sourcing dentro del broker de eventos para reconstruir operaciones con mayor facilidad.


Escenario 3: Disponibilidad
En este escenario, se busca demostrar que la aplicación es capaz de tener una disponibilidad en un escenario normal del 98% a lo largo del año, dado que se necesitaría tiempo para probar este escenario mediante monitoreos se puede va a generar un tráfico de 10 solicitudes por segundo por 1 h , para probar que el servicio en cuestión si este haciendo su trabajo de forma n

