# SPHUI

## 介绍

SPHUI基于Python的Tkinter库，为SPHLIB创建的一个GUI/CLI库。可以用于生成SPHLIB所需要的配置文件，并可调用和运行SPHLIB的程序。

关于SPHLIB见[SPHLIB项目地址](https://github.com/ZZP-DMU/SPHLIB)

## 主要特性
[x] 生成SPHLIB的配置文件

[ ] 运行SPHLIB程序(主要是SPHLIB还没写) 

## 安装使用

### 0. 安装

#### 源码安装

1. 安装python3（必需）
2. 安装git（非必需）
3. `git clone https://github.com/ZZP-DMU/SPHUI.git`.如果读者未安装git,可以直接下载本仓库。
4. `cd path/to/SPHUI`.对于巨硬使用者可以使用cmd or powershell等。
5. `python3 main.py`

##### pip安装

1. `pip install sphui`

#### 打包上传pypi(和读者无关)
1. `python3 -m build`
2. `python3 -m twine upload --repository testpypi dist/*`上传到testpypi中
3. `python3 -m twine upload dist/*`

### 1. 生成SPHLIB配置文件
1. `python3 -m sphui`

### 2. 调用SPHLIB程序

---
作者：张志鹏

邮箱：[3671669089@qq.com](3571669089@qq.com)

