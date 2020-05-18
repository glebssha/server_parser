from aiohttp_jinja2 import template
import typing as tp
from aiohttp import web
from random import randint
from server.handlers import jokes_getter
from enum import Enum


class Language(Enum):
    ENG = 1
    RUS = 2


j = jokes_getter.JokeGetter()


@template('index.html')
async def handle(request: web.Request) -> tp.Dict[str, str]:
    request.app.logger.info(f'got request')
    data = await request.post()
    data = int(data['code'])
    if data == Language.ENG.value:
        result = j.jokes_list_eng[randint(0, 49)]
    else:
        result = j.jokes_list_rus[randint(0, 49)]
    return {'result': result}
