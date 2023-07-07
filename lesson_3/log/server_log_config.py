import logging
import os

__directory = '/home/sunset/Рабочий стол/временная папка/lesson_3/log_file/'
__formater = logging.Formatter('%(asctime)-10s %(levelname)-6s %(message)-5s')
__handler_client = logging.FileHandler(os.path.join(__directory, 'server.log'), mode='w')

SERVER_LOGGER = logging.getLogger('server')
SERVER_LOGGER.setLevel(logging.INFO)

__handler_client.setFormatter(__formater)

SERVER_LOGGER.addHandler(__handler_client)