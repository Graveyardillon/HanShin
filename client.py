import socket
import configparser
import logging
import time

logging.basicConfig(level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('./connection.ini', 'UTF-8')

# Connection Settings
SERVER_IP = config.get('server', 'ip')
SERVER_PORT = int(config.get('server', 'port'))

# Image Settings
IMAGE_WIDTH = int(config.get('packet', 'image_width'))
IMAGE_HEIGHT = int(config.get('packet', 'image_height'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((SERVER_IP, SERVER_PORT))
  logging.info(" Connected to the server")

  i = 0
  while True:
    logging.info(" " + str(i))
    time.sleep(1)
    i = i + 1