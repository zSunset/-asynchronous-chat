import json
import sys
import socket
import time

from log.decorat_log import log
from log.client_log_config import CLIENT_LOGER
from common.utils import load_configs, send_message, get_message

CONFIGS = dict()


@log
def create_presence_message(account_name, CONFIGS):
    message = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.time(),
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): account_name
        }
    }
    CLIENT_LOGER.info('Создание сообщения для отпарвки на сервер.')
    return message

@log
def handle_response(message, CONFIGS):
    CLIENT_LOGER.info('Обработка сообщения от сервера.')
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] == 200:
            CLIENT_LOGER.info('Успешная обработка сообшения от сервера.')
            return '200 : OK'
        CLIENT_LOGER.critical('Обработка сообщения от сервера провалилась.')
        return f'400 : {message[CONFIGS.get("ERROR")]}'
    raise ValueError

@log
def main():
    global CONFIGS
    CONFIGS = load_configs(is_server=False)
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
    except ValueError:
        CLIENT_LOGER.critical('Порт должен быть указан в пределах от 1024 до 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    presence_message = create_presence_message('Guest', CONFIGS)
    CLIENT_LOGER.info(f'Отправка сообшения серверу.')
    send_message(transport, presence_message, CONFIGS)
    try:
        response = get_message(transport, CONFIGS)
        hanlded_response = handle_response(response, CONFIGS)
        CLIENT_LOGER.debug(f'Ответ от сервера: {response}')
        CLIENT_LOGER.info(f'Обработанный ответ от сервера: {hanlded_response}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGER.critical('Ошибка декодирования сообщения')


if __name__ == '__main__':
    main()