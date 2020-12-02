# Powerschool Learning API

This is a simple asynchronous api for interfacing with powerschool learning.

# Installation

`pip install powerschoollearning` Works best.

# Example

```py
import powerschoollearning
import asyncio
import logging
logging.basicConfig(level=logging.INFO)
client = powerschoollearning.ps("<my refresh token>", "lakesideblended.learning.powerschool.com")

async def main():
    await client.login()
    for school_class in client.classes:
        print(f'Found class {school_class.name} at {school_class.url}.')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

This program will take a look at the user's classes and print every classes name and url.

## Refresh Tokens

Since logging into powerschool is handled via oauth, we use refresh tokens to authenticate the user, to get your refresh token push look in the network -> cookies tab of the development tab of a browser while you load powersscool.

## Not finished.

This very much is not finished, and does not support a lot of stuff. This is a work in process.
