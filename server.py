import asyncio
import datetime
import random
import websockets


async def time(websocket, path):
    '''
    Send current time to new clients on connection
    '''

    now = datetime.datetime.utcnow().isoformat() + "Z"
    await websocket.send(now)

host = 'localhost'
port = 5789
print(f'Serving requests on {host}:{port}. Press Ctrl+C to exit.')
server = websockets.serve(time, host, port)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
