import asyncio

from aiohttp import web

from app.core import cmdline
from app.core import installtools
from app.core import licenses
from app.core import logger
from app.core import xmltools

from app.core.constants.database import APP_DB_MANAGER
from app.core.constants.app import APP_USER_INFO, APP_LOGGER
from app.api.http.v2.setup import setup as setup_api_v2

from app.services.mcudatabase.client import Manager as MCUDatabaseManager
from app.api.http.middlewares import parse_token

from evtproc.evtprocserver import convert_web_api_port_to_evtproc_port
from evtproc.evtprocserver import set_db_client
from evtproc.evtprocserver import start_evtproc_server


async def init_app(config) -> web.Application:
    app = web.Application(middlewares=[parse_token])
    app.on_cleanup.append(close_database)

    app[APP_DB_MANAGER] = MCUDatabaseManager(
        host=config['db']['host'],
        port=config['db']['port'],
        user=config['db']['username'],
        password=config['db']['password'],
        database=config['db']['dbname']
    )
    app[APP_USER_INFO] = {}
    app[APP_LOGGER] = logger.get_logger()

    setup_api_v1(app)
    setup_api_v2(app)
    setup_api_v3(app)

    return app


def main() -> None:
    config = xmltools.get_config()

    licenses.set_first_license_upd(True)
    installtools.set_installing(False)

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(config))
    lg = app[APP_LOGGER]

    if "--join-evt-proc" in cmd_line_params["params"]:
        if "--evtproc-port" in cmd_line_params["params"]:
            evtproc_port = cmd_line_params["params"]["--evtproc-port"]
        else:
            evtproc_port = convert_web_api_port_to_evtproc_port(config["webapi"]["port"])
        set_db_client(app[APP_DB_MANAGER])
        start_evtproc_server(config["redirector"]["host"], evtproc_port, loop)

    web.run_app(app, host='127.0.0.1', port=config["webapi"]["port"], access_log=lg)


async def close_database(app: web.Application):
    pool: MCUDatabaseManager = app[APP_DB_MANAGER]
    await pool.close()
