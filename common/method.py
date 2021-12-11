




import time
from selenium.webdriver.common.by import By
def exec_search(driver,url,name,password,key):
    driver.get(url)
    driver.find_element(By.ID,'username').send_keys(name)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'btnSubmit').click()
    username=driver.find_element(By.XPATH,('//p')).text
    driver.find_element(By.XPATH,"//span[text()='零售出库']").click()   #注意单引号和双引号的配对区分
    time.sleep(3)
    id=driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute('id')  #获取id属性
    frame_id=id+'-frame'   #得到iframe id
    driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(frame_id)))  #通过id进行 iframe的页面切换
    driver.find_element(By.ID,'searchNumber').send_keys(key)  #对子页面的元素进行操作
    driver.find_element(By.ID,'searchBtn').click()
    time.sleep(0.1)
    text=driver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
    return  text #返回文本


