import logging

# 获取当前 OS
def get(level='DEBUG'):
    if level == 'DEBUG':
      return logging.DEBUG
    elif level == 'INFO':
      return logging.INFO
    elif level == 'WARNING':
      return logging.WARNING
    elif level == 'ERROR':
      return logging.ERROR
    elif level == 'CRITICAL':
      return logging.CRITICAL
    else:
      return logging.DEBUG