import logging
import sched
import time
from datetime import datetime, timedelta
import utils.get_os as get_os
import utils.get_focus_app as g_app
import act_working
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
last_send_working = datetime.now()

scheduler = sched.scheduler(time.time, time.sleep)
# 获取当前时间的格式化字符串，例如：'2024-06-14_15-42-30'
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# 定义日志文件的基本名称和扩展名
log_base_name = 'app_log'
log_extension = '.log'
# 完整的日志文件名，包含时间戳
log_file_path = os.path.join('logs', f"{log_base_name}_{current_time}{log_extension}")
logging.basicConfig(
  level=logging.INFO,  # 日志级别
  filename=log_file_path,  # 日志文件名，将被保存在当前文件夹
  filemode='w',  # 模式，'a'表示追加，'w'表示覆盖
  format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
  datefmt='%Y-%m-%d %H:%M:%S'  # 自定义时间格式，不包含毫秒
)

# 执行任务
def job():
  global last_send_working
  current = datetime.now()
  
  focus_app = ''
  try:
    focus_app = g_app.get()
  except Exception as e:
    logging.exception(e)
  logging.debug(f'focus_app={focus_app}')

  time_diff = current - last_send_working
  if time_diff >= timedelta(seconds=60):
    last_send_working = current
    act_working.heartbeat()

  scheduler.enter(5, 1, job)

logging.info(f"当前系统: {get_os.get()}")
# 立即执行job
scheduler.enter(0, 1, job)
scheduler.run()