import aiohttp_jinja2
import jinja2
import pytest
from aiohttp import web

from server.handlers import jokes_getter
from server.routes import router


def test_link():
    assert jokes_getter.get_html('https://pun.me/pages/funny-jokes.php') is not None
    assert jokes_getter.get_html('https://vk.com/@techrocks-top-50-shutok-programmistov-o-sebe') is not None


@pytest.fixture
def cli(loop, aiohttp_client, aiohttp_unused_port):
    port = aiohttp_unused_port()
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    router.assign_routes(app)
    return loop.run_until_complete(aiohttp_client(app, server_kwargs={'port': port}))


@pytest.mark.asyncio
async def test_predict_invalid_method(cli):
    resp = await cli.get('/get-joke')
    assert resp.status == 405
