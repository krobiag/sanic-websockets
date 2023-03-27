from textwrap import dedent
from sanic import Sanic
from sanic_ext import Extend

from backend.blueprints.car import blueprint as car_blueprint
from backend.blueprints.driver import blueprint as driver_blueprint
from backend.blueprints.garage import blueprint as garage_blueprint
from backend.blueprints.manufacturer import blueprint as manufacturer_blueprint
from backend.blueprints.repair import blueprint as repair_blueprint
from backend.socket import sio


def create_app(app_name: str) -> Sanic:
    # sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins="*")
    app = Sanic(app_name)

    sio.attach(app)

    Extend(app)
    app.ext.openapi.describe(
        "Nettle.ai",
        version="1.1.1",
        description=dedent(
            """
            #This is a sample server Petstore server.
            You can find out more about Swagger at
            [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).
            For this sample, you can use the api key `special-key` to test the authorization filters.
            # Introduction
            This API is documented in **OpenAPI format** and is based on
            [Petstore sample](http://petstore.swagger.io/) provided by [swagger.io](http://swagger.io) team.
            It was **extended** to illustrate features of [generator-openapi-repo](https://github.com/Rebilly/generator-openapi-repo)
            tool and [ReDoc](https://github.com/Redocly/redoc) documentation. In addition to standard
            OpenAPI syntax we use a few [vendor extensions](https://github.com/Redocly/redoc/blob/main/docs/redoc-vendor-extensions.md).
            # OpenAPI Specification
            This API is documented in **OpenAPI format** and is based on
            [Petstore sample](http://petstore.swagger.io/) provided by [swagger.io](http://swagger.io) team.
            It was **extended** to illustrate features of [generator-openapi-repo](https://github.com/Rebilly/generator-openapi-repo)
            tool and [ReDoc](https://github.com/Redocly/redoc) documentation. In addition to standard
            OpenAPI syntax we use a few [vendor extensions](https://github.com/Redocly/redoc/blob/main/docs/redoc-vendor-extensions.md).
            # Cross-Origin Resource Sharing
            This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with  [W3C spec](https://www.w3.org/TR/cors/).
            And that allows cross-domain communication from the browser.
            All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.
            # Authentication
            Petstore offers two forms of authentication:
            - API Key
            - OAuth2
            OAuth2 - an open protocol to allow secure authorization in a simple
            and standard method from web, mobile and desktop applications.
            <!-- ReDoc-Inject: <security-definitions> -->
            """
        ),
    )

    app.blueprint(car_blueprint)
    app.blueprint(driver_blueprint)
    app.blueprint(garage_blueprint)
    app.blueprint(manufacturer_blueprint)
    app.blueprint(repair_blueprint)

    app.config.CORS_ORIGINS = "http://localhost:3000"

    # @sio.event
    # def connect(sid, environ, auth):
    #     print('connect ', sid)

    # @sio.event
    # def disconnect(sid):
    #     print('disconnect ', sid)

    # @sio.event
    # async def received_random_country(sid, data):
    #     print('message from received_random_country', sid, data)

    return app
