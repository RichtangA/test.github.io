'''
切换到借款账户
'''
# from time import sleep
#
# import pytest
# from selenium.webdriver.common.by import By
#
# @pytest.mark.skip("跳过")
# class Test_Switch:
#     # def login(self, anxiang_web, password, username):
#     #     anxiang_web.driver.find_element(By.CSS_SELECTOR, "#keywords").send_keys(username)
#     #     anxiang_web.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
#     #     anxiang_web.driver.find_element(By.CSS_SELECTOR, "#login-btn").click()
#
#     # def test_login_suecss(self, anxiang_web):
#         # 点击登录
#         # anxiang_web.driver.find_element(By.CSS_SELECTOR,
#         #                                 "body > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a").click()
#         # self.login(anxiang_web, "aaa123456", "923456789")
#         # anxiang_web.driver.forward()
#         # sleep(3)
#     def test_switch(self,anxiang_web):
#         anxiang_web.driver.find_element(By.XPATH,"//*[@id='mlayout']/div[2]/div[2]/div[1]/a").click()