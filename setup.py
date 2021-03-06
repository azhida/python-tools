import os
import setuptools

# 如果readme文件中有中文，那么这里要指定encoding='utf-8'，否则会出现编码错误
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

# 允许setup.py在任何路径下执行
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# 版本号，每次更新都需要更新该值
version = '0.0.8'

setuptools.setup(
    name="azhida_tools",  # 库名，需要在pypi中唯一
    version=version,  # 版本号
    author="azhida",  # 作者
    author_email="334064034@qq.com",  # 作者邮箱（方便使用者发现问题后联系我们）
    description="常用工具包",  # 简介
    long_description='',  # 详细描述（一般会写在README.md中）
    long_description_content_type="text/markdown",  # README.md中描述的语法（一般为markdown）
    url="https://github.com/azhida/python-tools.git",  # 库/项目主页，一般我们把项目托管在GitHub，放该项目的GitHub地址即可
    packages=setuptools.find_packages(),  # 默认值即可，这个是方便以后我们给库拓展新功能的
    classifiers=[  # 指定该库依赖的Python版本、license、操作系统之类的
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[  # 该库需要的依赖库
        # '你的库依赖的第三方库（也可以指定版本）',
        # exapmle
        # 'pyautogui',
        # 'Django >= 1.11, != 1.11.1, <= 2',
    ],
    python_requires='>=3.6',
)