import logging
import os


__directory = '/home/sunset/Рабочий стол/-asynchronous-chat/lesson_3/log_file/'
__formater = logging.Formatter('%(asctime)-10s %(levelname)-6s %(message)-5s')
__handler_client = logging.FileHandler(os.path.join(__directory, 'client.log'), mode='w')


CLIENT_LOGER = logging.getLogger('client')
CLIENT_LOGER.setLevel(logging.INFO)

__handler_client.setFormatter(__formater)

CLIENT_LOGER.addHandler(__handler_client)


