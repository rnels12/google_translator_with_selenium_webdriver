import logging
import sys

def activate_logging(log_level: str | None = ''):
  if log_level is None:
    return

  logger = logging.getLogger("WebPage.web_page")
  logger.addHandler(logging.StreamHandler(sys.stdout))

  if log_level.upper() in "DEBUG":
    logger.setLevel(logging.DEBUG)
  elif log_level.upper() in "INFO":
    logger.setLevel(logging.INFO)
  else:
    pass




