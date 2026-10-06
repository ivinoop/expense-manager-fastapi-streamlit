import logging


def configure_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)

    # Configure custom logger
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('server.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger