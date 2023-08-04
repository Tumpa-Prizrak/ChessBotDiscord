import logging
from logging.handlers import RotatingFileHandler


def setup_logger() -> logging.Logger:
    logger: logging.Logger = logging.getLogger("discord")
    logger.addHandler(get_file_handler())

    return logger


def get_file_handler() -> RotatingFileHandler:
    """Returns a handler for writing general logs to a file.

    :return: Handler for info level in shared logs
    :rtype: RotatingFileHandler
    """
    file_handler = RotatingFileHandler(
        filename="discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=10,
    )
    file_handler.setFormatter(get_file_formatter())
    file_handler.setLevel(logging.INFO)

    return file_handler

def get_file_formatter() -> logging.Formatter:
    """Returns a formatter for file handlers.
    
    :return: Formatter for ``{`` style logging. 
    :rtype: logging.Formatter
    """
    dt_fmt = "%Y-%m-%d %H:%M:%S"
    return logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
    )
