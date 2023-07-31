import win32api
import win32con
import threading
import tkinter as tk


def LeftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def confirm_delay():
    global CLICKDELAY
    if not E_delay.get().isdigit():
        win32api.MessageBox(None, "不是整数!", "类型错误", win32con.MB_ICONWARNING)
        return None
    CLICKDELAY = float(E_delay.get())
    root.title(f"延迟:{CLICKDELAY}毫秒")


def StartProcess():
    global work
    work = threading.Timer(CLICKDELAY/1000, LeftClick)
    work.run()


def StopProcess():
    work.close()


CLICKDELAY = 1000
root = tk.Tk()
root.title(f"延迟:{CLICKDELAY}毫秒")
root.resizable(0, 0)
root.grid()
L_delay_F = tk.Label(root, text="按键延迟:")
E_delay = tk.Entry(root, width=10)
L_delay_B = tk.Label(root, text="毫秒")
B_delay = tk.Button(root, text="确认", width=12, command=confirm_delay)
B_run = tk.Button(root, text="启动", command=StartProcess)
B_stop = tk.Button(root, text="停止", command=StopProcess)
L_delay_F.grid(column=0, row=0)
E_delay.grid(column=1, row=0)
L_delay_B.grid(column=2, row=0)
B_delay.grid(column=3, row=0)
B_run.grid(column=0, columnspan=2, row=1, sticky="nswe")
B_stop.grid(column=2, columnspan=2, row=1, sticky="nswe")
root.mainloop()
