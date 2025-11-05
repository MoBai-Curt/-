import tkinter as tk
import random
import time
import sys
import math

h, a = [], []
# 提示文本
t = ['多喝水哦~', '好好爱自己', '好好吃饭', '保持好心情', '我想你了', '顺顺利利', '别熬夜', '天冷了多穿衣服']
# 背景颜色
c = ['pink', 'lightblue', 'lightgreen', 'lemonchiffon', 'hotpink', 'skyblue']


def generate_heart_points(n, screen_width, screen_height):
    """生成爱心形状的点坐标"""
    points = []
    for i in range(n):
        theta = i / n * 2 * math.pi
        x = 16 * math.sin(theta) ** 3
        y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)
        screen_x = int(screen_width / 2 + x * 20 - 75)
        screen_y = int(screen_height / 2 - y * 20 - 20)
        clamped_x = max(0, min(screen_x, screen_width - 150))
        clamped_y = max(0, min(screen_y, screen_height - 40))
        points.append((clamped_x, clamped_y))
    return points


def create_window(x, y, tip=None, is_heart=True):
    """创建提示窗口"""
    window = tk.Toplevel()
    window.geometry(f"150x40+{x}+{y}")
    window.title('提示')
    window.attributes('-topmost', 1)
    window.attributes('-alpha', 1.0)
    bg_color = random.choice(c)
    text = tip or random.choice(t)
    tk.Label(
        window,
        text=text,
        bg=bg_color,
        font=('微软雅黑', 16),
        width=20,
        height=3
    ).pack()
    window.bind('<space>', lambda e: [w.destroy() for w in h + a] or sys.exit())
    return window


def explode_heart(root, heart_windows, screen_width, screen_height):
    """爱心爆开效果：更快的扩散速度"""
    explode_duration = 0.5  # 爆炸动画持续时间缩短到0.5秒
    frame_count = 30  # 保持帧数确保流畅性
    interval = explode_duration / frame_count  # 每帧间隔更短
    
    # 计算爱心中心（爆炸原点）
    center_x = screen_width / 2
    center_y = screen_height / 2
    
    # 为每个窗口设置更快的扩散参数
    explode_params = []
    for window in heart_windows:
        angle = random.uniform(0, 2 * math.pi)  # 随机角度
        distance = random.uniform(80, 400)  # 扩散距离增加
        speed = random.uniform(1.5, 3.0)  # 速度因子提高
        x = window.winfo_x()
        y = window.winfo_y()
        explode_params.append((angle, distance, speed, x, y))
    
    # 执行爆炸动画
    for frame in range(frame_count):
        progress = frame / frame_count
        for i, window in enumerate(heart_windows):
            if not (isinstance(window, tk.Toplevel) and window.winfo_exists()):
                continue
                
            angle, distance, speed, start_x, start_y = explode_params[i]
            move_x = distance * math.cos(angle) * progress * speed
            move_y = distance * math.sin(angle) * progress * speed
            new_x = int(start_x + move_x)
            new_y = int(start_y + move_y)
            new_x = max(-200, min(new_x, screen_width + 50))
            new_y = max(-200, min(new_y, screen_height + 50))
            window.geometry(f"+{new_x}+{new_y}")
            window.attributes('-alpha', 1.0 - progress * 1.2)
            
        root.update()
        time.sleep(interval)


def main():
    root = tk.Tk()
    root.withdraw()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    heart_points_count = 100  # 组成爱心的窗口数量

    heart_points = generate_heart_points(heart_points_count, screen_width, screen_height)
    for i, (x, y) in enumerate(heart_points):
        window = create_window(x, y, "保持好心情" if i == heart_points_count - 1 else None)
        h.append(window)
        root.update()
        time.sleep(0.02)

    # 爱心爆开效果（更快）
    time.sleep(0.01)  # 缩短停顿时间
    explode_heart(root, h, screen_width, screen_height)

    for window in h:
        if isinstance(window, tk.Toplevel) and window.winfo_exists():
            window.destroy()
    h.clear()

    total_notes = (screen_width // 150) * (screen_height // 40) + 50
    for _ in range(total_notes):
        x = random.randint(0, screen_width - 150)
        y = random.randint(0, screen_height - 40)
        window = create_window(x, y, is_heart=False)
        a.append(window)
        root.update()
        time.sleep(0.005)
    time.sleep(10)
    close_duration = 1.0
    if a:
        interval = close_duration / len(a)
        for window in a:
            if isinstance(window, tk.Toplevel) and window.winfo_exists():
                window.destroy()
            root.update()
            time.sleep(interval)
    a.clear()

    root.mainloop()


if __name__ == "__main__":
    main()