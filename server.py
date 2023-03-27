import sys
from sanic import Sanic
from sanic.worker.loader import AppLoader
from functools import partial

from backend import main


def create_app(app_name: str) -> Sanic:
    return main.create_app(app_name)


if __name__ == "__main__":
    app_name = sys.argv[-1] or "Websocket_Application"
    if (".py" in app_name):
        app_name = "Websocket_Application"
    loader = AppLoader(factory=partial(create_app, app_name))
    app = loader.load()
    app.prepare(host='0.0.0.0', port=8000, dev=True)
    Sanic.serve(primary=app, app_loader=loader)
