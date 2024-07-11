from selenium.webdriver.common.by import By  # 没有selenium库的(请在所用的环境下pip install selenium)
from selenium import webdriver  #selenium库
from selenium.webdriver.support.select import Select 
import random  # 用于产生随机数
import time  # 用于延时
'''import pyautogui  # 用于模拟人手'''


'''def gundong(driver, distance): #延时+屏幕滚动
    js = "var q=document.documentElement.scrollTop=" + str(distance)    #下拉像素(800是基于最顶端测算的距离)
    driver.execute_script(js)
    time.sleep(0.5)
'''

def xiaoqumingtiankong(driver):
    #填空函数
    #这里是所需要问题的标签汇总，例如有四个要答的问题，下面的answer的ABC数量需要跟index里面的数量相等
    index = ["A", "B", "C","D"]
    # 自定义要回答的答案
    answer = {"A": "局西小区", "B": "局内小区", "C": "二七小区","D":"惠安新居"}
    driver.find_element(by=By.CSS_SELECTOR, value=f'#q2')\
        .send_keys(answer.get(index[random.randint(0, len(index)-1)]))
    


    
def danxuan(driver):
    # 找到所有标签（定位问题）这里是单选
        
        '''dan = driver.find_elements(By.CSS_SELECTOR,('#div2 > div.ui-controlgroup.two_column'))
        for answer in dan:
            ans = answer.find_elements(By.CSS_SELECTOR,'.ui-radio')#对应的绝对子标签
            random.choice(ans).click()  # 找到标签并点击
            time.sleep(random.randint(0, 1))'''

        for num in range(4,31):
            dan = driver.find_elements(By.CSS_SELECTOR,(f'#div{num} > div.ui-controlgroup.column1'))
            for answer in dan:
                ans = answer.find_elements(By.CSS_SELECTOR,'.ui-radio')#对应的绝对子标签
                random.choice(ans).click()  # 找到标签并点击
                time.sleep(random.randint(0, 1))
        
        '''dan = driver.find_elements(By.CSS_SELECTOR,('#div15 > div.ui-controlgroup.column1'))
        for answer in dan:
            ans = answer.find_elements(By.CSS_SELECTOR,'.ui-radio')#对应的绝对子标签
            random.choice(ans).click()  # 找到标签并点击
            time.sleep(random.randint(0, 1))'''      

'''def duoxuan(driver):
    #这里是多选题,找到所有多选的标签
    for num in range(13,15):
        duo = driver.find_elements(By.CSS_SELECTOR,f'#div{num} > div.ui-controlgroup.column1')
        for answer in duo:
            ans = answer.find_elements(By.CSS_SELECTOR,'.ui-checkbox')#对应的绝对子标签
            #随机填几次
            for i in range(1, 2):#这里的7可以改成5，10，12
                random.choice(ans).click()#找到标签并点击
            time.sleep(random.randint(0, 1))'''


def tiankong(driver, num):
    dri = driver.find_element(by=By.CSS_SELECTOR, value=f'#q{num}')
    dri.click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@class="select2-selection__rendered"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//li[contains(text(), "平城区")]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//span[contains(text(), "请选择街道")]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//li[contains(text(), "新华街道")]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//span[contains(text(), "请选择社区")]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//li[contains(text(), "局西社区")]').click()
    time.sleep(0.5)
    #driver.find_element(By.XPATH,'//span[contains(text(), "请选择小区名称")]').click()
    #time.sleep(0.5)
    #driver.find_element(By.XPATH,'//li[contains(text(), "局西小区")]').click()
    #time.sleep(0.5)
    driver.find_element(By.XPATH,'//a[contains(text(), "确定")]').click()





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
        option = webdriver.EdgeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        # 本地下载的谷歌浏览器地址
        option.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msdege.exe'
        # 下载好的Chrome驱动的地址
        driver = webdriver.Edge(r'D:\pythonpractice\HTML_practice\msedgedriver.exe')
        '''driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                               {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})'''
        # 初始配置，地址
        url_survey = 'https://app-quest.datongshutou.com/vm/wAbDGA.aspx'
        # 启动要填写的地址
        driver.get(url_survey)
        
        xiaoqumingtiankong(driver)#调用填空题函数
        time.sleep(1)
        tiankong(driver, 1)#调用填空题函数
        danxuan(driver) #调用单选函数
        #duoxuan(driver) #调用多选函数
        '''gundong(driver, 600)#调用滚动屏幕函数，如果不需要则注释掉'''
        
        # 最后交卷点击提交
        time.sleep(random.randint(0, 1))
        driver.find_element(By.CSS_SELECTOR,'#ctlNext').click()#找到提交的css并点击
        time.sleep(1)

        '''renzheng(driver)#智能认证函数调用'''
        '''huakuai()#滑块函数调用'''
        print('已经提交了{}次问卷'.format(int(i) + int(1)))
        time.sleep(4)
        driver.quit()#停止

if __name__ == "__main__":
    zonghe(1)#里面填写的数是表示要提交多少次问卷