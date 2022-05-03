from aiohttp import web
import config


from models import db
from views import CharacterView

app = web.Application()


async def check_health(request):
    return web.json_response({'status': 'OK'})


async def test_request(request: web.Request):
    json_data = await request.json()
    return web.json_response({
        'headers': dict(request.headers),
        'json': json_data,
        'qs': dict(request.query),
    })


app.add_routes([
    web.get('/check_health', check_health),
    web.get('/character/{id:\d+}', CharacterView),
    web.post('/character', CharacterView),
    web.post('/test', test_request),
    web.delete('/character/{id:\d+}', CharacterView)
])


async def init_orm(app):
    await db.set_bind(config.PG_DSN)
    await db.gino.create_all()
    yield
    await db.pop_bind().close()


app.cleanup_ctx.append(init_orm)
web.run_app(app)


async def get_app():
    return app
