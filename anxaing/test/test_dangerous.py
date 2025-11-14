'''
风险测评
'''
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.skip()
@pytest.mark.order(11)

class Test_dan():
    # 一个都不回答
    def test_fail_null(self, anxiang_web):
        confirm_btn = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div:nth-child(1) > div.icome-charge > div.to-assess > a"))  # 用文本定位最稳定
        )
        confirm_btn.click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > div:nth-child(3) > a"))).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#xubox_layer1 > div.xubox_main > span.xubox_botton > a.xubox_yes.xubox_botton2"))
        ).click()
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#xubox_layer2 > div.xubox_main > span.xubox_setwin > a"))
        ).click()
        #确定按钮
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 " /html/body/div/div/div[2]/form/div[2]/input"))
        ).click()
        sleep(2)
    #回答不完全
    def test_fail_notall(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(1) > div > label:nth-child(2) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 " /html/body/div/div/div[2]/form/div[2]/input"))
        ).click()
        sleep(2)
    def test_success(self,anxiang_web):

        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(1) > div > label:nth-child(2) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(2) > div > label:nth-child(1) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(3) > div > label:nth-child(1) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(4) > div > label:nth-child(1) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(5) > div > label:nth-child(4) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 " body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(6) > div > label:nth-child(3) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 " body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(7) > div > label:nth-child(2) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "  body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(8) > div > label:nth-child(3) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 " body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(9) > div > label:nth-child(1) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 " body > div > div > div.risk-pagecontent.ng-scope > form > ul > li:nth-child(10) > div > label:nth-child(2) > input"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 " /html/body/div/div/div[2]/form/div[2]/input"))
        ).click()
        sleep(2)
        WebDriverWait(anxiang_web.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#mlayout > div.conbox.t20.fn-clear.user-cont > div.user-content.fr > div > div > h2 > span.close"))
        ).click()
        # WebDriverWait(anxiang_web.driver, 5).until(
        #  EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div > div > div.risk - pagecontent.ng - scope > form > div.frombtn > input"))
        #  ).click()
