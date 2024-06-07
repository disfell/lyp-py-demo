from AppKit import NSWorkspace
from urllib.parse import unquote
import time

def get_focused_app_info():
    ws = NSWorkspace.sharedWorkspace()
    app = ws.frontmostApplication()
    
    if app:
        # app_name = app.localizedName()
        app_path = unquote(app.bundleURL().absoluteString())
    else:
        # app_name = "无"
        app_path = ""

    return app_path

print(get_focused_app_info())