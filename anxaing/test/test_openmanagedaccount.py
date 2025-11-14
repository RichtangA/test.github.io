from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
开户测试
'''
# @pytest.mark.skip(reason="暂时不运行这个测试类")
@pytest.mark.order(3)
class Testopenaccount:

    def openaccount(self,anxiang_web):

        # 点击开通账户按钮进入开通资金托管界面
        anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                    "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div.user-open.fn-clear.ng-scope > div > a").click()
       #输入信息
    def input(self,anxiang_web,name,ID):
        #输入姓名
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#safeName > div:nth-child(2) > input"))
        ).send_keys(name)

        # #输入身份证号
        WebDriverWait(anxiang_web.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#safeName > div:nth-child(3) > input"))
        ).send_keys(ID)
        #点击确认提交按钮
        anxiang_web.driver.find_element(By.CSS_SELECTOR,"#safeName > div:nth-child(5) > div > input").click()
    def clear(self,anxiang_web):
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#safeName > div:nth-child(2) > input").clear()
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#safeName > div:nth-child(3) > input").clear()

    #身份证号码为空
    def test_IDisnull(self,anxiang_web):
        self.openaccount(anxiang_web)
        self.input(anxiang_web,"张三","")
        t=WebDriverWait(anxiang_web.driver,10).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR,"#safeName > div:nth-child(3) > label.dy-validation > span"))
       ).text
        assert t=="不能为空"
        self.clear(anxiang_web)
        # 姓名为空

    def test_nameisnull(self, anxiang_web):

        self.input(anxiang_web, "", "12345678")
        anxiang_web.driver.implicitly_wait(5)
        t = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#safeName > div:nth-child(2) > label.dy-validation > span"))
        ).text
        assert t == "不能为空"
        self.clear(anxiang_web)
    #身份证号姓名都为空
    def test_Allisnull(self,anxiang_web):
        self.input(anxiang_web,"","")
        assert anxiang_web.driver.find_element(By.CSS_SELECTOR,"#safeName > div:nth-child(2) > label.dy-validation > span").text=="不能为空"
        assert anxiang_web.driver.find_element(By.CSS_SELECTOR,"#safeName > div:nth-child(3) > label.dy-validation > span").text=="不能为空"
        self.clear(anxiang_web)
        #输入姓名为全数字
    def test_nameisnum(self, anxiang_web):
        self.input(anxiang_web, "123456", "123456")
        assert anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                               "#safeName > div:nth-child(2) > label.dy-validation > span").text == "输入姓名格式有误"
        self.clear(anxiang_web)
    #输入姓名全部为字母
    def test_nameischar(self, anxiang_web):
        self.input(anxiang_web, "aaaa", "123456")
        assert anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                               "#safeName > div:nth-child(2) > label.dy-validation > span").text == "输入姓名格式有误"
        self.clear(anxiang_web)
    #名字只输入一个字
    def test_nameonlyone(self, anxiang_web):
        self.input(anxiang_web, "张", "123456")
        assert anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                               "#safeName > div:nth-child(2) > label.dy-validation > span").text == "输入姓名格式有误"
        self.clear(anxiang_web)

    #身份证号码已存在
    def test_exit(self,anxiang_web):
        self.input(anxiang_web,"张三",123456)
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#safeName > div:nth-child(5) > div > label"))
        ).text
        assert text=="身份证号码已存在"
        self.clear(anxiang_web)
    #     # 身份证号码已存在
    # def test_success(self, anxiang_web):
    #     self.input(anxiang_web, "张三", 111111111111)

#点击立即开通,开通资金托管
    # @pytest.mark.skip()
    def test_success(self, anxiang_web):
        self.input(anxiang_web, "张三", 93665678994)
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "#successForm > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            lambda driver: len(driver.window_handles) == 2
        )
        all_handles = anxiang_web.driver.window_handles
        anxiang_web.driver.switch_to.window(all_handles[-1])
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"body"))
        ).text
        # 切换到第一个窗口句柄（返回第一个界面）
        anxiang_web.driver.switch_to.window(all_handles[0])
    #返回用户中心
    def test_return_centrl(self,anxiang_web):
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#xuboxPageHtml1 > div > div > a.closeWinow"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li.last.regFinish2 > a.logout"))).click()
        # 点击注册
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "body > div > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(2) > a"))).click()
        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#keywords"))).send_keys("923456789")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys("aaa123456")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-btn"))).click()