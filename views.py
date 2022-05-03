from aiohttp import web
from asyncpg import UniqueViolationError

from models import Character, CharacterValidationModel


class CharacterView(web.View):

    async def delete(self):
        character_id = int(self.request.match_info['id'])
        character = await Character.get(character_id)
        if character is None:
            return web.json_response({"error": "not found for delete"}, status=404)
        await character.delete()
        return web.json_response({"deleted": "ok"}, status=200)

    async def get(self):
        character_id = int(self.request.match_info['id'])
        character = await Character.get(character_id)
        if character is None:
            return web.json_response({"error": "not found"}, status=404)
        character_data = character.to_dict()
        return web.json_response(character_data)

    async def post(self):
        json_data = await self.request.json()
        json_data_validated = CharacterValidationModel(**json_data).dict()
        print(json_data_validated)
        try:
            new_character = await Character.create(**json_data_validated)
        except UniqueViolationError:
            return web.json_response({'error': 'Already exist'}, status=400)
        return web.json_response(new_character.to_dict())
