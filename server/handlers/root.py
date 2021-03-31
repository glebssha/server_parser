from aiohttp_jinja2 import template
import typing as tp
from aiohttp import web


@template('index.html')
async def handle(request: web.Request) -> tp.Dict[str, str]:
    version = request.app['config'].get('version')
    return {'version': version}
