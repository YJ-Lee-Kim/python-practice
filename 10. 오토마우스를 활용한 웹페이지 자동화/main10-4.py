import pyautogui
import pyperclip
import time

weather=["서울 날씨","시흥 날씨", "청주 날씨", "전주 날씨", "부산 날씨", "강원도 날씨"]

addr_x=1108
addr_y=61
start_x=977
start_y=243
end_x=1658
end_y=663

for rg in weather:
    pyautogui.moveTo(addr_x, addr_y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)
    
    pyperclip.copy(rg)
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    save_path="10. 오토마우스를 활용한 웹페이지 자동화\\" + rg + ".png"
    pyautogui.screenshot(save_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))
    