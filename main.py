from computer import *
import tkinter as tk

def update_cpu():
    cpu_usage = cpu()
    Cpu_Usage.config(text=f"CPU: %{cpu_usage}")
    root.after(1000, update_cpu)

def update_drive():
    drive_info = drive()
    Drive_Total.config(text=f"Total Drive: {drive_info.total() / (1024**3):.2f} GB")
    Drive_Used.config(text=f"Used Drive: {drive_info.used() / (1024**3):.2f} GB")
    Drive_Free.config(text=f"Free Drive: {drive_info.free() / (1024**3):.2f} GB")
    root.after(60000, update_drive)

def update_ram():
    ram_info = ram()
    Ram_Total.config(text=f"Total RAM: {ram_info.total() / (1024**3):.2f} GB")
    Ram_Used.config(text=f"Used RAM: {ram_info.used() / (1024**3):.2f} GB")
    Ram_Free.config(text=f"Free RAM: {ram_info.free() / (1024**3):.2f} GB")
    root.after(1000, update_ram)

root = tk.Tk()
root.title("Computer Information App")
root.attributes("-topmost", True)
#root.iconbitmap('AGElogobeyaz.ico')
root.config(bg="black")


# CPU
cpu_usage = cpu()
Cpu_Usage = tk.Label(root, text=f"CPU: %{cpu_usage}", bg="black", fg="white")
Cpu_Usage.grid(column=0, row=0)
update_cpu()

# Drive
drive_info = drive()
Drive_Total = tk.Label(root, text=f"Total Drive: {drive_info.total() / (1024**3):.2f} GB", bg="black", fg="white")
Drive_Total.grid(column=1, row=0)
Drive_Used = tk.Label(root, text=f"Used Drive: {drive_info.used() / (1024**3):.2f} GB", bg="black", fg="white")
Drive_Used.grid(column=2, row=0)
Drive_Free = tk.Label(root, text=f"Free Drive: {drive_info.free() / (1024**3):.2f} GB", bg="black", fg="white")
Drive_Free.grid(column=3, row=0)
update_drive()

# Ram
ram_info = ram()
Ram_Total = tk.Label(root, text=f"Total RAM: {ram_info.total() / (1024**3):.2f} GB", bg="black", fg="white")
Ram_Total.grid(column=4, row=0)
Ram_Used = tk.Label(root, text=f"Used RAM: {ram_info.used() / (1024**3):.2f} GB", bg="black", fg="white")
Ram_Used.grid(column=5, row=0)
Ram_Free = tk.Label(root, text=f"Free RAM: {ram_info.free() / (1024**3):.2f} GB", bg="black", fg="white")
Ram_Free.grid(column=6, row=0)
update_ram()

# Computer
computer_info = computer()
System = tk.Label(root, text=f"System: {computer_info.system()}", bg="black", fg="white")
System.grid(column=7, row=0)
Release = tk.Label(root, text=f"Release: {computer_info.release()}", bg="black", fg="white")
Release.grid(column=8, row=0)
Architecture = tk.Label(root, text=f"Architecture: {computer_info.architecture()}", bg="black", fg="white")
Architecture.grid(column=9, row=0)

# Web
web_info = web()
HostName = tk.Label(root, text=f"HostName: {web_info.hostname()}", bg="black", fg="white")
HostName.grid(column=10, row=0)
#IP_Adress = tk.Label(content, text=f"IP_Adress: {web_info.ip_adress()}", bg="black", fg="white")
#IP_Adress.grid(column=11, row=0)

root.mainloop()
