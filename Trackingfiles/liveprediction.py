# import cv2
# import time

# CONFIDENCE_THRESHOLD = 0.2
# NMS_THRESHOLD = 0.4
# COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# class_names = []
# with open("classes.txt", "r") as f:
#     class_names = [cname.strip() for cname in f.readlines()]

# import asyncio
# from email import message
# import websockets
# from time import sleep 
# print("waiting.....")
# async def hello(l):
#     async with websockets.connect("wss://mgo6mb343m.execute-api.ap-northeast-1.amazonaws.com/production") as websocket:
#         print("connected") 
#         if(l=="for_esp"):
#           if(l=="for_esp"):
#             await On_webcam()
            
#         else:
#           a=str(l)
#           s='{"action": "sendmessage", "message":'+'"' + a + '"' +' }'
#           await websocket.send(s)
#           print("sent")




# async def On_webcam():
#     vc = cv2.VideoCapture(0)

#     net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
#     net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#     net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
#     pres=-1
#     prev=-1
#     model = cv2.dnn_DetectionModel(net)
#     model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
#     w=-1
#     h=-1
#     cx=-1
#     cy=-1
#     while cv2.waitKey(1) < 1:
#         # print("yes")
#         (grabbed, frame) = vc.read()
#         if not grabbed:
#             exit()

#         start = time.time()
#         classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
#         # print(classes,"yes")
#         end = time.time()

#         start_drawing = time.time()

#         for (classid, score, box) in zip(classes, scores, boxes):
#             if(classid==0):
#                 print(box)
#                 left, top, right, bottom =box[0],box[1],box[2],box[3]
#                 w = int(right - left)
#                 h = int(bottom - top)
#                 cx = int(top + h/2)
#                 cy = int(left + w/2)
#                 # pres
#                 print(cx, cy)
#                 print(left)
#                 if(pres==-1):
#                     pres=left
#                 else:
#                     prev=pres
#                     pres=left
#                 #     await hello(str(pres-prev))
#                 color = COLORS[int(classid) % len(COLORS)]
#                 label = "%s : %f" % (class_names[classid], score)

#                 cv2.rectangle(frame, box, color, 2)
#                 cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
#         await hello(str(pres-prev))
#         end_drawing = time.time()
        
#         fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
#         cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#         cv2.imshow("detections", frame)
# asyncio.run(hello("for_esp"))
import cv2
import time

CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

import asyncio
from email import message
import websockets
from time import sleep 
print("waiting.....")
async def hello(l):
    async with websockets.connect("wss://31ok2x42e4.execute-api.ap-northeast-1.amazonaws.com/production") as websocket:
        print("connected") 
        if(l=="for_esp"):
            if(await websocket.recv()=="on_the_cam"):
                print("webcam_turned_on")
                vc = cv2.VideoCapture(0)

                net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
                net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
                net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
                pres=-1
                prev=-1
                model = cv2.dnn_DetectionModel(net)
                model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
                while cv2.waitKey(1) < 1:
                    # print("yes")
                    (grabbed, frame) = vc.read()
                    if not grabbed:
                        exit()

                    start = time.time()
                    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
                    # print(classes,"yes")
                    end = time.time()

                    start_drawing = time.time()
                    for (classid, score, box) in zip(classes, scores, boxes):
                        if(classid==0):
                            print(box)
                            left, top, right, bottom =box[0],box[1],box[2],box[3]
                            w = int(right - left)
                            h = int(bottom - top)
                            cx = int(top + h/2)
                            cy = int(left + w/2)
                            
                            print(cx, cy)
                            if(pres==-1):
                                pres=left
                            else:
                                prev=pres
                                pres=left
                                s='{"action": "sendmessage", "message":'+'"' + str((prev-pres)*100) + '"' +' }'
                                
                                # sleep(0.5)
                            
                            color = COLORS[int(classid) % len(COLORS)]
                            label = "%s : %f" % (class_names[classid], score)

                            cv2.rectangle(frame, box, color, 2)
                            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    await hello(str((pres-prev)))
                    end_drawing = time.time()
                    
                    fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
                    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                    cv2.imshow("detections", frame)
            
            
        else:
          a=str(l)
          s='{"action": "sendmessage", "message":'+'"' + a + '"' +' }'
          await websocket.send(s)
          print("sent")




# async def On_webcam():
#     vc = cv2.VideoCapture(0)

#     net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
#     net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#     net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
#     pres=-1
#     prev=-1
#     model = cv2.dnn_DetectionModel(net)
#     model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
#     while cv2.waitKey(1) < 1:
#         # print("yes")
#         (grabbed, frame) = vc.read()
#         if not grabbed:
#             exit()

#         start = time.time()
#         classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
#         # print(classes,"yes")
#         end = time.time()

#         start_drawing = time.time()
#         for (classid, score, box) in zip(classes, scores, boxes):
#             if(classid==0):
#                 print(box)
#                 left, top, right, bottom =box[0],box[1],box[2],box[3]
#                 w = int(right - left)
#                 h = int(bottom - top)
#                 cx = int(top + h/2)
#                 cy = int(left + w/2)
                
#                 print(cx, cy)
#                 if(pres==-1):
#                     pres=cx
#                 else:
#                     prev=pres
#                     pres=cx
#                 await hello(str(pres-prev))
#                 color = COLORS[int(classid) % len(COLORS)]
#                 label = "%s : %f" % (class_names[classid], score)

#                 cv2.rectangle(frame, box, color, 2)
#                 cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
#         end_drawing = time.time()
        
#         fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
#         cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#         cv2.imshow("detections", frame)
asyncio.run(hello("for_esp"))