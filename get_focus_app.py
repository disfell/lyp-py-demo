import subprocess
import get_os
import sys

def get_focus_app_mac():
    focus_app = subprocess.run([sys.executable, 'get_focus_app_mac.py'], stdout=subprocess.PIPE, text=True)
    if focus_app.returncode == 0:
      focus_app_ret = focus_app.stdout.strip()
    else:
      focus_app_ret = ''
    return focus_app_ret
    
def get_focus_app_win():
    focus_app = subprocess.run([sys.executable, 'get_focus_app_win.py'], stdout=subprocess.PIPE, text=True)
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