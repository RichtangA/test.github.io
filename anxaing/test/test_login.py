from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# 添加显式等待获取错误提示
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
注册登陆界面测试
'''
# @pytest.mark.skip()
@pytest.mark.order(2)
class Test_login:
#登录封装
    def login(self, anxiang_web, password, username):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#keywords"))).send_keys(username)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(password)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-btn"))).click()
    def clear(self,anxiang_web):
        # 点击注册
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(2) > a"))).click()
        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
# 失败登录（调用时保持参数一致）
    # @pytest.mark.skip()
    # 密码错误
    def test_login_passfail(self, anxiang_web):
        #点击tuichu
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div > div.header > div > div.header-top > div > div.sub-nav.fr > li.last.regFinish2 > a.logout"))
        ).click()
        self.login(anxiang_web, "aaa1234560", "923456789")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#login-btn"))).click()
        error_msg = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#err > span"))
        ).text
        assert "密码错误2次,达到3次将锁定账户" in error_msg
        self.clear(anxiang_web)
    #用户不存在
    def test_login_accountfail(self, anxiang_web):
        sleep(2)
        self.login(anxiang_web, "aaa123456", "23456789")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#login-btn"))).click()
        error_msg = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#err > span"))
        ).text
        assert "用户不存在" in error_msg  # 断言错误提示符合预期
        anxiang_web.driver.forward()
        self.clear(anxiang_web)
    #passwordisnull
    def test_passwordisnull(self,anxiang_web):
        sleep(2)
        self.login(anxiang_web, "", "23456789")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-btn"))).click()
        error_msg = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#err > span"))
        ).text
        assert "用户名或密码不能为空" in error_msg
        self.clear(anxiang_web)
    #usernameisnull
    def test_usernameisnull(self,anxiang_web):
        sleep(2)
        self.login(anxiang_web, "aaa123456", "")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-btn"))).click()
        error_msg = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#err > span"))
        ).text
        assert "用户名或密码不能为空" in error_msg
        self.clear(anxiang_web)

    # @pytest.mark.skip()
    # 正确登录（调用时保持参数一致）
    def test_login_suecss(self, anxiang_web):
        # anxiang_web.driver.find_element(By.CSS_SELECTOR,"body > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a").click()
        #点击注册
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(2) > a"))).click()
        #点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
        self.login(anxiang_web, "aaa123456", "93665678994")
        anxiang_web.driver.forward()
        sleep(3)