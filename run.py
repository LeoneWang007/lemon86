
from selenium import webdriver
from common import method  #从公共包中导入公共方法
from testdata import data  #导入测试数据
driver=webdriver.Chrome()
driver.implicitly_wait(10)
url=data.testdata.get('url')
name=data.testdata.get('name')
passwd=data.testdata.get('password')
key=data.testdata.get('key')
result=method.exec_search(driver=driver,url=url,name=name,password=passwd,key=key)  #调用method中的函数，并接受返回值
if key in result:
    print('搜索成功')
else:
    print('搜索失败')