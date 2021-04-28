import logging

downloader_logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./errors.log', mode='w')
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s: %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

downloader_logger.addHandler(console_handler)
downloader_logger.addHandler(file_handler)