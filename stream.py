import socket
import configparser
import logging
import time
import cv2
import numpy as np

logging.basicConfig(level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('./connection.ini', 'UTF-8')

# Connection Settings
SERVER_IP = config.get('server', 'ip')
SERVER_PORT = int(config.get('server', 'port'))

# Image Settings
IMAGE_WIDTH = int(config.get('packet', 'image_width'))
IMAGE_HEIGHT = int(config.get('packet', 'image_height'))
IMAGE_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT
logging.info(" IMAGE SIZE: " + str(IMAGE_SIZE))

# Get a VideoCapture object
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if __name__ == '__main__':
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
      # 'frame' gets image frame
      (ret, frame) = capture.read()
      
      for i in frame:
        for j in i:
          for k in j:
            print(k)

      time.sleep(1)

    # i = 0
    # while True:
    #   s.sendto(i.to_bytes(IMAGE_SIZE, 'big'), (SERVER_IP, SERVER_PORT))
    #   logging.info(" Sent: " + str(i))
    #   time.sleep(1)
    #   i = i + 1