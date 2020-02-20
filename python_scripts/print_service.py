#!/usr/bin/python
# coding: utf8
import os, sys, time
import json, cv2

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
time.sleep(waiting_time);
to_node("say_message", "3")
time.sleep(waiting_time);
to_node("say_message", "2")
time.sleep(waiting_time);
to_node("say_message", "1")
time.sleep(waiting_time);
to_node("say_message", "CLICK")

filename = str(time.ctime()) + ".jpg"

video_cap = cv2.VideoCapture()

#if(print_source == "DETECTIONS"):
video_cap.open("shmsrc socket-path=/dev/shm/center_display ! video/x-raw, format=BGR ,height=1920, width=1080, framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink drop=true", cv2.CAP_GSTREAMER)
#else:
#  video_cap.open("shmsrc socket-path=/dev/shm/style_transfer ! video/x-raw, format=BGR, height=1920, width=1080, framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink drop=true", cv2.CAP_GSTREAMER)
 
ret, image = video_cap.read()
# needed image size 1620x1080 (3:2)
crop_img = image[100:1720, 0:1080]

# logo size 520x100
cm_logo = cv2.imread('logos/Christmann.jpg',cv2.IMREAD_COLOR)
# logo size 300x225
legato_logo = cv2.imread('logos/legato.jpg',cv2.IMREAD_COLOR)
# logo size 360x100
uni_logo = cv2.imread('logos/uni-bielefeld.jpg',cv2.IMREAD_COLOR)

crop_img[20:120,20:540] = cm_logo
crop_img[20:(20+225) , (1060-300) :1060] = legato_logo
crop_img[140:240,20:380] = uni_logo
#crop_img[140:240,20:380] = uni_logo


cv2.imwrite("taken_selfies/"+filename, crop_img)

time.sleep(1);
#os.system("lp \"taken_selfies/" + filename + "\"")
