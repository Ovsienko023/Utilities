from app.api.http.middlewares import authorize
from aiohttp import web
from app.core.constants.database import APP_DB_MANAGER
from app.api.http.errors import ErrorContainer
import app.api.native.misc.lang_time as misc
from app.api.native.misc.constants import ERRORS_LANGS_NOT_FOUND


@authorize
async def get_langs(request: web.Request) -> web.Response:
    errors = ErrorContainer()

    res = await misc.get_langs(request.app)

    if not res:
        return errors.done(404, ERRORS_LANGS_NOT_FOUND)

    return web.json_response(res.get_entity())
