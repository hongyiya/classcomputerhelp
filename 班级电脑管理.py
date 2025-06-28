import subprocess
from tkinter import Button, Entry, Label, Tk, StringVar, Radiobutton, Frame, Text, Scrollbar
from tkinter import messagebox
from threading import Thread
from shutil import rmtree
from ctypes import windll
from sys import version_info, executable
from os import system, getlogin
from psutil._compat import unicode
from zipfile import ZipFile
from time import sleep
import psutil

def extract_specific_file(zip_path, file_name):
    with ZipFile(zip_path) as z:
        z.extract(file_name)

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    def shutdown():
        system("shutdown /s /t 0")
        text_output.insert("end", "关机，消息：系统正在关机...\n")

    def restart():
        system("shutdown /r /t 0")
        text_output.insert("end", "重启，消息：系统正在重启...\n")

    def logout():
        system("shutdown /l")
        text_output.insert("end", "注销，消息：用户正在注销...\n")

    def quxiao():
        system("shutdown -a")
        text_output.insert("end", "取消定时关闭，消息：定时关闭已取消...\n")

    def blue():
        def submit():
            entered_password = password_entry.get()
            if entered_password == '12344321':
                if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                    if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                        if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                            if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                                if messagebox.askyesno("警告",
                                                      "此操作会导致系统错误,这是最后一次提醒,你要继续吗？"):
                                    system("Taskkill /fi \"pid ge 1\" /f")
                                    text_output.insert("end", "蓝屏，消息：系统正在蓝屏...\n")

        root = Tk()
        root.title("密码输入")

        label = Label(root, text="请输入密码：")
        label.pack(pady=10)

        password_entry = Entry(root, show="•")
        password_entry.pack(pady=10)

        submit_button = Button(root, text="提交", command=submit)
        submit_button.pack(pady=10)

        root.mainloop()

    def open_c_drive():
        def submit1():
            entered_password = password_entry.get()
            if entered_password == '12344321':
                if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                    if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                        if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                            if messagebox.askyesno("警告", "此操作会导致系统错误,你要继续吗？"):
                                if messagebox.askyesno("警告",
                                                      "此操作会导致系统错误,这是最后一次提醒,你要继续吗？"):
                                    system(r"mountvol c:\ /d")
                                    text_output.insert("end", "弹出C盘，消息：C盘已弹出...\n")

        root = Tk()
        root.title("密码输入")

        label = Label(root, text="请输入密码：")
        label.pack(pady=10)

        password_entry = Entry(root, show="•")
        password_entry.pack(pady=10)

        submit_button = Button(root, text="提交", command=submit1)
        submit_button.pack(pady=10)

        root.mainloop()

    def delete_cache():
        try:
            username = getlogin()
        except OSError:
            import getpass
            username = getpass.getuser()
        cache_path = rf"C:\Users\{username}\AppData\Local\Temp"
        rmtree(cache_path, ignore_errors=True)
        text_output.insert("end", "删除系统缓存，消息：系统缓存已删除...\n")

    def open_task_manager():
        subprocess.Popen("taskmgr")
        text_output.insert("end", "打开任务管理器，消息：任务管理器已打开...\n")

    def write():
        for i in range(0, 10):
            subprocess.Popen("cmd")
            subprocess.Popen("taskkill /F /im cmd.exe")
        text_output.insert("end", "写入缓存，消息：写入缓存完成...\n")

    def xfwin():
        def sfc():
            run_command("sfc/scannow")

        def chkdsk():
            run_command("chkdsk C: /f")

        def sllsystem():
            def putong():
                try:
                    extract_specific_file('360系统急救箱.zip', 'SuperKiller.exe')
                    run_command(r"start SuperKiller.exe")
                    text_output.insert("end", f"解压并运行“SuperKiller.exe”成功...\n")
                except:
                    text_output.insert("end", f"解压并运行“SuperKiller.exe”时出错...\n")

            def yingji():
                try:
                    extract_specific_file('360系统急救箱.zip', '360急救箱运行不了请点我.bat')
                    run_command(r"start 360急救箱运行不了请点我.bat")
                    text_output.insert("end", f"解压并运行“360急救箱运行不了请点我.bat”成功...\n")
                except:
                    text_output.insert("end", f"解压并运行“360急救箱运行不了请点我.bat”时出错...\n")

            def yingji1():
                try:
                    extract_specific_file('360系统急救箱.zip', '所有360程序无法运行时请双击.com')
                    run_command(r"start 所有360程序无法运行时请双击.com")
                    text_output.insert("end", f"解压并运行“所有360程序无法运行时请双击.com”成功...\n")
                except:
                    text_output.insert("end", f"解压并运行“所有360程序无法运行时请双击.com”时出错...\n")

            sy = Tk()
            sy.title = "修复系统"
            btn_shutdown = Button(sy, text="360系统急救箱普通版", command=putong)
            btn_shutdown.pack()
            btn_shutdown = Button(sy, text="360系统急救箱应急包", command=yingji)
            btn_shutdown.pack()
            btn_shutdown = Button(sy, text="所有360程序无法运行时", command=yingji1)
            btn_shutdown.pack()

        xf = Tk()
        xf.title = "修复系统"
        btn_shutdown = Button(xf, text="sfc/scannow", command=sfc)
        btn_shutdown.pack()
        btn_shutdown = Button(xf, text="chkdsk", command=chkdsk)
        btn_shutdown.pack()
        btn_shutdown = Button(xf, text="360系统急救箱", command=sllsystem)
        btn_shutdown.pack()


    def protect_system_mbr_repair(self):
        while self.mbr_protect and self.mbr_value != None:
            try:
                sleep(0.2)
                with open(r"\\.\PhysicalDrive0", "r+b") as f:
                    if f.read(512) != self.mbr_value:
                        f.seek(0)
                        f.write(self.mbr_value)
                        self.system_notification(self.text_Translate("引导分区修复: PhysicalDrive0"))
            except:
                pass

    def PowerShell():
        subprocess.Popen("powershell")
        text_output.insert("end", "PowerShell，消息：PowerShell已打开...\n")

    def Cmd():
        subprocess.Popen("cmd")
        text_output.insert("end", "Cmd，消息：命令提示符已打开...\n")

    def schedule_action(action_type, seconds):
        sleep(seconds)
        if action_type == "shutdown":
            system("shutdown /s /t 0")  # Windows系统关机命令
            text_output.insert("end", f"关机：系统将在{seconds}秒后关机...\n")
        elif action_type == "restart":
            system("shutdown /r /t 0")  # Windows系统重启命令
            text_output.insert("end", f"重启：系统将在{seconds}秒后重启...\n")
        elif action_type == "logout":
            system("shutdown /l /t 0")  # Windows系统注销命令
            text_output.insert("end", f"注销：用户将在{seconds}秒后注销...\n")

    def sanliuling():
        try:
            extract_specific_file('360.zip', '360.exe')
            run_command("360.exe")
            text_output.insert("end", f"解压并运行“360.exe”成功...\n")
        except:
            text_output.insert("end", f"解压并运行“360.exe”时出错...\n")

    def huorong():
        try:
            extract_specific_file('sysdiag.zip', 'sysdiag.exe')
            run_command("sysdiag.exe")
            text_output.insert("end", f"解压并运行“sysdiag.exe”成功...\n")
        except:
            text_output.insert("end", f"解压并运行“sysdiag.exe”时出错...\n")

    def vir_kill_software():
        vir_kill_software = Tk()
        vir_kill_software.title = "杀毒软件"
        btn_shutdown = Button(vir_kill_software, text="360安全卫士极速版", command=sanliuling)
        btn_shutdown.pack()
        btn_shutdown = Button(vir_kill_software, text="火绒安全", command=huorong)
        btn_shutdown.pack()

    def schedule():
        seconds = int(entry_seconds.get())
        action_type = action_var.get()
        Thread(target=schedule_action, args=(action_type, seconds)).start()

    def force_terminate(process_name):
        run_command(f"taskkill /im {process_name} /f")
        # text_output.insert("end", f"强制终止进程，消息：已强制终止 {process_name} 进程...\n")

    def create_process_termination():
        process_name = entry_process_name.get()
        Thread(target=force_terminate, args=(process_name,)).start()

    def mianze():
        text_output.insert("end", "免责声明，消息：本程序造成的一切后果由使用者承担，与程序开发者无关...\n")

    def run_command(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output, error = process.communicate()
        if output:
            text_output.insert("end", output)
        if error:
            text_output.insert("end", error)

    def close_non_system_processes():
        current_pid = psutil.Process().pid
        system_pids = set()

        # 获取所有系统进程和服务的PID
        for proc in psutil.process_iter(['pid', 'name', 'ppid']):
            try:
                if proc.info['ppid'] == 0:  # 父进程ID为0的是系统进程
                    system_pids.add(proc.info['pid'])
                elif proc.info['name'].lower() in ['services.exe', 'smss.exe', 'csrss.exe', 'wininit.exe',
                                                   'winlogon.exe', 'lsass.exe', 'lsm.exe', 'svchost.exe']:
                    system_pids.add(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # 获取所有子进程的PID
        for pid in list(system_pids):
            try:
                proc = psutil.Process(pid)
                for child in proc.children(recursive=True):
                    system_pids.add(child.pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['pid'] != current_pid and proc.info['pid'] not in system_pids:
                    proc.terminate()
                    text_output.insert("end",
                                       f"关闭进程，消息：已终止进程 {proc.info['name']} (PID: {proc.info['pid']})\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def execute_powershell_command(event):
        command = entry_command.get()
        if command:
            text_output.insert("end", f"执行命令: {command}\n")
            run_command(f"powershell {command}")
            entry_command.delete(0, 'end')


    # def submit1():
    #     entered_password = password_entry.get()
    #     if entered_password == '12344321':
    #         pass
    #     else:
    #         run_command('taskkill /f /im 班级电脑管理。exe')
    #
    # root = Tk()
    # root.title("密码输入")
    #
    # label = Label(root, text="请输入密码：")
    # label.pack(pady=10)
    #
    # password_entry = Entry(root, show="•")
    # password_entry.pack(pady=10)
    #
    # submit_button = Button(root, text="提交", command=submit1)
    # submit_button.pack(pady=10)

    app = Tk()
    app.title("班级电脑管理 by 罗弘毅")
    app.iconname("1.ico")




    # root.mainloop()
    # 创建一个框架来容纳按钮
    frame = Frame(app)
    frame.pack()

    # 使用grid布局来放置按钮，并设置按钮的宽度和高度
    btn_shutdown = Button(frame, text="关机", command=shutdown, width=15, height=2)
    btn_shutdown.grid(row=0, column=0, padx=5, pady=5)

    btn_restart = Button(frame, text="重启", command=restart, width=15, height=2)
    btn_restart.grid(row=0, column=1, padx=5, pady=5)

    btn_logout = Button(frame, text="注销", command=logout, width=15, height=2)
    btn_logout.grid(row=0, column=2, padx=5, pady=5)

    btn_blue = Button(frame, text="蓝屏", command=blue, width=15, height=2)
    btn_blue.grid(row=0, column=3, padx=5, pady=5)

    btn_close_non_system = Button(frame, text="关闭非系统进程", command=close_non_system_processes, width=15, height=2)
    btn_close_non_system.grid(row=0, column=4, padx=5, pady=5)

    btn_open_c_drive = Button(frame, text="弹出C盘", command=open_c_drive, width=15, height=2)
    btn_open_c_drive.grid(row=1, column=0, padx=5, pady=5)

    btn_logout = Button(frame, text="取消定时关闭", command=quxiao, width=15, height=2)
    btn_logout.grid(row=1, column=1, padx=5, pady=5)

    btn_shutdown = Button(frame, text="杀毒软件", command=vir_kill_software, width=15, height=2)
    btn_shutdown.grid(row=1, column=2, padx=5, pady=5)

    btn_shutdown = Button(frame, text="修复系统", command=xfwin, width=15, height=2)
    btn_shutdown.grid(row=1, column=3, padx=5, pady=5)

    btn_shutdown = Button(frame, text="PowerShell", command=PowerShell, width=15, height=2)
    btn_shutdown.grid(row=1, column=4, padx=5, pady=5)

    btn_cmd = Button(frame, text="Cmd", command=Cmd, width=15, height=2)
    btn_cmd.grid(row=2, column=0, padx=5, pady=5)

    btn_delete_cache = Button(frame, text="删除系统缓存", command=delete_cache, width=15, height=2)
    btn_delete_cache.grid(row=2, column=1, padx=5, pady=5)

    btn_task_manager = Button(frame, text="打开任务管理器", command=open_task_manager, width=15, height=2)
    btn_task_manager.grid(row=2, column=2, padx=5, pady=5)

    btn_schedule = Button(frame, text="设置延迟", command=schedule, width=15, height=2)
    btn_schedule.grid(row=3, column=4, padx=5, pady=5)

    entry_seconds = Entry(frame, width=15)
    entry_seconds.grid(row=3, column=0, padx=5, pady=5)
    entry_seconds.insert(0, "输入秒数")

    action_var = StringVar(value="shutdown")

    Radiobutton(frame, text="关机", variable=action_var, value="shutdown").grid(row=3, column=1, padx=5, pady=5)
    Radiobutton(frame, text="重启", variable=action_var, value="restart").grid(row=3, column=2, padx=5, pady=5)
    Radiobutton(frame, text="注销", variable=action_var, value="logout").grid(row=3, column=3, padx=5, pady=5)

    btn_force_terminate = Button(frame, text="强制终止进程", command=create_process_termination, width=15, height=2)
    btn_force_terminate.grid(row=4, column=1, padx=5, pady=5)

    entry_process_name = Entry(frame, width=15)
    entry_process_name.grid(row=4, column=0, padx=5, pady=5)
    entry_process_name.insert(0, "输入进程名")

    btn_task_manager = Button(frame, text="免责声明", command=mianze, width=15, height=2)
    btn_task_manager.grid(row=4, column=3, padx=5, pady=5)

    # 创建一个Text小部件来显示输出
    text_output = Text(app, height=10, width=90)
    text_output.pack(padx=5, pady=5)

    # 创建一个Scrollbar并将其与Text小部件关联
    scrollbar = Scrollbar(app, command=text_output.yview)
    scrollbar.pack(side="right", fill="y")
    text_output.config(yscrollcommand=scrollbar.set)

    # 添加命令输入框
    entry_command = Entry(app, width=80)
    entry_command.pack(padx=5, pady=5)
    entry_command.bind("<Return>", execute_powershell_command)

    # 添加执行命令按钮
    btn_execute_command = Button(app, text="执行命令", command=lambda: execute_powershell_command(None))
    btn_execute_command.pack(padx=5, pady=5)

    app.mainloop()


else:
    if version_info[0] == 3:
        windll.shell32.ShellExecuteW(
            None, "runas", executable, __file__, None, 1)
    else:
        windll.shell32.ShellExecuteW(None, u"runas", unicode(executable), unicode(__file__), None, 1)
