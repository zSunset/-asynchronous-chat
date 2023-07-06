import logging as logging
import os
from logging.handlers import TimedRotatingFileHandler
from time import sleep

__rot_directory = '/home/sunset/Рабочий стол/-asynchronous-chat/lesson_3/log_file/server.log'

def get_filename(filename):
    # Получаем директорию, где расположены логи
    log_directory = os.path.split(filename)[0]

    # suffix - это расширение (с точкой) файла. 
    # У нас - %Y%m%d. Например .20181231.
    # Точка нам не нужна, т.к. файл будет называться suffix.log (20181231.log)
    date = os.path.splitext(filename)[1][1:]

    # Сформировали имя нового лог-файла
    filename = os.path.join(log_directory, date)

    if not os.path.exists('{}.log'.format(filename)):
        return '{}.log'.format(filename)

    # Найдём минимальный индекс файла на текущий момент.
    index = 0
    f = '{}.{}.log'.format(filename, index)
    while os.path.exists(f):
        index += 1
        f = '{}.{}.log'.format(filename, index)
    return f


rotation_logging_handler = TimedRotatingFileHandler(__rot_directory, when='s', interval=1, backupCount=5)
rotation_logging_handler.suffix = 'server' + '%Y%m%d'
rotation_logging_handler.namer = get_filename

logger = logging.getLogger()
logger.addHandler(rotation_logging_handler)

for i in range(121):
    logger.error('current iteration: {}'.format(i))

