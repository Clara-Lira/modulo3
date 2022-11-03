from loguru import logger

logger.info("Essa é uma info")
logger.warning("Este é um warning")
logger.error("Este é um erro")

try:
    print(40/0)
except ZeroDivisionError as error:
    logger.error(error)