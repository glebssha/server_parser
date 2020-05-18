from aiohttp import web

from server.handlers import jokes_handler
from server.handlers import root


def assign_routes(app) -> None:
    app.router.add_routes([
        web.post('/get-joke', jokes_handler.handle),
        web.get('/', root.handle)
    ])
    app.add_routes([web.static('/static', "server/static")])
