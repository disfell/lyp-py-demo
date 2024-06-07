import subprocess
import sched
import time
from datetime import datetime,timedelta
import platform

scheduler = sched.scheduler(time.time, time.sleep)
last_send_working = datetime.now()

# 获取当前 OS
def get_os():
    system = platform.system()
    if system == 'Windows':
      return 'Windows'
    elif system == 'Darwin':
      return 'macOS'
    elif system == 'Linux':
      return 'Linux'
    else:
      return ''

# 执行任务
def job():
    global last_send_working
    focus_app = subprocess.run(['python3', 'get_focus_app.py'], stdout=subprocess.PIPE, text=True)
    if focus_app.returncode == 0:
      focus_app_ret = focus_app.stdout.strip()
    else:
      focus_app_ret = ''
    print(focus_app_ret)

    current = datetime.now()
    lsd_diff = current - last_send_working
    print(last_send_working)
    if lsd_diff >= timedelta(seconds=30):
      last_send_working = current
      print('change:' + str(last_send_working))

    scheduler.enter(2, 1, job)

print(f"当前系统: {get_os()}")
# 立即执行job
scheduler.enter(0, 1, job)
scheduler.run()