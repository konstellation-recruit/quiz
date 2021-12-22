import logging
from rich.logging import RichHandler


def get_logger(log_file=None, log_level=logging.INFO):
    logger = logging.getLogger("quizquiz")
    handlers = [
        RichHandler(log_level, show_path=False, rich_tracebacks=True)
    ]

    if log_file is not None:
        handlers.append(logging.FileHandler(log_file, 'w'))

    # fmt = logging.Formatter('%(asctime)s [%(name)s][%(levelname)s] %(message)s')
    fmt = logging.Formatter('%(message)s')
    for h in handlers:
        h.setFormatter(fmt)
        h.setLevel(log_level)
        logger.addHandler(h)

    logger.setLevel(log_level)
    return logger
