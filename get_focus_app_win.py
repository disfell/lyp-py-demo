import psutil
import win32gui
import win32process

try:
  pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
  print(psutil.Process(pid[-1]).name().replace('.exe', ''))
except Exception as e:
  print(e)