'''
申请借款额度
'''
from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.order(4)
# @pytest.mark.skip
class Test_ApplyLimit():
    #点击借款账户
    def test_switch(self, anxiang_web):
        anxiang_web.driver.find_element(By.XPATH, "//*[@id='mlayout']/div[2]/div[2]/div[1]/a").click()
    # 点击申请额度
    def test_applylimit(self,anxiang_web):
        apply = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-menu.fl.ng-scope > div.menu > div:nth-child(2) > dl > dd:nth-child(4) > a")
                                             ))
        apply.click()
#封装申请
    def apply(self,anxiang_web,amount,shuoming,yanzhengma):
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#amount_account"))
        ).send_keys(Keys.CONTROL, 'a')
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#amount_account"))
        ).send_keys(Keys.DELETE)
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#amount_account"))
        ).send_keys(amount)
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mamountapply > div:nth-child(3) > textarea"))
        ).send_keys(Keys.CONTROL, 'a')
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mamountapply > div:nth-child(3) > textarea"))
        ).send_keys(Keys.DELETE)
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mamountapply > div:nth-child(3) > textarea"))
        ).send_keys(shuoming)
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#verifycode"))
        ).send_keys(Keys.CONTROL,'a')
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#verifycode"))
        ).send_keys(Keys.DELETE)
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#verifycode"))
        ).send_keys(yanzhengma)
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mamountapply > div:nth-child(5) > input"))
        ).click()


#申请失败验证码为空
    def test_applycount_fail_Captcha(self,anxiang_web):
        self.apply(anxiang_web, 10000, "测试", "")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#mamountapply > div:nth-child(4) > label.error"))
        ).text
        assert text=="验证码不能为空"
    @pytest.mark.skip()
#申请失败  验证码过期
    def test_applycount_fail_Captchaexpire(self, anxiang_web):
        self.apply(anxiang_web, 10000, "测试", "")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mamountapply > div:nth-child(4) > label.error"))
        ).text
        assert text == "验证码不能为空"
#     # @pytest.mark.skip()
# #申请失败申请500个字(success)
#     def test_applycount_fail_applycount(self, anxiang_web):
#
#         self.apply(anxiang_web, 10000, "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "8888")


        # 申请失败申请额度为0

    def test_applycount_fail_countis100001(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.apply(anxiang_web, 1000000001,
                   "测试",
                   "8888")
        text = WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mamountapply > div:nth-child(2) > label.error"))
        ).text
        assert text == "申请额度不能超过1亿"
#申请额度为空
    def test_applycount_fail_countisnull(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.apply(anxiang_web, "",
                   "测试",
                   "8888")
        text = WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#mamountapply > div:nth-child(2) > label.error"))
        ).text
        assert text == "申请额度不能为空"

        # 申请额度为非整数
    def test_applycount_fail_countisfloat(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.apply(anxiang_web, 999.9,
                   "测试",
                   "8888")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "#mamountapply > div:nth-child(2) > label.error"))
        ).text
        assert text == "申请额度格式不正确"

        # 申请失败详细说明0个字
    def test_applycount_fail_shuomingcountis0(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(5)
        self.apply(anxiang_web, 0,
                   "",
                   "8888")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "#mamountapply > div:nth-child(3) > label.error")
            )
        ).text
        assert text == "详情说明不能为空"

        # 申请失败申请额度为0

# 申请信用额度成功
#     @pytest.mark.skip
    def test_applycount_success(self,anxiang_web):
        anxiang_web.driver.implicitly_wait(5)

        self.apply(anxiang_web,10000,"测试",8888)
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-top > div > div.sub-nav.fr > li.last > span > a"))
        ).click()
        sleep(10)




