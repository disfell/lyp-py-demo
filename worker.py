import sched
import time
from datetime import datetime, timedelta
import get_os
import get_focus_app
import action_working

scheduler = sched.scheduler(time.time, time.sleep)
last_send_working = datetime.now()

# 执行任务
def job():
    global last_send_working
    
    try:
      get_focus_app.get()
    except Exception as e:
      print(f"Error: {e}")
    
    current = datetime.now()
    lsd_diff = current - last_send_working
    if lsd_diff >= timedelta(seconds=30):
      last_send_working = current
      action_working.heartbeat()

    scheduler.enter(4, 1, job)

print(f"当前系统: {get_os.get()}")
# 立即执行job
scheduler.enter(0, 1, job)
scheduler.run()