import asyncio
import more_itertools

from client_request.api_models import CharacterGetFromURL, CharacterAPI


async def filter_none(data_list):
    result = []
    for elem in data_list:
        if elem is None:
            continue
        result.append(elem)
    return result


async def main(dict_for_template):
    person = CharacterGetFromURL()
    new_character_in_db = CharacterAPI()

    for person_id_chunk in more_itertools.chunked(range(1, 100), 10):
        list_of_task = []

        for person_id in person_id_chunk:
            task = asyncio.create_task(person.get_full_data(person_id, dict_for_template))
            list_of_task.append(task)
        result = await asyncio.gather(*list_of_task)
        result_list = await filter_none(result)

        await new_character_in_db.create_from_list(result_list)

    await new_character_in_db.close()
    await person.close()
    return result


if __name__ == '__main__':
    from template import template

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(template))
