#python client
import asyncio
from email import message
import websockets
from time import sleep 
async def hello(l):
    async with websockets.connect("wss://31ok2x42e4.execute-api.ap-northeast-1.amazonaws.com/production") as websocket:
        print("connected")
        """a="person not detected"
        if(t=="true"):
          a="person detected"
        # else:
        """ 
        # m=""   
        if(l=="for_esp"):
          if(await websocket.recv()=="on_the_cam"):
            await On_webcam()
        else:
          a=str(l)
          s='{"action": "sendmessage", "message":'+'"' + a + '"' +' }'
          await websocket.send(s)
          print("sent")
 
        # print(await websocket.recv())
