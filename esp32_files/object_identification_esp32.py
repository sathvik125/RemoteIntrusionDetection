import uwebsockets.client
import sys,time
import network
from machine import Pin
from time import sleep
import _thread
import upip

import machine, time
from machine import Timer
import time,json,hcsr04
TIMEOUT_MS = 5000 #soft-reset will happen around 5 sec

def timeout_callback(t):
    try:
        print("I am in Call back")
        #ffwebsocket.send("Ws send \r")
    finally:
        print("I am in Call back finally")
       

def wlan_connect(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    #upip.install("")
    
    
wlan_connect('V2029','202212367')
ultrasonic = hcsr04.HCSR04(trigger_pin=14, echo_pin=12, echo_timeout_us=1000000)

#p0 = Pin(4, Pin.OUT)
uri = "wss://31ok2x42e4.execute-api.ap-northeast-1.amazonaws.com/production"
websocket = uwebsockets.client.connect(uri)
#print(websocket)
while True:
    #print("Enter Command:\r")
    #mesg=input()
    #websocket.send(mesg + "\r")
    print("inloop")
    distance = ultrasonic.distance_cm()
    distance1 = ultrasonic.distance_mm()
    print('Distance:', distance, 'cm', '|', distance1, 'mm')
    if distance<20:

        s='{"action": "sendmessage", "message":'+'"' + "on_the_cam" + '"' +' }'
           
        websocket.send(s)
        timer = Timer(0)
        timer.init(period=TIMEOUT_MS, callback=timeout_callback)
        print("sent")
        break
        
    sleep(1)
    
