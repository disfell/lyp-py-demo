import sched
import time
from datetime import datetime,timedelta
from get_os import check_os
import get_focus_app

scheduler = sched.scheduler(time.time, time.sleep)
last_send_working = datetime.now()

# 执行任务
def job():
    global last_send_working
    
    print(get_focus_app.get())
    
    current = datetime.now()
    lsd_diff = current - last_send_working
    if lsd_diff >= timedelta(seconds=30):
      last_send_working = current

    scheduler.enter(2, 1, job)

print(f"当前系统: {check_os()}")
# 立即执行job
scheduler.enter(0, 1, job)
scheduler.run()