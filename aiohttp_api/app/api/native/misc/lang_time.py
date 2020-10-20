from aiohttp import web
import app.api.native.misc.messages as messages
from app.core.constants.database import APP_DB_MANAGER


async def get_langs(app: web.Application) -> messages.MessageLangList:
    client = app[APP_DB_MANAGER]

    query = "select * from misc.get_langs()"

    #  если нужны params:
    # query = """
    #     select *
    #     from misc.get_langs(
    #         %(usei_id)s
    #     )
    # """
    # params = {
    #     "usei_id": user_id # msg.user_id 
    # }

    records = await client.fetch_all(query)

    langs = messages.MessageLangList(langs=[],
                                     count=len(records))

    for row in records:
        item = messages.MessageLang(
            lang_id=row.get("lang_id"),
            name=row.get("name")
        )
        langs.add(item)

    return langs
