import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('宝宝')
    window.geometry("220x50" + "+" + str(a) + "+" + str(b))

    # 修正提示文字列表：补全引号、修正分隔符、闭合列表
    texts = [
        '记得加衣!',
        '记得照顾好自己',
        '天天开心，好好吃饭',
        '早点休息',
        '别感冒'
    ]
    text = random.choice(texts)

    # 修正背景色列表：添加赋值符号、补全引号和分隔符、闭合列表
    bg_colors = [
        'pink',
        'lavender',
        'lightyellow',
        'Darkviolet',
        'orange',
        'Lightskyblue',
        'lightgreen'
    ]
    bg = random.choice(bg_colors)

    # 中文逗号改为英文逗号
    tk.Label(window,
             text=text,
             bg=bg,
             font=('楷体', 18),
             width=25,
             height=4
             ).pack()
    window.mainloop()


threads = []
for i in range(350):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()