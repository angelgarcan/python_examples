import asyncio
import datetime
from time import sleep
import websockets


async def test():
    while True:
        async with websockets.connect('ws://localhost:8000') as websocket:
            data = f"{datetime.datetime.now().strftime('%d-%b-%Y (%H:%M:%S)')} - Py Client!!"
            print(f"Sending: {data}")
            await websocket.send(data)
            response = await websocket.recv()
            print(response)
        sleep(1)

asyncio.get_event_loop().run_until_complete(test())
# asyncio.get_event_loop().run_forever()


# https://stackoverflow.com/questions/65083428/python-websockets-how-to-do-a-simple-synchronous-send-command
# from websocket import create_connection
# from contextlib import closing

# def wsSend(uri,msg):
#     ws=create_connection(uri)
#     ws.send(json.dumps({"msg":msg}))
#     ws.close()

# def send_event_info(event_path):
#     with closing(create_connection(GUEST_WS_URI)) as ws:
#         ws.send(event_path)

# https://pypi.org/project/websocket-client/
