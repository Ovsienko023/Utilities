import app.api.http.v1.handlers.langs_time as misc
from aiohttp import web


def setup_routes(app):
    app.add_routes([
        web.get('/misc/langs', misc.get_langs)
    ])
