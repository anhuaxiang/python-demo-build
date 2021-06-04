from setuptools import setup, Extension
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='spam',
    version='0.0.1',
    author="anhuaxiang",
    author_email="1342181530@qq.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://anhuaxiang.cn",
    project_urls={
        "Bug Tracker": "https://anhuaxiang.cn",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=False,  # 为True根据 MANIFEST.in 中定义的文件获取 https://docs.python.org/3.8/distutils/sourcedist.html
    package_data={
        '': ['*.txt'],  # 所有包下的文件
        'demo': ['data/*.csv', '*.txt', 'data/*.txt']  # demo包下的文件
    },
    exclude_package_data={"": ["exclude.txt"]},  # 不包括所有包下的文件
    python_requires=">=3.6",
    install_requires=[
        'docutils',
    ],
    ext_modules=[
        Extension('spam', ['lib/spammodule.c'])
    ],
    entry_points={'console_scripts': [
        'demo-run = demo.demo:main'  # 会生成 demo-run的命令，调用demo.demo.main函数
    ]},
)
