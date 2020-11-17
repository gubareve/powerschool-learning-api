import powerschoollearning
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

client = powerschoollearning.ps(
    "<my refresh token>", "lakesideblended.learning.powerschool.com"
)


async def main():
    await client.login()
    for school_class in client.classes:
        print(f'Found class {school_class.name} at {school_class.url}.')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
