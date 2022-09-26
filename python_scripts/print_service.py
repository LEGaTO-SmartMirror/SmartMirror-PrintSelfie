#!/usr/bin/python
# coding: utf8
import os, sys, datetime, time
import json, cv2
import numpy as np

BASE_DIR = os.path.dirname(__file__) + '/'
os.chdir(BASE_DIR)

def to_node(type, message):
  # convert to json and print (node helper will read from stdout)
  try:
    print(json.dumps({type: message}))
  except Exception:
    pass
  # stdout has to be flushed manually to prevent delays in the node helper communication
  sys.stdout.flush()

#print_source = sys.argv[1]
waiting_time = 2;

#to_node("status", "printing from source: " + print_source)

to_node("say_message", "Taking a selfie on the count of 3!!")
video_cap = cv2.VideoCapture()
video_cap.open("shmsrc socket-path=/dev/shm/center_display ! video/x-raw, format=BGR ,height=1920, width=1080, framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink drop=true", cv2.CAP_GSTREAMER)
time.sleep(waiting_time);

to_node("say_message", "3")
# logo size 155x582
ved_logo = cv2.imread('logos/Vedliot_small_vert.png',cv2.IMREAD_COLOR)
time.sleep(waiting_time);

to_node("say_message", "2")
time.sleep(waiting_time);

to_node("say_message", "1")
time.sleep(waiting_time);

to_node("say_message", "CLICK")

filename = str(datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")) + ".jpg"



#if(print_source == "DETECTIONS"):

#else:
#  video_cap.open("shmsrc socket-path=/dev/shm/style_transfer ! video/x-raw, format=BGR, height=1920, width=1080, framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink drop=true", cv2.CAP_GSTREAMER)
 
ret, image = video_cap.read()
# needed image size 1620x1080 (3:2)
crop_img = image[100:1720, 0:1080]

# logo size 520x100
#cm_logo = cv2.imread('logos/Christmann.jpg',cv2.IMREAD_COLOR)
# logo size 300x225
#legato_logo = cv2.imread('logos/legato.jpg',cv2.IMREAD_COLOR)
# logo size 360x100
#uni_logo = cv2.imread('logos/uni-bielefeld.jpg',cv2.IMREAD_COLOR)

# logo size 1000x309
#ved_logo = cv2.imread('logos/Vedliot.jpg',cv2.IMREAD_COLOR)
# logo size 232x300
#ved_logo = cv2.imread('logos/Vedliot_small.jpg',cv2.IMREAD_COLOR)



#crop_img[20:120,20:540] = cm_logo
#crop_img[20:(20+225) , (1060-300) :1060] = legato_logo
#crop_img[140:240,20:380] = uni_logo
#crop_img[140:240,20:380] = uni_logo

#crop_img[50:359,50:1050] = ved_logo
crop_img[1008:1590,905:1060] = np.where((ved_logo > 0) ,ved_logo,crop_img[1008:1590,905:1060] )
#crop_img[832:1600,812:1030] = ved_logo.notnull()

#time.sleep(1);
cv2.imwrite("taken_selfies/"+filename, crop_img)
os.system("lp \"taken_selfies/" + filename + "\"")
