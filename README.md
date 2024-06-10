python -m venv myprojectenv


win:
.\myprojectenv\Scripts\activate

列出依赖
pip freeze > requirements_win.txt

安装依赖
pip install -r requirements_win.txt

macos
source myprojectenv/bin/activate

列出依赖
pip freeze > requirements_macos.txt

安装依赖
pip install -r requirements_macos.txt

临时切换pip源
pip install some-package -i https://pypi.mirrors.ustc.edu.cn/simple/