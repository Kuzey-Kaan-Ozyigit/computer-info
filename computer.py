import psutil
import shutil
import platform
import socket

def cpu():
    return psutil.cpu_percent(interval=0)

def drive():
    Usage = shutil.disk_usage("/")
    class DriveInfo:
        def total(self):
            return Usage.total
        def used(self):
            return Usage.used
        def free(self):
            return Usage.free
    return DriveInfo()
drive_info = drive()

def ram():
    ram_information = psutil.virtual_memory()
    class RamInfo():
        def total(self):
            return ram_information.total
        def used(self):
            return ram_information.used
        def free(self):
            return ram_information.free
    return RamInfo()
ram_info = ram()

def computer():
    class Computer():
        def system(self):
            return platform.system()
        def release(self):
            return platform.release()
        def architecture(self):
            return platform.architecture()[0]
    return Computer()
computer_info = computer()

def web():
    class Web():
        def hostname(self):
            return socket.gethostname()
        def ip_adress(self):
            return socket.gethostbyname(socket.gethostname())
    return Web()
web_info = web()