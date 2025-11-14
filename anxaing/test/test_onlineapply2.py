from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.skip
@pytest.mark.order(8)
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

# 借款期限为非数字
    def test_onlineapply_monthontnum(self, anxiang_web):
        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(10)
        self.itemname(anxiang_web, "测试")
        anxiang_web.driver.implicitly_wait(10)

        self.itemcity1(anxiang_web)
        anxiang_web.driver.implicitly_wait(10)

        self.itemcity2(anxiang_web)
        anxiang_web.driver.implicitly_wait(10)

        self.count(anxiang_web, 50)
        anxiang_web.driver.implicitly_wait(10)

        self.month(anxiang_web, "nh")
        anxiang_web.driver.implicitly_wait(10)

        self.percent(anxiang_web, 3)

        anxiang_web.driver.implicitly_wait(10)

        self.detail(anxiang_web, "11")
        anxiang_web.driver.implicitly_wait(10)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#applyForm > div > div.lg-item.verify-group.fn-clear.has-error > div > label"))
        ).text
        assert text=="请输入大于0的整数"
    def test_onlineapply_detailisnull(self, anxiang_web):
        anxiang_web.driver.implicitly_wait(10)

        self.clear(anxiang_web)
        anxiang_web.driver.implicitly_wait(10)

        self.itemname(anxiang_web, "测试")
        anxiang_web.driver.implicitly_wait(10)

        self.itemcity1(anxiang_web)
        anxiang_web.driver.implicitly_wait(10)

        self.itemcity2(anxiang_web)
        anxiang_web.driver.implicitly_wait(10)

        self.count(anxiang_web, 50)
        anxiang_web.driver.implicitly_wait(10)

        self.month(anxiang_web, 10)
        anxiang_web.driver.implicitly_wait(10)

        self.percent(anxiang_web, 3)
        anxiang_web.driver.implicitly_wait(10)

        self.detail(anxiang_web, "")
        anxiang_web.driver.implicitly_wait(10)
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#applyForm > div > div:nth-child(7) > input"))
        ).click()


