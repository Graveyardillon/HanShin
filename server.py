import socket
import configparser
import logging

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
  s.bind((SERVER_IP, SERVER_PORT))
  s.listen(1)
  logging.info(" Listening on http://" + SERVER_IP + ":" + str(SERVER_PORT))

  while True:
    (conn, addr) = s.accept()
    with conn:
      while True:
        data = conn.recv(IMAGE_WIDTH * IMAGE_HEIGHT * 3)
        if not data:
          break
        logging.info()