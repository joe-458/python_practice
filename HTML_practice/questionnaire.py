from selenium.webdriver.common.by import By  # 没有selenium库的(请在所用的环境下pip install selenium)
from selenium import webdriver  #selenium库
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.options import Options
import random  # 用于产生随机数
import time  # 用于延时
'''import pyautogui  # 用于模拟人手'''



'''proxy_ip = "61.128.128.0"
proxy_port = "8081"

# 创建代理对象
proxy = webdriver.Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f"{proxy_ip}:{proxy_port}"
proxy.ssl_proxy = f"{proxy_ip}:{proxy_port}"

# 将代理对象添加到WebDriver对象中
capabilities = webdriver.DesiredCapabilities.EDGE
proxy.add_to_capabilities(capabilities)
'''





def gundong(driver, distance): #延时+屏幕滚动
    js = "var q=document.documentElement.scrollTop=" + str(distance)    #下拉像素(800是基于最顶端测算的距离)
    driver.execute_script(js)
    time.sleep(0.5)

def danxuan(driver,selector):
    # 找到所有标签（定位问题）这里是单选
        dan = driver.find_elements(By.CSS_SELECTOR,(f'#div{selector} > div.ui-controlgroup.column1'))
        for answer in dan:
            ans = answer.find_elements(By.CSS_SELECTOR,'.ui-radio')#对应的绝对子标签
            random.choice(ans).click()  # 找到标签并点击
            time.sleep(random.randint(0, 1))

def duoxuan(driver):
    #这里是多选题,找到所有多选的标签
    duo = driver.find_elements(By.CSS_SELECTOR,'#div7 > div.ui-controlgroup.column1')
    for answer in duo:
        ans = answer.find_elements(By.CSS_SELECTOR,'.ui-checkbox')#对应的绝对子标签
        #随机填几次
        for i in range(1, 2):#这里的7可以改成5，10，12
            random.choice(ans).click()#找到标签并点击
        time.sleep(random.randint(0, 1))

    duo = driver.find_elements(By.CSS_SELECTOR,'#div8 > div.ui-controlgroup.column1')
    for answer in duo:
        ans = answer.find_elements(By.CSS_SELECTOR,'.ui-checkbox')#对应的绝对子标签
        #随机填几次
        for i in range(1, 2):#这里的7可以改成5，10，12
            random.choice(ans).click()#找到标签并点击
        time.sleep(random.randint(0, 1))

'''def tiankong(driver, num):
    #填空函数
    #这里是所需要问题的标签汇总，例如有四个要答的问题，下面的answer的ABC数量需要跟index里面的数量相等
    index = ["A", "B", "C"]
    # 自定义要回答的答案
    answer = {"A": "python真的好用！", "B": "这个测试很成功！", "C": "填空题随机填写文本"}
    driver.find_element(by=By.CSS_SELECTOR, value=f'#q{num}')\
        .send_keys(answer.get(index[random.randint(0, len(index)-1)]))
'''

'''def renzheng(driver):
    # 智能验证,找到智能认证的标签
    bth = driver.find_elements(By.CSS_SELECTOR,'#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0')
    bth.click()#点击
    time.sleep(1)
    rectBottom = driver.find_elements(By.CSS_SELECTOR,'#rectBottom') #提交按钮
    rectBottom.click() #点击
    time.sleep(5)
'''

'''def huakuai():
    # 当次数多了的时候就会出现滑块，这里是模拟人手解决滑块拖动
    pyautogui.moveTo(random.randint(494, 496), 791, 0.2)#控制鼠标移动到x,y处，耗时0.2秒
    time.sleep(1)
    pyautogui.dragTo(random.randint(888, 890), 791, 1)#让鼠标点击并拖拽到x,y处，耗时1秒
    time.sleep(1)
    pyautogui.click(random.randint(652, 667), random.randint(793, 795))#让鼠标点击x,y处
    time.sleep(1)
    pyautogui.moveTo(random.randint(494, 496), 791, 0.2)#控制鼠标移动到x,y处，耗时0.2秒
    time.sleep(1)
    pyautogui.dragTo(random.randint(888, 890), 791, 1)#让鼠标点击并拖拽到x,y处，耗时1秒
'''

def zonghe(times):
    for i in range(0, times):
        # 初始配置，地址
        url = 'https://www.wjx.cn/vm/OnGjGws.aspx'
        url_survey = url
        option = Options()
        option.add_argument('--headless')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument("--user-agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) > AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/12A365 > MicroMessenger/8.0.34 NetType/WIFI  '")   
        driver = webdriver.Edge(options = option)
        #本地下载的edge浏览器地址
        option.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

             

        #Here you specify the actual profile folder    
        #option.add_argument("--profile-directory=Profile 1")     

        #Here you set the path of the profile ending with User Data not the profile folder
        #option.add_argument("--user-data-dir=C:\\Users\\27782\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")

        '''proxy = {"http": "http://118.190.244.234:3128","https": "https://118.190.244.234:3128"}
        option.add_argument('--proxy-server%s' % proxy)'''

        



        



        # 下载好的edge驱动的地址
        #driver = webdriver.Edge(r'D:\pythonpractice\HTML_practice\msedgedriver.exe')
        #覆写浏览器用户代理，模拟成微信用户
        #driver.execute_cdp_cmd(
        #    'Network.setUserAgentOverride', {"userAgent":'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) > AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/12A365 > MicroMessenger/8.0.34 NetType/WIFI' }
        #   )
        



        # 启动要填写的地址
        driver.get(url_survey)

        #time.sleep(100)

        num=1
        for num in range(1,7):
            danxuan(driver,num) #调用单选函数
        duoxuan(driver) #调用多选函数
        gundong(driver, 600)#调用滚动屏幕函数，如果不需要则注释掉
        #tiankong(driver, 3)#调用填空题函数
        #最后交卷点击提交
        time.sleep(random.randint(0, 1))
        driver.find_element(By.ID,'ctlNext').click()#找到提交的css并点击
        #time.sleep(4)

        #renzheng(driver)#智能认证函数调用
        #huakuai()#滑块函数调用
        print('已经提交了{}次问卷'.format(int(i) + int(1)))
        time.sleep(0.5)
        driver.quit()#停止



if __name__ == "__main__":
    zonghe(5)#里面填写的数是表示要提交多少次问卷