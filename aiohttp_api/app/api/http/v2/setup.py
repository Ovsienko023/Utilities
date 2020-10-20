from aiohttp import web

from app.core.constants.database import APP_DB_MANAGER
from .routes import setup_routes


def setup(app: web.Application) -> None:
    subapp = web.Application()

    subapp[APP_DB_MANAGER] = app[APP_DB_MANAGER]

    setup_routes(subapp)

    app.add_subapp('/api/v2/', subapp)
