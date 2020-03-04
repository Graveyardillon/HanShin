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
IMAGE_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT
logging.info(" IMAGE SIZE: " + str(IMAGE_SIZE))

if __name__ == '__main__':
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    logging.info(" Binding port on: " + SERVER_IP + ":" + str(SERVER_PORT))

    while True:
      data, addr = s.recvfrom(IMAGE_SIZE)
      print(addr, int.from_bytes(data, 'big'))