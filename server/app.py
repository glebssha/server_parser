import jinja2
from aiohttp import web
from server.routes import router
import aiohttp_jinja2
import typing as tp


async def create_app(config: tp.Dict[str, str]):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('server', 'templates')
    )
    router.assign_routes(app)
    return app
