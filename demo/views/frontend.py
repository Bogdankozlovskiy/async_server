import aiohttp
from aiohttp_jinja2 import template
import logging


@template('index.html')
async def index(request):
	logging.info('client load a page')
	return {}
	return aiohttp.web.Response(text='OK')