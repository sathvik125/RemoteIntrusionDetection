import asyncio
from email import message
from time import sleep
import websockets

import vlc
from time import sleep 
import multiprocessing
from playsound import playsound

async def hello():
    async with websockets.connect("wss://31ok2x42e4.execute-api.ap-northeast-1.amazonaws.com/production") as websocket:


        print("connected")
        # while(1):
        #     # print()
        #     msg1=await websocket.recv()
        #     if(msg1=="turnedOn"):
        #         playsound('Music12.mp3')
        #         print("true")
        while(1):
            print(await websocket.recv())

        # print("enter input:")
        # a=str(input())
        # i=0
        # while(1):
        #     print("waiting")
        #     print(await websocket.recv())

            # a="on_the_cam"+str(i)
            # i+=1
            # s='{"action": "sendmessage", "message":'+'"' + a + '"' +' }'
            # await websocket.send(s)
            # i+=1
            # print("sent")
            # playsound.playsound('BGM.mp3', True)
        # print(await websocket.recv())

        # while(1):
        #     # print()
        #     if(await websocket.recv()=="turnedOn"):
        #         playsound('Music12.mp3')
        #         print("true")
        #         break
  
asyncio.run(hello())