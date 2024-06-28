# 创建本地环境

python -m venv .venv

或者

python3 -m venv .venv

# Windows

**进入本地环境**

.venv\Scripts\activate

**列出依赖**

pip freeze > requirements_win.txt

或者

pip3 freeze > requirements_win.txt

**安装依赖**

pip install -r requirements_win.txt

或者

pip3 install -r requirements_win.txt

**执行app.py**

# macOS

**进入本地环境**

. .venv/bin/activate

**列出依赖**

pip freeze > requirements_macos.txt

或者

pip3 freeze > requirements_macos.txt

**安装依赖**

pip install -r requirements_macos.txt

或者

pip3 install -r requirements_macos.txt

**执行app.py**

**安装 realpath**

brew install coreutils