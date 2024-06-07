import subprocess
import sched
import time
from datetime import datetime
import platform

scheduler = sched.scheduler(time.time, time.sleep)
last_send_working = None

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

def job():
    global last_send_working
    last_send_working = datetime.now()
    
    focus_app = subprocess.run(['python3', 'get_focus_app.py'], stdout=subprocess.PIPE, text=True)
    if focus_app.returncode == 0:
        focus_app_ret = focus_app.stdout.strip()
    else:
        focus_app_ret = ''
    print(focus_app_ret)

    current = datetime.now()
    lsd_diff = current - last_send_working
    print(last_send_working)
    if lsd_diff >=60:
        last_send_working = current
        print('change:' + last_send_working)

    scheduler.enter(2, 1, job)

print(get_os())
# 立即执行job
scheduler.enter(0, 1, job)
scheduler.run()