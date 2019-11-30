# 推荐使用 Python 3.7.1 以上版本
# 开发时使用 Python 3.7.4 IDLE 64Bit
# 推荐编码为 ANSI
# 使用 UTF-8 测试时出现了一些bug.
# MBR-Studio Project
############
# 特别鸣谢
# bmyjack 的 Multic-Toolbox 项目

# 导入必须文件
import os
import uuid
import platform
#import psutil
#此处运行失败，转换为注释模式
import turtle
import socket

print('自检完成，请稍后')
print('软件信息：')
#软件信息部分
ver = '4.1.1 Release'
print('版本号为 v' + ver)


#由于环境设置时失败，暂时该模块使用 MT

#Python
print('##########关于运行库##########')
print('运行库版本: ' + platform.python_version())




#System
print('##########关于系统##########')
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('1.1.1.1',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_load():
    f = open("/proc/loadavg")
    loadstate=f.read().split()
    return loadstate
load_list = get_load()[0:3]
system_load = ''
for i in load_list:
    if system_load:
        system_load = system_load+','+i
    else:
        system_load = i



myname = socket.getfqdn(socket.gethostname())
print('system: ' + platform.system())
print('system version: ' + platform.version())
print('hostname:',myname)
print('host ip:',get_host_ip())
print('host MAC address:',get_mac_address())
print('system load(1, 5, 15):',system_load)
print('system tasks:',len(psutil.pids()))

devs = psutil.disk_partitions()
for dev in devs:
    statvfs = os.statvfs(dev.mountpoint)
devs = psutil.disk_partitions()
for dev in devs:
    statvfs = os.statvfs(dev.mountpoint)
    total_disk_space = statvfs.f_frsize * statvfs.f_blocks
    free_disk_space = statvfs.f_frsize * statvfs.f_bfree
    disk_usage = int((total_disk_space - free_disk_space) * 100.0 / total_disk_space)
    print('mounted on equipment：%s，mount point：%s disk utilization:%d%%  file system:%s' % (dev.device,dev.mountpoint,disk_usage,dev.fstype))
print()

print('硬件信息：')
#cpu
cts = psutil.cpu_times()
cputime = 0
for item in cts:
    if item != 0:
        cputime = cputime + item
print('##########CPU##########')
print('CPU family: ' + platform.processor())
print('user：%d%%' % (cts.user/cputime * 100))
print('kernel：%d%%' % (cts.system/cputime * 100))
print('free：%d%%' % (cts.idle/cputime * 100))
print('Number of logical CPUs:',psutil.cpu_count())
print('Number of physical CPUs:',psutil.cpu_count(logical=False))
print()

#MEM
print('##########恰好吃的内存##########')
mem = psutil.virtual_memory()
print('Memory size: %dM'%(int(mem.total/1024/1024)))
print('Used memory: %dM'%(int(mem.used/1000/1000)))
print('Remaining memory:%dM'%(int(mem.free/1024/1024)))
print('Memory utilization: %d%%'%(int(mem.percent)))


print()

