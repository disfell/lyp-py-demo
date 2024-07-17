import sys

sys.path.append('..')
from AppKit import NSWorkspace
from urllib.parse import unquote

ws = NSWorkspace.sharedWorkspace()
app = ws.frontmostApplication()

if app:
    # app_name = app.localizedName()
    app_path = unquote(app.bundleURL().absoluteString())
else:
    # app_name = "无"
    app_path = ""

print(app_path)
