import sys
import asyncio
from discord.gateway import Gateway

if __name__ == '__main__':
    # Creating client object
    gateway = Gateway(json=True) if sys.argv[0] == True else Gateway()
    loop = asyncio.get_event_loop()
    # Start connection and get client connection protocol
    connection = loop.run_until_complete(gateway.start(loop))
    # Start listener and heartbeat 
    tasks = [
        asyncio.ensure_future(gateway.heartbeat(connection)),
        asyncio.ensure_future(gateway.listen(connection))
    ]

    loop.run_until_complete(asyncio.wait(tasks))