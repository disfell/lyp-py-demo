import platform


# 获取当前 OS
def get():
    system = platform.system()
    if system == 'Windows':
        return 'Windows'
    elif system == 'Darwin':
        return 'macOS'
    elif system == 'Linux':
        return 'Linux'
    else:
        return ''
