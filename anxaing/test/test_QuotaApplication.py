'''
个人借款申请
'''
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# @pytest.mark.skip()
@pytest.mark.order(6)
class Test_QuotaApplication():
    def Quota(self,anxiang_web):
        #悬停
        setting_btn=anxiang_web.driver.find_element(By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(3) > a")
        actions=ActionChains(anxiang_web.driver)
        actions.move_to_element(setting_btn).perform()
        sleep(1)
        #找到个人借款
        jiekuan = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#mlayout > div.header.fn-clear > div.header-cont > div > ul > li:nth-child(3) > ul > li:nth-child(1) > a")
        ))
        #点击个人借款
        jiekuan.click()

    #信用借款
    def xinyong(self,anxiang_web):
# 跳转到了另一个页面
        allhandler=anxiang_web.driver.window_handles
        anxiang_web.driver.switch_to.window(allhandler[-1])
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div.conbox.ng-scope > div > ul > li:nth-child(1) > dl > dd:nth-child(5) > a"))
        ).click()


# 输入借款信息封装/失败项目名称为空
    def test_inputmessage_itemnull(self, anxiang_web):
        self.Quota(anxiang_web)
        self.xinyong(anxiang_web)
        allhandles = anxiang_web.driver.window_handles
        anxiang_web.driver.switch_to.window(allhandles[-1])
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(5) > input"))
        ).send_keys("")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(5)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("200")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).send_keys("4")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(12) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(12) > select > option:nth-child(8)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,  "#tender_amount_min"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_min"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_min > option:nth-child(3)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,  "#tender_amount_max"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_max > option:nth-child(4)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrow_contents"))
        ).send_keys("测试")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div.u-item.verify-group.fn-clear.verify-code > input"))
        ).send_keys("8888")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text=WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(5) > label.dy-validation > span"))
        ).text
        assert text=="不能为空"
    #借款用途为空
    def test_inputmessage_usenull(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(5) > input"))
        ).send_keys("1")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(1)"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,5).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(6) > label.dy-validation > span"))
       ).text
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        assert text=="不能为空"

    #借款金额为空
    def test_countisnull(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(7) > label.dy-validation > span"))
        ).text
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        assert text=="不能为空"
#借款金额不为50的倍数
    def test_countisfloat(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("200.5")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(7) > label.dy-validation > span"))
        ).text
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        assert text=="请输入50的倍数"
    #借款金额少于50
    def test_countless50(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("20")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(7) > label.dy-validation > span"))
        ).text
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        assert text=="不能小于最低借款金额"
#借款金额大于最高
    def test_countmore(self,anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("2000000")
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(7) > label.dy-validation > span"))
        ).text
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        assert text=="不能大于最高借款金额"

        # 借款金额大于最高额度
    def test_countmorelimit(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("100000")

        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        # text = WebDriverWait(anxiang_web.driver, 5).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "//*[@id='xubox_layer6']/div[1]/div/span[2]"))
        # ).text
        # assert text == "可用信用额度小于借款金额"

    #年利率为空
    def test_lenynull(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("100")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).send_keys("")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(8) > label.dy-validation > span"))
        ).text
        assert  text=='不能为空'
        # 年利率低
    def test_lenylesslimit(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("100")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).send_keys("2")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(8) > label.dy-validation > span"))
        ).text
        assert  text=='年利率不能小于最低限制'
        # 年利率低

    def test_lenymorelimit(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(6) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(7) > input"))
        ).send_keys("100")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).send_keys("11")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text = WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > label.dy-validation > span"))
        ).text
        assert text == '年利率不能大于最高限制'
        #借款期限为空
    def test_lenylimitnull(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).clear()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(8) > input"))
        ).send_keys("4")
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(11) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(11) > select > option:nth-child(1)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(11) > label.dy-validation > span"))
        ).text
        assert text=="不能为空"
    #筹标期限为空
    def test_choubiaolimitnull(self, anxiang_web):
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(11) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(11) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(12) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(12) > select > option:nth-child(1)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(12) > label.dy-validation > span"))
        ).text
        assert text=="不能为空"
#最低投资金额为空
    def test_investcountnull(self, anxiang_web):
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(12) > select"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrowPublish > div:nth-child(12) > select > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_min"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_min > option:nth-child(1)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text=WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrowPublish > div:nth-child(13) > label.dy-validation > span"))
        ).text
        assert text=="不能为空"

    # 最低投资金额为空
    def test_investhcountnull(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_min"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_min > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_max"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_max > option:nth-child(1)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text = WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(14) > label.dy-validation > span"))
        ).text
        assert text == "不能为空"
    #详情描述为空
    def test_detailnull(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_max"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tender_amount_max > option:nth-child(2)"))
        ).click()
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrow_contents"))
        ).clear()
        WebDriverWait(anxiang_web.driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#borrow_contents"))
        ).send_keys("")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        text = WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div:nth-child(16) > div > label > span"))
        ).text
        assert text == "不能为空"
    # 输入借款信息封装/成功
    def test_inputmessage(self, anxiang_web):
        WebDriverWait(anxiang_web.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#borrow_contents"))
        ).send_keys("ceshi")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowPublish > div.u-item.verify-group.fn-clear.verify-code > input"))
        ).send_keys("8888")
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#borrowForm"))
        ).click()