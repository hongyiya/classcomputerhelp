from win10toast import ToastNotifier

def show_notification():
    toaster = ToastNotifier()
    toaster.show_toast(
        "初始化",  # 通知标题
        "正在初始化，预计需要5秒钟",  # 通知内容
        icon_path="1.ico",  # 可选：图标路径
        duration=3,  # 消息持续时间
        threaded=True  # 是否在后台线程中显示
    )

show_notification()