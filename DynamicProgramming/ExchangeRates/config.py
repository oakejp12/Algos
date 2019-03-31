import logging

root_logger = logging.getLogger(__name__)
root_logger.setLevel(logging.DEBUG)

CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setLevel(logging.WARNING)
CONSOLE_HANDLER.setFormatter(logging.Formatter(
    fmt='{levelname}: {message}', style='{'))
root_logger.addHandler(CONSOLE_HANDLER)

LOG_FILE = "./dynamicprogramming.log"
LOG_FILE_HANDLER = logging.FileHandler(str(LOG_FILE))
LOG_FILE_HANDLER.setLevel(logging.DEBUG)
fmt_s = '{asctime} ' + \
    '{module}.{funcName} line {lineno}: {levelname}: {message}'
LOG_FILE_HANDLER.setFormatter(logging.Formatter(fmt=fmt_s, style='{'))
root_logger.addHandler(LOG_FILE_HANDLER)
