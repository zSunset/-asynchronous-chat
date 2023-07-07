from .client_log_config import CLIENT_LOGER
from .server_log_config import SERVER_LOGGER
import inspect



def log(func_log):

    def log_saver(*args, **kwargs):
        if SERVER_LOGGER:
            ret = func_log(*args, **kwargs)
            if SERVER_LOGGER.debug:
                SERVER_LOGGER.debug(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}.'
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if SERVER_LOGGER.critical:
                SERVER_LOGGER.critical(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if SERVER_LOGGER.error:
                SERVER_LOGGER.error(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if SERVER_LOGGER.warning:
                SERVER_LOGGER.warning(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if SERVER_LOGGER.info:
                SERVER_LOGGER.info(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )

        if CLIENT_LOGER:
            ret = func_log(*args, **kwargs)
            if CLIENT_LOGER.debug:
                CLIENT_LOGER.debug(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}.'
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if CLIENT_LOGER.critical:
                CLIENT_LOGER.critical(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if CLIENT_LOGER.error:
                CLIENT_LOGER.error(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if CLIENT_LOGER.warning:
                CLIENT_LOGER.warning(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
            if CLIENT_LOGER.info:
                CLIENT_LOGER.info(
                    f'Была вызвана функция {func_log.__name__} с параметроми {args}, {kwargs}.'
                    f'Вызов из модуля {func_log.__module__}. Вызов из '
                    f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2
                )
        return ret
    return log_saver