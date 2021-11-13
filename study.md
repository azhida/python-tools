# 学习记录

打包命令
```
python setup.py sdist bdist_wheel
```
检查包
```
python -m twine check dist/*
```
上传 pypi
```
python -m twine upload dist/*
```
下载安装
```
python -m pip install -U azhida-tools
```
