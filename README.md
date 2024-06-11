# 创建本地环境

python3 -m venv .venv

# Windows

**进入本地环境**

.venv\Scripts\activate

**列出依赖**

pip freeze > requirements_win.txt  
pip3 freeze > requirements_win.txt

**安装依赖**

pip install -r requirements_win.txt  
pip3 install -r requirements_win.txt

# macOS

**进入本地环境**

. .venv/bin/activate

**列出依赖**

pip freeze > requirements_macos.txt  
pip3 freeze > requirements_macos.txt

**安装依赖**

pip install -r requirements_macos.txt  
pip3 install -r requirements_macos.txt

# 执行App

gunicorn -w 4 flask_app:app

# 临时切换pip源

pip install some-package -i https://pypi.mirrors.ustc.edu.cn/simple/