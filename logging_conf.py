import logging
import sys
from logging.handlers import TimedRotatingFileHandler
import os


def setup_logging():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    # 读取环境变量，设置日志级别（如果有）
    logging_level = os.getenv('LOGGING_LEVEL', 'DEBUG').upper()
    numeric_level = getattr(logging, logging_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {logging_level}')

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(numeric_level)  # 设置控制台输出的日志级别

    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    file_handler = TimedRotatingFileHandler(
        filename=os.path.join(logs_dir, 'app.log'),
        when='h',  # 每小时分割
        interval=1,  # 每小时
        backupCount=24  # 保留最近24个文件
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(numeric_level)  # 设置文件输出的日志级别

    logger = logging.getLogger()
    logger.setLevel(numeric_level)  # 设置日志记录器的级别
    logging_console = os.getenv('LOGGING_CONSOLE', 'true').lower() in ('true', '1', 't')
    if logging_console:
        logger.addHandler(console_handler)  # 添加控制台处理器
    logger.addHandler(file_handler)  # 添加文件处理器
