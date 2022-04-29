import asyncio
import websockets
import json
import time
from pygame import mixer


async def handler(websocket):
	while True:
		message = await websocket.recv()
		parsed_msg = json.loads(message)
		print(parsed_msg["msg"])
		if(parsed_msg["msg"] == "PLAY"):
			mixer.init()
			mixer.music.load("audio-file.mp3")
			mixer.music.play()

async def main():
	async with websockets.connect("ws://my-web-socket-server.com") as websocket:
		await handler(websocket)

try:
	asyncio.get_event_loop().run_until_complete(main())


except KeyboardInterrupt:
	print(" App closed")
