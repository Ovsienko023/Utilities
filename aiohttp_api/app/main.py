import asyncio

from aiohttp import web
from app.core.constants.database import APP_DB_MANAGER
from app.api.http.v2.setup import setup as setup_api_v2
from app.services.mcudatabase.client import Manager as MCUDatabaseManager


async def init_app(config) -> web.Application:
    app = web.Application()
    app.on_cleanup.append(close_database)

    app[APP_DB_MANAGER] = MCUDatabaseManager(
        host=config['db']['host'],
        port=config['db']['port'],
        user=config['db']['username'],
        password=config['db']['password'],
        database=config['db']['dbname']
    )

    setup_api_v2(app)

    return app


async def close_database(app: web.Application):
    pool: MCUDatabaseManager = app[APP_DB_MANAGER]
    await pool.close()
