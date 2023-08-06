from dotenv import load_dotenv
import logging
import os
load_dotenv()

DEFAULT_IP_ADDRESS = os.getenv('DEFAULT_IP_ADDRESS')
DEFAULT_PORT = int(os.getenv('DEFAULT_PORT'))
MAX_CONNECTIONS = int(os.getenv('MAX_CONNECTIONS'))
MAX_PACKAGE_LENGTH = int(os.getenv('MAX_PACKAGE_LENGTH'))
ENCODING = os.getenv('ENCODING')
ACTION = os.getenv('ACTION')
TIME = os.getenv('TIME')
USER = os.getenv('USER')
ACCOUNT_NAME = os.getenv('ACCOUNT_NAME')
PRESENCE = os.getenv('PRESENCE')
RESPONSE = os.getenv('RESPONSE')
ERROR = os.getenv('ERROR')
LOGGING_LEVEL = logging.DEBUG
MESSAGE = os.getenv('MESSAGE')
MESSAGE_TEXT = os.getenv('MESSAGE_TEXT')
SENDER = os.getenv('SENDER')
DESTINATION = os.getenv('DESTINATION')
EXIT = os.getenv('EXIT')
SERVER_DATABASE = os.getenv('SERVER_DATABASE')
LIST_INFO = os.getenv('LIST_INFO')
USERS_REQUEST = os.getenv('USERS_REQUEST')
ADD_CONTACT = os.getenv('ADD_CONTACT')
REMOVE_CONTACT = os.getenv('remove')
GET_CONTACTS = os.getenv('get_contacts')
SERVER_CONFIG = os.getenv('server.ini')
PUBLIC_KEY_REQUEST = os.getenv('pubkey_need')
DATA = os.getenv('bin')
PUBLIC_KEY = os.getenv('pubkey')


RESPONSE_200 = {RESPONSE: 200}
RESPONSE_202 = {RESPONSE: 202,
                LIST_INFO: None
                }

RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
    }
RESPONSE_205 = {
    RESPONSE: 205
    }

RESPONSE_511 = {
    RESPONSE: 511,
    DATA: None
    }
