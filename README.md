# 文件资源管理器杀手（explorerkiller）
## 简介
这是一个基于python制作并编译的恶意程序。
## 安全提醒
玩归玩，闹归闹，别拿设备开玩笑。假如你不小心（故意不小心）将此病毒运行，其造成的破坏是可以修复的，参见：
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

