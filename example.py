import powerschoollearning
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

client = powerschoollearning.ps("<my refresh token>", "lakesideblended.learning.powerschool.com")


async def main():
    await client.login()
    for school_class in client.classes:
        print(f"Found class {school_class.name} at https://{client.url_base}{school_class.url}.")
    # for i in range(len(client.classes)):
    #     assignments = await client.fetch_assignments(client.classes[i])
    #     for assignment in assignments:
    #         print(f"{assignment.name} was{' ' if assignment.handed_in else ' not '}turned in. The url for this assignment is at https://{client.url_base}{assignment.url}")
    history_grades = await client.get_grades(client.classes[0])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
