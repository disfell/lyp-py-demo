import sched
import time
from datetime import datetime, timedelta
import utils.get_os as get_os
import utils.get_focus_app as g_app
import os
import requests
import json
from logger.my_logger import LoggingConfig

logger = LoggingConfig.setup_logging()

# 轮训执行程序
scheduler = sched.scheduler(time.time, time.sleep)

# 一些全局变量
last_send_time = datetime.now()
current_app = ''
current_platform = get_os.get()

# 执行任务
def job():
  global last_send_time
  global current_app
  current_time = datetime.now()
  
  # ==================  获取聚焦的 APP ================== 
  focus_app = ''
  try:
    focus_app = g_app.get()
  except Exception as e:
    logger.exception(e)
  logger.debug(f'focus_app={focus_app}')
  # ==================  获取聚焦的 APP ================== 
  
  lypink = os.environ.get('LYP_INK_DOMAIM')
  if lypink is None:
    lypink = 'http://localhost:3000'

  time_difference = current_time - last_send_time

  if (time_difference >= timedelta(seconds=60) or focus_app != current_app) and (focus_app != '' or current_app != ''):
    current_app = focus_app
    json_data = {'current_app': current_app, 'platform': current_platform}
    try:
      ret = requests.post(f'{lypink}/api/supa', json={'id': '19960928', 'msg': json.dumps(json_data)})
      logger.info(f'req succ, req={json_data}, ret={ret.content}')
    except Exception as e:
      logger.exception(e)
    last_send_time = datetime.now()
  
  scheduler.enter(10, 0, job)

logger.info(f"当前系统: {current_platform}")
# 立即执行job
scheduler.enter(0, 0, job)
scheduler.run()