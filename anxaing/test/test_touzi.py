from time import sleep

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

'''
投资
'''
# @pytest.mark.skip()
@pytest.mark.order(12)

class Test_touzi:
    # def test_touzi(self,anxiang_web):
    #     anxiang_web.driver.find_element(By.XPATH,"//*[@id='mlayout']/div[2]/div[2]/div[1]/a/em").click()
    def touzi(self,anxiang_web):
        # anxiang_web.driver.find_element(By.XPATH,"//*[@id='mlayout']/div[2]/div[2]/div[1]/a/em").click()

        # target=anxiang_web.driver.find_element(By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(2) > a")
        # ActionChains(anxiang_web.driver).move_to_element(target).perform()
        # anxiang_web.driver.find_element(By.XPATH,"//*[@id='ng-app']/body/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/a").click()
        # WebDriverWait(anxiang_web.driver, 10).until(
        #     lambda d: len(d.window_handles) > 1
        # )
        anxiang_web.driver.find_element(By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(2) > a").click()
        handlers=anxiang_web.driver.window_handles
        anxiang_web.driver.switch_to.window(handlers[-1])
        target=WebDriverWait(anxiang_web.driver,10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='ng-app']/body/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/a"))
        )
        target.click()
    def input(self,anxiang_web,account):
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#money"))
        ).send_keys(account)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#tender_form > p:nth-child(5) > input.tender-sub.ng-scope"))).click()
    def clear(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#money"))).clear()

        # 投资金额为非整数
    def test_touzifail_accountisnotint(self, anxiang_web):
        self.touzi(anxiang_web)
        anxiang_web.driver.implicitly_wait(5)
        self.input(anxiang_web, 50.3)
        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(5)
    #投资金额非10的整数倍
    def test_touzifail_accountisnot50(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.input(anxiang_web, 144)
        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(5)
    def test_touzifail_accountless50(self, anxiang_web):
        self.input(anxiang_web, 40)
        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(5)
#投资金额大于投资金额
    def test_touzifail_accountmore1000000(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.input(anxiang_web, 4040000000000000000000000000000000000000000000000000000000)
        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(5)
#投资金额大于可投
    def test_touzifail_accountmorecan(self, anxiang_web):
        self.input(anxiang_web, 300000)
        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(5)
#余额不足
    def touzifail_accountnotenough(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.input(anxiang_web, 30000)
        anxiang_web.driver.switch_to.frame(anxiang_web.driver.find_element(By.CSS_SELECTOR,"#xubox_iframe5"))
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="tender_new_submit"]'))
        ).click()
        anxiang_web.driver.switch_to.default_content()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#xubox_layer5 > div.xubox_main > span.xubox_setwin'))
        ).click()
        self.clear(anxiang_web)
#投自己的标
#未开通账户
#未进行风险评估
#借款标过期
#借款标满标待审
#投资人未登录
#投资失败  投资金额为空
    def test_touzifail_accountisnull(self,anxiang_web):
        anxiang_web.driver.implicitly_wait(5)
        self.input(anxiang_web,"")

        # WebDriverWait(anxiang_web.driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-top > div > div.sub-nav.fr > li.last > span > a"))).click()
    def test_success(self,anxiang_web):
        sleep(2)
        self.input(anxiang_web,10000)
