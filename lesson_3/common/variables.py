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
