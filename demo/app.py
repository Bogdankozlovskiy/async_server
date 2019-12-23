from aiohttp import web
from .routes import setup_routes
import aiohttp_jinja2
import jinja2
import asyncpgsa

async def create_app(config=None):
	app = web.Application()
	app['config'] = config
	aiohttp_jinja2.setup(app,
		loader=jinja2.PackageLoader('demo', 'templates')
		)
	setup_routes(app)
	app.on_startup.append(on_start)  #callback
	app.on_cleanup.append(on_shudown)#callback
	return app

async def on_start(app):
	config = app['config']
	app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])

async def on_shudown(app):
	await app['db'].close()