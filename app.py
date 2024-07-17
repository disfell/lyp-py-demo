from datetime import datetime, timedelta
import utils.get_os as get_os
import utils.get_focus_app as g_app
import os
import requests
import json
import logging
import logging_conf
import concurrent.futures
import time

# 设置日志
logging_conf.setup_logging()
logger = logging.getLogger(__name__)

# 一些全局变量
last_send_time = datetime.now()
current_app = ''
current_platform = get_os.get()
lypink = os.getenv('LYP_INK_DOMAIM', 'http://localhost:3000')


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

    # 计算上一次请求距当前时间，隔了多久
    time_difference = current_time - last_send_time

    # 如果一直是同一个App，大于1分钟可刷新一次；如果是不同App，看立即刷新
    if (time_difference >= timedelta(seconds=60) or focus_app != current_app) and (
            focus_app != '' or current_app != ''):
        current_app = focus_app
        json_data = {'current_app': current_app, 'platform': current_platform}
        try:
            ret = requests.post(f'{lypink}/api/supa', json={'id': '19960928', 'msg': json.dumps(json_data)})
            logger.info(f'req succ, req={json_data}, ret={ret.content}')
        except Exception as e:
            logger.exception(e)
        last_send_time = datetime.now()


logger.info(f"当前系统: {current_platform}")
with concurrent.futures.ThreadPoolExecutor() as executor:
    while True:
        executor.submit(job)
        time.sleep(10)
