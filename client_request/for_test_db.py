import asyncio

from client_request.api_models import CharacterAPI


async def main_post_db():
    character_in_db = CharacterAPI()
    print(await character_in_db.get_character(2))
    await character_in_db.close()


if __name__ == '__main__':
    asyncio.run(main_post_db())
