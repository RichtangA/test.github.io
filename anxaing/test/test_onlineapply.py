'''
在线申请
'''
from telnetlib import EC
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.mark.skip
@pytest.mark.order(7)
class Test_onlineapply():

        def Quota(self, anxiang_web):
            # 悬停
            setting_btn = anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                                          "#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(3) > a")
            actions = ActionChains(anxiang_web.driver)
            actions.move_to_element(setting_btn).perform()
            sleep(1)
            # 找到在线申请
            jiekuan = WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(3) > ul > li:nth-child(2)")
                                                 ))
            # 点击在线申请
            jiekuan.click()
            allhandler = anxiang_web.driver.window_handles
            anxiang_web.driver.switch_to.window(allhandler[-1])
#项目名称
        def itemname(self,anxiang_web,name):
            WebDriverWait(anxiang_web.driver,20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,"#applyForm > div > div:nth-child(1) > div > input"))
            ).send_keys(name)


        def itemcity1(self, anxiang_web):
            WebDriverWait(anxiang_web.driver,20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#applyForm > div > div:nth-child(2) > div > select:nth-child(1)"))
            ).click()
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='applyForm']/div/div[2]/div/select[1]/option[3]"))
            ).click()

        def itemcity2(self, anxiang_web):
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#applyForm > div > div:nth-child(2) > div > select:nth-child(2)"))
            ).click()
            WebDriverWait(anxiang_web.driver,20).until(
                EC.visibility_of_element_located((By.XPATH,
                                            "//*[@id='applyForm']/div/div[2]/div/select[2]/option[5]"))).click()
        def count(self,anxiang_web,num):
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#applyForm > div > div:nth-child(3) > div > input"))
            ).send_keys(num)
        def month(self,anxiang_web,num):
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#applyForm > div > div:nth-child(4) > div > input"))
            ).send_keys(num)
        def percent(self,anxiang_web,num):
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#applyForm > div > div:nth-child(5) > div > input"))
            ).send_keys(num)
        def detail(self,anxiang_web,string):
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#applyForm > div > div:nth-child(6) > div > textarea"))
            ).send_keys(string)

        def clear(self,anxiang_web):
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 "#applyForm > div > div:nth-child(1) > div > input"))
            ).clear()

            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,"#applyForm > div > div:nth-child(2) > div > select:nth-child(1)"))
            ).click()
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[@id='applyForm']/div/div[2]/div/select[1]/option[1]"))
            ).click()
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,  "#applyForm > div > div:nth-child(2) > div > select:nth-child(2)"))
            ).click()
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[@id='applyForm']/div/div[2]/div/select[2]/option"))
            ).click()

            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#applyForm > div > div:nth-child(3) > div > input"))
            ).clear()
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#applyForm > div > div:nth-child(4) > div > input"))
            ).clear()
            WebDriverWait(anxiang_web.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#applyForm > div > div:nth-child(5) > div > input"))
            ).clear()

            WebDriverWait(anxiang_web.driver,20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(6) > div > textarea"))
            ).clear()
        #申请失败-项目名称为空
        def test_onlineapply_fail_itemnull(self,anxiang_web):
            self.Quota(anxiang_web)
            self.itemname(anxiang_web, "")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 2)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            WebDriverWait(anxiang_web.driver,10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
            text=WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div.lg-item.verify-group.fn-clear.has-error > div > label"))
            ).text
            assert text=="不能为空"

#申请失败，项目名称为201个字符
        def test_onlineapply_fail_item51(self, anxiang_web):
            anxiang_web.driver.implicitly_wait(10)
            self.clear(anxiang_web)
            anxiang_web.driver.implicitly_wait(10)

            self.itemname(anxiang_web, "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 2)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            anxiang_web.driver.implicitly_wait(10)

            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
            # text = WebDriverWait(anxiang_web.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.CSS_SELECTOR, "#applyForm > div > div.lg-item.verify-group.fn-clear.has-error > div > label"))
            # ).text
            # assert text == "限制为25个汉字以内"
#申请失败（只选择省）
        def test_onlineapply_fail_onlycity1(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "11")
            self.itemcity1(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 2)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
            text = WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#applyForm > div > div:nth-child(2) > div > label"))
            ).text
            assert text == "不能为空"
#只选择城市
        def test_onlineapply_fail_onlycity2(self, anxiang_web):
            self.clear(anxiang_web)
            anxiang_web.driver.implicitly_wait(5)
            self.itemname(anxiang_web, "11")
            self.itemcity1(anxiang_web)

            WebDriverWait(anxiang_web.driver,10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                            "#applyForm > div > div:nth-child(2) > div > select:nth-child(1)"))
            ).click()
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='applyForm']/div/div[2]/div/select[1]/option[1]"))
            ).click()
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 2)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
        #借款金额为200050
        def test_online_count200050(self,anxiang_web):
            sleep(3)
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 200000050)
            self.month(anxiang_web, 2)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            sleep(3)
        #
        #     WebDriverWait(anxiang_web.driver, 10).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))).click()
        #     assert WebDriverWait(anxiang_web.driver, 10).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR,"#applyForm > div > div:nth-child(3) > div > label"))).text=="不能大于1亿"
        #借款失败，借款金额为空
        def  test_onlineapply_countnull(self,anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, "")
            self.month(anxiang_web, 2)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
#借款期限为0个月
        def test_onlineapply_monthnull(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 0)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
#借款期限为101个月
        def test_onlineapply_month101(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 1001)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "11")
            sleep(5)
        #     anxiang_web.driver.implicitly_wait(10)
        #     WebDriverWait(anxiang_web.driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
        #     ).click()
            # assert WebDriverWait(anxiang_web.driver, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR,"#xubox_layer29 > div.xubox_main > div > span.xubox_msg.xubox_text"))).text=="借款期限超过限制"
      #提交年回报率为负数
        def test_onlineapply_reisfuhsu(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 1)
            self.percent(anxiang_web, -1)
            self.detail(anxiang_web, "11")
            anxiang_web.driver.implicitly_wait(10)
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
        # 提交年回报率为空
        def test_onlineapply_reisnull(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 10)
            self.percent(anxiang_web, "")
            self.detail(anxiang_web, "你好")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
        # 提交年回报率为0
        def test_onlineapply_reis0(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 10)
            self.percent(anxiang_web, 0)
            self.detail(anxiang_web, "你好")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
        # 提交年回报率为非数字
        def test_onlineapply_notnum(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 10)
            self.percent(anxiang_web, "你好")
            self.detail(anxiang_web, "你好")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
#详细描述大于200
        def test_onlineapply_detail202(self, anxiang_web):
            self.clear(anxiang_web)
            self.itemname(anxiang_web, "测试")
            self.itemcity1(anxiang_web)
            self.itemcity2(anxiang_web)
            self.count(anxiang_web, 50)
            self.month(anxiang_web, 10)
            self.percent(anxiang_web, 3)
            self.detail(anxiang_web, "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            WebDriverWait(anxiang_web.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
            ).click()
