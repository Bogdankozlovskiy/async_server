import aiohttp
from aiohttp_jinja2 import template
import logging


@template('index.html')
async def index(request):
	logging.info('client load a page')
	site_name = request.app['config'].get('site_name')
	return {'site_name':site_name}
	return aiohttp.web.Response(text='OK')