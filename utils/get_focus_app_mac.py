from AppKit import NSWorkspace
from urllib.parse import unquote
import json

ws = NSWorkspace.sharedWorkspace()
app = ws.frontmostApplication()
file_path = 'utils/dict_macos_app.json'

if app:
  # app_name = app.localizedName()
  app_path = unquote(app.bundleURL().absoluteString())
  app_name_dict = json.load(open(file_path, 'r', encoding='utf-8'))
  app_path = app_name_dict.get(app_path, '')
else:
  # app_name = "无"
  app_path = ""

print(app_path)