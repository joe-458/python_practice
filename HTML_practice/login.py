from selenium.webdriver.common.by import By
from selenium import webdriver  #selenium库
from selenium.webdriver.edge.options import Options
import random  # 用于产生随机数
import time  # 用于延时



def login():
    url = 'http://121.30.193.137:81'
    option = Options()
    #option.add_argument('--headless')
    driver = webdriver.Edge(options = option)
    # 下载好的edge驱动的地址
    #driver = webdriver.Edge(r'D:\pythonpractice\HTML_practice\msedgedriver.exe')
    driver.get(url)
    driver.find_element(By.ID,'login_username').send_keys("15203520811")#找到提交的id并填充用户名
    driver.find_element(By.ID,'login_password1').send_keys("Jx123456.")#找到提交的id并填充密码
    driver.find_element(By.ID,'login_button').click()#找到提交的id并点击
    #print("登陆成功")
    time.sleep(5)
    driver.find_element(By.CLASS_NAME,'d_name  ').click()#找到提交的id并点击
    time.sleep(10)



if __name__ == "__main__":
    login() #登陆程序

