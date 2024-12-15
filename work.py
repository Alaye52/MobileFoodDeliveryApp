import pyautogui
import time
import subprocess
# 启动应用（示例：python main.py）
subprocess.Popen(["python", "main.py"])
time.sleep(3) # 等待GUI出现
# 使用坐标点击 "Register" 按钮（请根据实际情况调整坐标）
pyautogui.click(x=100, y=200)
time.sleep(1)
# 输入邮箱
pyautogui.typewrite("testuser@example.com")
pyautogui.press("tab")
# 输入密码
pyautogui.typewrite("ValidPass123")
pyautogui.press("tab")
# 确认密码
pyautogui.typewrite("ValidPass123")
pyautogui.press("enter")
# 等待确认
time.sleep(2)
pyautogui.screenshot("registration_result.png")
# 手动检查截图或使用OCR确认成功消息