import pytest
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AnxiangWebbackebd:
    def __init__(self):
        #创建浏览器对象
        self.q1=Options()
        #禁用黑盒模式
        self.q1.add_argument("--no-sandbox")
        #保持浏览器打开对象
        self.q1.add_experimental_option('detach',True)
        #创建并启动浏览器
        self.driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=self.q1)

    #打开安享理财页面
    def launch(self):
        self.driver.get("http://121.43.169.97:8082/")

    def close(self):
        self.driver.close()

@pytest.fixture(scope="session")
def anxiangbackend_web():
    Anxiang=AnxiangWebbackebd()
    Anxiang.launch()
    yield Anxiang
    # Anxiang.close()

