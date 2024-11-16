import tkinter as tk
import tkinter.messagebox
import subprocess
import time
import threading
import shutil
import ctypes
import sys
import os

from psutil._compat import unicode


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system("初始化模块.exe")
    time.sleep(2)
    def shutdown():
        os.system("shutdown /s /t 0")

    def restart():
        os.system("shutdown /r /t 0")

    def logout():
        os.system("shutdown /l")

    def quxiao():
        os.system("shutdown -a")

    def blue():
        def submit():
            entered_password = password_entry.get()
            if entered_password == '12344321':
                    if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                        if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                            if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                                if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                                    if tk.messagebox.askyesno("警告",
                                                              "此操作会导致系统错误,这是最后一次提醒,你要继续吗？"):
                                        os.system("Taskkill /fi \"pid ge 1\" /f")



        root = tk.Tk()
        root.title("密码输入")

        label = tk.Label(root, text="请输入密码：")
        label.pack(pady=10)

        password_entry = tk.Entry(root, show="•")
        password_entry.pack(pady=10)

        submit_button = tk.Button(root, text="提交", command=submit)
        submit_button.pack(pady=10)

        root.mainloop()






    def open_c_drive():
        def submit1():
            entered_password = password_entry.get()
            if entered_password == '12344321':
                if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                    if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                        if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                            if tk.messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                                if tk.messagebox.askyesno("警告",
                                                          "此操作会导致系统错误,这是最后一次提醒,你要继续吗？"):
                                    os.system(r"mountvol c:\ /d")

        root = tk.Tk()
        root.title("密码输入")

        label = tk.Label(root, text="请输入密码：")
        label.pack(pady=10)

        password_entry = tk.Entry(root, show="•")
        password_entry.pack(pady=10)

        submit_button = tk.Button(root, text="提交", command=submit1)
        submit_button.pack(pady=10)

        root.mainloop()
    def delete_cache():
        cache_path = r"C:\Users\seewo\AppData\Local\Temp"
        shutil.rmtree(cache_path, ignore_errors=True)
        tk.messagebox.showinfo("提示", "系统缓存已删除")

    def open_task_manager():
        subprocess.Popen("taskmgr")

    def write():
        for i in range(0,100):
            os.system("start cmd")
            os.system("taskkill /F /im cmd.exe")

    def xfwin():
        def sfc():
            os.system("sfc/scannow")
        def chkdsk():
            os.system("chadsk C: /f")
        def sllsystem():
            def putong():
                os.system(r"start 360系统急救箱/360compkill64/SuperKillller.exe")
            def yingji():
                os.system(r"powershell 360系统急救箱/360compkill64/360急救箱运行不了请点我.bat")
            def yingji1():
                os.system(r"start 360系统急救箱/360compkill64/所有360程序无法运行时请双击.com")
            # def yingji2():
            #     os.system("cd D:/supperkiller")
            #     os.system("move ../360系统急救箱/360compkill64/急救箱运行不了被删除请将我放到其他目录改名运行后再下载使用.exe D:/supperkiller")
            #     os.system("D:/supperkiller/急救箱运行不了被删除请将我放到其他目录改名运行后再下载使用.exe")
            sy = tk.Tk()
            xf.title = "修复系统"
            btn_shutdown = tk.Button(sy, text="360系统急救箱普通版", command=putong)
            btn_shutdown.pack()
            btn_shutdown = tk.Button(sy, text="360系统急救箱应急包", command=yingji)
            btn_shutdown.pack()
            btn_shutdown = tk.Button(sy, text="所有360程序无法运行时", command=yingji1)
            btn_shutdown.pack()
            # btn_shutdown = tk.Button(sy, text="移动到其他目录后运行", command=yingji2)
            # btn_shutdown.pack()
        xf = tk.Tk()
        xf.title = "修复系统"
        btn_shutdown = tk.Button(xf, text="sfc/scannow", command=sfc)
        btn_shutdown.pack()
        btn_shutdown = tk.Button(xf, text="chkdsk", command=chkdsk)
        btn_shutdown.pack()
        btn_shutdown = tk.Button(xf, text="360系统急救箱", command=sllsystem)
        btn_shutdown.pack()

    def PowerShell():
        os.system("start powershell")

    def Cmd():
        os.system("start cmd")

    def schedule_action(action_type, seconds):
        time.sleep(seconds)
        if action_type == "shutdown":
            os.system("shutdown /s /t 0")  # Windows系统关机命令
        elif action_type == "restart":
            os.system("shutdown /r /t 0")  # Windows系统重启命令
        elif action_type == "logout":
            os.system("shutdown /l /t 0")  # Windows系统注销命令
    def sanliuling():
        os.system("360.exe")
    def sanliulingsd():
        os.system("360sd.exe")
    def huorong():
        os.system("sysdiag.exe")
    def vir_kill_software():
        vir_kill_software=tk.Tk()
        vir_kill_software.title="杀毒软件"
        # 360按钮
        btn_shutdown = tk.Button(vir_kill_software, text="360安全卫士极速版", command=sanliuling)
        btn_shutdown.pack()
        btn_shutdown = tk.Button(vir_kill_software, text="360杀毒", command=sanliulingsd)
        btn_shutdown.pack()
        # 火绒按钮
        btn_shutdown = tk.Button(vir_kill_software, text="火绒安全", command=huorong)
        btn_shutdown.pack()
    def schedule():
        seconds = int(entry_seconds.get())
        action_type = action_var.get()
        threading.Thread(target=schedule_action, args=(action_type, seconds)).start()

    def force_terminate(process_name):
        os.system(f"taskkill /im {process_name} /f")
        tk.messagebox.showinfo("提示", f"已强制终止 {process_name} 进程")

    def create_process_termination():
        process_name = entry_process_name.get()
        threading.Thread(target=force_terminate, args=(process_name,)).start()

    def mianze():
        tk.messagebox.showinfo("免责声明", "本程序造成的一切后果由使用者承担，与程序开发者无关。")

    app = tk.Tk()
    app.title("电脑工具")
    app.iconname("1.ico")
    # 关机按钮
    btn_shutdown = tk.Button(app, text="关机", command=shutdown)
    btn_shutdown.pack()

    # 重启按钮
    btn_restart = tk.Button(app, text="重启", command=restart)
    btn_restart.pack()

    # 注销按钮
    btn_logout = tk.Button(app, text="注销", command=logout)
    btn_logout.pack()



    # 蓝屏按钮
    btn_blue = tk.Button(app, text="蓝屏", command=blue)
    btn_blue.pack()

    btn_open_c = tk.Button(app, text="写入缓存", command=write)
    btn_open_c.pack()

    # 弹出C盘按钮
    btn_open_c = tk.Button(app, text="弹出C盘", command=open_c_drive)
    btn_open_c.pack()

    btn_logout = tk.Button(app, text="取消定时关闭", command=quxiao)
    btn_logout.pack()

    # 杀毒软件按钮
    btn_shutdown = tk.Button(app, text="杀毒软件", command=vir_kill_software)
    btn_shutdown.pack()

    # 修复系统按钮
    btn_shutdown = tk.Button(app, text="修复系统", command=xfwin)
    btn_shutdown.pack()

    btn_shutdown = tk.Button(app, text="PowerShell", command=PowerShell)
    btn_shutdown.pack()

    btn_shutdown = tk.Button(app, text="Cmd", command=Cmd)
    btn_shutdown.pack()

    # 删除系统缓存按钮
    btn_delete_cache = tk.Button(app, text="删除系统缓存", command=delete_cache)
    btn_delete_cache.pack()

    # 打开任务管理器按钮
    btn_task_manager = tk.Button(app, text="打开任务管理器", command=open_task_manager)
    btn_task_manager.pack()

    # 设置关机、重启、注销的时间
    action_var = tk.StringVar(value="shutdown")

    tk.Radiobutton(app, text="关机", variable=action_var, value="shutdown").pack()
    tk.Radiobutton(app, text="重启", variable=action_var, value="restart").pack()
    tk.Radiobutton(app, text="注销", variable=action_var, value="logout").pack()

    entry_seconds = tk.Entry(app)
    entry_seconds.pack()
    entry_seconds.insert(0, "输入秒数")

    btn_schedule = tk.Button(app, text="设置延迟", command=schedule)
    btn_schedule.pack()

    # 强制终止进程输入
    entry_process_name = tk.Entry(app)
    entry_process_name.pack()
    entry_process_name.insert(0, "输入进程名")

    btn_force_terminate = tk.Button(app, text="强制终止进程", command=create_process_termination)
    btn_force_terminate.pack()
    btn_task_manager = tk.Button(app, text="免责声明", command=mianze)
    btn_task_manager.pack()
    app.mainloop()
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)