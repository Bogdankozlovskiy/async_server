import aiohttp
import aioreloader
import asyncio
import argparse
from demo import create_app
import logging
logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
try:
	import uvloop
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
	logging.warning('uvloop is not allowed')
else:
	logging.warning('uvloop is loaded successful')

parser = argparse.ArgumentParser(description="Best project")
parser.add_argument(
	'--host',
	help='Host to listen',
	default='0.0.0.0')
parser.add_argument(
	'--port',
	help='Port to accept connections',
	default='8080')
parser.add_argument(
	'--reload', 
	action='store_true',   #не требовать аргумент
	help='Autoreload code on change')
args = parser.parse_args()

def main():
	if args.reload:
		aioreloader.start()
		logging.warning('Autoreload is started')
	app = create_app()
	aiohttp.web.run_app(app, host=args.host, port=args.port)

if __name__ == '__main__':
	main()