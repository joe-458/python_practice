import  pyautogui
import  time
import os
import xlwings as xw
import pyperclip

# 读取Excel表格数据


pyautogui.FAILSAFE =False
pyautogui.PAUSE = 0.8 
#print(pyautogui.size())   # 返回所用显示器的分辨率； 输出：Size(width=2560, height=1440)
#pyautogui.keyDown('alt')
#pyautogui.keyDown('tab')
#pyautogui.keyUp('tab')
#pyautogui.keyUp('alt')

#进入主界面后的退出流程
def tuichu():
    #点击个人中心
    pyautogui.click(2501,1270) 
    pyautogui.click(2501,1270) 
    #pyautogui.mouseDown(x=2400, y=132, button='left')
    #pyautogui.mouseUp(x=2560, y=132, button='left')
    #点击设置
    pyautogui.click(2509,132) 
    time.sleep(1)
    #这一步是以防出现类似日历的东西
    pyautogui.click(2013,132) 
    pyautogui.click(2509,132) 
    #退出登录
    pyautogui.click(2290,932)     
    #确定
    pyautogui.click(2398,773) 
    #定位登陆界面输入框
    pyautogui.click(2272,452) 
    #删除电话号
    pyautogui.press('backspace', presses=11, interval=0.05)

def denglu(data):
    #pyautogui.hotkey('ctrl','c')
    pyautogui.click(2272,452) 
    pyautogui.hotkey('ctrl','v')
    #判断是否是0352开头
    if 0 <= data <= 79:
        pyautogui.press('backspace', presses=2, interval=0.05)
    #登录流程
    pyautogui.click(2113,605) 
    pyautogui.dragTo(2559,605,duration=0.5) 
    pyautogui.click(2048,979)
    pyautogui.click(2272,759)



if __name__ == "__main__":
    #start = time.time()
    app = xw.App(visible=False, add_book=False)
    '''wb_all_data是退休人员数据总表'''
    wb_all_data = app.books.open('D:\\pythonpractice\\工作簿.xlsx')
    sheet_all_data = wb_all_data.sheets[3]
    #这个是确定电话所在列，改动这个就行
    list_value = sheet_all_data.range('C1:C97').value
    print(pyautogui.position())
    #确定输入数据个数，改动这个就行
    for i in range(0,37):
        data = i
        print(list_value[i])
        tuichu()#里面是退出流
        pyperclip.copy(list_value[i])
        denglu(data)#里面是登录

    wb_all_data.close()

    #end = time.time()
    #print(end-start)
        

        