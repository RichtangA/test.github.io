# import time
#
# import pytest
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# 
# '''
#   测试申请金额界面--投资账户
#   '''
# @pytest.mark.skip()
# @pytest.mark.order(7)
# class Testobtainlimit:
#     def test_switch(self, anxiang_web):
#         anxiang_web.driver.find_element(By.XPATH, "//*[@id='mlayout']/div[2]/div[2]/div[1]/a").click()
#     #测试点进申请界面
#
#     def test_ApplicationInterface(self,anxiang_web):
#         #悬停在品质理财上
#         setting_button=anxiang_web.driver.find_element(By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(3) > a > span")
#         # 创建ActionChains对象
#         actions = ActionChains(anxiang_web.driver)
#         # 鼠标移动到元素上（悬停）
#         actions.move_to_element(setting_button).perform()
#         # 定位下拉菜单中的目标元素（例如第一个子项）
#         target_element = anxiang_web.driver.find_element(
#             By.CSS_SELECTOR,
#             "#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(3) > ul > li:nth-child(2) > a"
#         )
#         # 移动到目标元素并点击
#         actions.move_to_element(target_element).click().perform()
#         # 停留2秒，观察悬停效果（下拉菜单会显示）
#         time.sleep(2)
#
#     '''
#     测试在线申请界面
#     '''
#     def test_applyonline(self,anxiang_web):
#         #换句柄
#         all_handles = anxiang_web.driver.window_handles
#         anxiang_web.driver.switch_to.window(all_handles[-1])
#         #填写项目名称
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#applyForm > div > div:nth-child(1) > div > input").send_keys("ceshi")
#         anxiang_web.driver.implicitly_wait(5)
#         #选择省份
#         anxiang_web.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/form/div/div[2]/div/select[1]").click()
#         anxiang_web.driver.implicitly_wait(5)
#         #点击北京市
#         anxiang_web.driver.find_element(By.XPATH,
#                                         "/html/body/div[2]/div/div[1]/form/div/div[2]/div/select[1]/option[2]").click()
#         anxiang_web.driver.implicitly_wait(5)
#         #点击地方
#         anxiang_web.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/form/div/div[2]/div/select[2]").click()
#         anxiang_web.driver.implicitly_wait(5)
#         anxiang_web.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/form/div/div[2]/div/select[2]/option[9]").click()
#         anxiang_web.driver.implicitly_wait(5)
#
#         #输入借款金额
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#applyForm > div > div:nth-child(3) > div > input").send_keys(10000)
#         anxiang_web.driver.implicitly_wait(5)
#
#         #借款期限
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#applyForm > div > div:nth-child(4) > div > input").send_keys(2)
#         anxiang_web.driver.implicitly_wait(5)
#
#         #年化回报率
#         anxiang_web.driver.find_element(By.CSS_SELECTOR," #applyForm > div > div:nth-child(5) > div > input").send_keys(20)
#         anxiang_web.driver.implicitly_wait(5)
#
#         #详细描述
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#applyForm > div > div:nth-child(6) > div > textarea").send_keys("测试")
#         anxiang_web.driver.implicitly_wait(5)
#         #立即提交
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#applyForm > div > div:nth-child(7) > input").click()
#
#







