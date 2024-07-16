import logging
import os
import utils.get_logging_level as g_log_level

class LoggingConfig:
    logger = None

    @staticmethod
    def setup_logging():
      level = g_log_level.get(os.environ.get('LOG_LEVEL'))
      if LoggingConfig.logger is not None:
        return LoggingConfig.logger
      # 定义日志根目录
      log_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs')
      # 确保日志目录存在
      os.makedirs(log_dir, exist_ok=True)
      
      # 日志文件名，使用日期和时间戳来区分不同运行的日志文件
      log_filename_date = LoggingConfig._get_date_string()
      log_path = os.path.join(log_dir, f'{log_filename_date}.log')

      # 创建一个日志记录器
      logger = logging.getLogger('my_logger')
      logger.setLevel(level)

      # 创建一个日志格式
      log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

      # 创建一个文件处理器，用于写入debug和info日志，每次运行覆盖旧文件
      file_handler = logging.FileHandler(log_path, mode='w')
      file_handler.setLevel(level)
      file_handler.setFormatter(log_format)

      # 将文件处理器添加到日志记录器
      logger.addHandler(file_handler)
      LoggingConfig.logger = logger
      logger.info(f'log_path: {log_path}')
      return LoggingConfig.logger

    @staticmethod
    def _get_date_string():
      # 返回日期字符串，格式为：'YYYYMMDD_HHMMSS'
      from datetime import datetime
      return datetime.now().strftime('%Y%m%d_%H%M%S')