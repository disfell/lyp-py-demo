#!/bin/bash

# 设置环境变量
export LYP_INK_DOMAIM="https://lyp.ink"
export LOGGING_LEVEL="INFO"
export LOGGING_CONSOLE="false"

# 获取脚本的绝对路径
SCRIPT_PATH=$(realpath "$0")

# 获取脚本所在的目录
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")

# 切换到脚本所在的目录
cd "$SCRIPT_DIR" || exit 1

# 虚拟环境的相对路径
VENV_DIR="$SCRIPT_DIR/.venv"

# 依赖文件的相对路径
REQUIREMENTS_FILE="$SCRIPT_DIR/requirements_macos.txt"

# Python脚本的相对路径
PYTHON_SCRIPT="$SCRIPT_DIR/app.py"

# 检查虚拟环境是否存在
if [ ! -d "$VENV_DIR" ]; then
    # 创建虚拟环境
    python3 -m venv "$VENV_DIR"
fi

# 激活虚拟环境
. "$VENV_DIR/bin/activate"

pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple

# 在虚拟环境中更新依赖项
pip3 install -r "$REQUIREMENTS_FILE" --upgrade -i https://mirrors.aliyun.com/pypi/simple

# 执行Python脚本
python3 "$PYTHON_SCRIPT"
