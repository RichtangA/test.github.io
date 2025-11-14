from telnetlib import EC
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
充值
'''
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# @pytest.mark.skip()
@pytest.mark.order(10)
class Test_rechargr():
    def recharge(self,anxiang_web,money,valicode):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-menu.fl.ng-scope > div.menu > div:nth-child(1) > dl > dd:nth-child(2) > a"))).click()

        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#money"))).send_keys(money)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#valicode"))).send_keys(valicode)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div:nth-child(6) > input"))).click()
    def clear(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#money"))).send_keys(Keys.CONTROL,'a')
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#money"))).send_keys(Keys.BACK_SPACE)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#valicode"))).send_keys(Keys.CONTROL,'a')
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#valicode"))).send_keys(Keys.BACK_SPACE)

   #失败充值 充值金额为0
    def test_rechargefail_moneyis0(self,anxiang_web):
        self.recharge(anxiang_web,0,8888)
        assert  WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div.item.verify-group.fn-clear.has-error > div > label"))).text=="充值金额必须大于0的整数或保留两位小数"
        self.clear(anxiang_web)

    # 失败充值 充值金额为null
    def test_rechargefail_moneyisnull(self, anxiang_web):
        self.recharge(anxiang_web, "", 8888)
        assert  WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div.item.verify-group.fn-clear.has-error > div > label"))).text == "不能为空"
        self.clear(anxiang_web)

    # 失败充值 充值金额为1000000001
    def test_rechargefail_moneyis1000000001(self, anxiang_web):
        self.recharge(anxiang_web, 1000000000001, 8888)
        sleep(1)
        assert  WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div.item.verify-group.fn-clear.has-error > div > label"))).text == "不能为空"
        sleep(2)
        self.clear(anxiang_web)

    # 失败充值 充值金额为非整数
    def test_rechargefail_moneyisnotnum(self, anxiang_web):
        self.recharge(anxiang_web, 100000.111, 8888)
        sleep(1)
        assert  WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div.item.verify-group.fn-clear.has-error > div > label"))).text == "不能为空"
        self.clear(anxiang_web)

    # 失败充值 充值金额为非数字
    def test_rechargefail_moneyisnotnum2(self, anxiang_web):
        self.recharge(anxiang_web, "你好", 8888)
        assert  WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div.item.verify-group.fn-clear.has-error > div > label"))).text == "不能为空"
        self.clear(anxiang_web)

        # 失败充值 验证码为空
    def test_rechargefail_valicodeisnull(self, anxiang_web):
        self.recharge(anxiang_web, 1000, "")

        assert  WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div > div.cont.ng-scope > div > form > div.item.verify-group.verify-code.has-error > label.control-label.dy-error"))).text == "不能为空"
        self.clear(anxiang_web)

        # 失败充值验证码错误
    def test_rechargefail_valicodeiseorr(self, anxiang_web):
        self.recharge(anxiang_web, 1000, 1111)
        # assert anxiang_web.driver.find_element(By.XPATH,
        #                                        "//*[@id='xubox_layer3']/div[1]/div/span[2]").text == "验证码错误"
        self.clear(anxiang_web)
    # @pytest.mark.skip
   #成功充值
    def test_recharge_success(self,anxiang_web):
       self.recharge(anxiang_web,100,8888)
       WebDriverWait(anxiang_web.driver, 10).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-top > div > div.sub-nav.fr > li.last > span > a"))).click()
