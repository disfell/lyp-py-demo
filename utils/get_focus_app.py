import subprocess
import utils.get_os as get_os
import sys
import os
import json
from logger.my_logger import LoggingConfig

logger = LoggingConfig.setup_logging()

def get_focus_app_mac():
    focus_app = subprocess.run([sys.executable, os.path.abspath('utils/get_focus_app_mac.py')], stdout=subprocess.PIPE, text=True)
    if focus_app.returncode == 0:
      focus_app_ret = focus_app.stdout.strip()
    else:
      focus_app_ret = ''
    logger.debug(f'mac current (real)app = {focus_app_ret}')
    if focus_app_ret:
      file_path = 'utils/dict_macos_app.json'
      app_name_dict = json.load(open(file_path, 'r', encoding='utf-8'))
      focus_app_ret = app_name_dict.get(focus_app_ret, '')
    return focus_app_ret
    
def get_focus_app_win():
    focus_app = subprocess.run([sys.executable, os.path.abspath('utils/get_focus_app_win.py')], stdout=subprocess.PIPE, text=True)
    if focus_app.returncode == 0:
      focus_app_ret = focus_app.stdout.strip()
    else:
      focus_app_ret = ''
    return focus_app_ret

def get():
  focus_app = ''
  check = get_os.get()
  if check == 'macOS':
    focus_app = get_focus_app_mac()
  elif check == 'Windows':
    focus_app = get_focus_app_win()
  else:
    focus_app = ''
  return focus_app