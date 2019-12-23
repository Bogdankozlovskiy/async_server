from sqlalchemy import select
import aiohttp
from aiohttp_jinja2 import template
import logging
from sqlalchemy.sql import text
from .. import model


@template('index.html')
async def index(request):
	logging.info('client load a page')
	site_name = request.app['config'].get('site_name')
	return {'site_name':site_name}
	return aiohttp.web.Response(text='OK')

async def post(request):
	async with request.app['db'].acquire() as conn:
		query = select([model.post])
		result = await conn.fetch(query)
	return aiohttp.web.Response(body = str(result))