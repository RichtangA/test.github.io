from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.skip()
@pytest.mark.order(1)
class Testregis:
    # @pytest.mark.skip()
    def regis(self,anxiang_web,iphone,password,verifycode,phone_code):
        # 打开注册界面
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "body > div > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(2) > a"))
        ).click()

        # 输入手机号码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#phone").send_keys(iphone)
        # 输入登录密码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        # 输入验证码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#verifycode").send_keys(verifycode)
        # 点击发送验证码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#get_phone_code").click()
        # 输入短信验证码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#phone_code").send_keys(phone_code)
        sleep(2)
        # 点击注册
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#reg_form > div.reg-cont > div:nth-child(6) > input").click()
        # 邀请个人用户名
        # 点击邀请个人用户名
        # anxiang_web.driver.find_element(By.CSS_SELECTOR," #reg_form > div.reg-cont > div.lg-item.fn-clear.ng-scope > a > i").click()
        # anxiang_web.driver.find_element(By.CSS_SELECTOR,"#invite_phone").send_keys("柯大贵")



    #错误注册--未勾选协议
    def test_regis_fail(self,anxiang_web):
        sleep(2)
        # 打开注册界面
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "body > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(2) > a"))
        ).click()
        # 输入手机号码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("123456789")
        # 输入登录密码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("aaa123456")
        # 输入验证码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#verifycode").send_keys("8888")
        # 点击发送验证码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#get_phone_code").click()
        # 输入短信验证码
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#phone_code").send_keys("666666")
        sleep(2)
        # 取消协议勾选
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#dy_server").click()
        # 点击注册
        anxiang_web.driver.find_element(By.CSS_SELECTOR, "#reg_form > div.reg-cont > div:nth-child(6) > input").click()

        assert anxiang_web.driver.find_element(By.CSS_SELECTOR,"#reg_form > div.reg-cont > div:nth-child(7) > span").text=="请同意我们的条款"

#     @pytest.mark.skip()
# #短信验证码过期
#     def test_regis_fail_message(self,anxiang_web):
#
#         # 点击登录
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,
#                                         "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a").click()
#         sleep(3)
#         # 再点击注册
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,
#                                         "body > div > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(2) > a").click()
#         #输入手机号码
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#phone").send_keys("993456789")
#         #输入登录密码
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#password").send_keys("aaa123456")
#         #输入验证码
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#verifycode").send_keys(8888)
#         #点击发送验证码
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#get_phone_code").click()
#         sleep(61)
#         #输入短信验证码
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#phone_code").send_keys(666666)
#         anxiang_web.driver.implicitly_wait(301)
#         #点击注册
#         anxiang_web.driver.find_element(By.CSS_SELECTOR,"#reg_form > div.reg-cont > div:nth-child(6) > input").click()
#         sleep(3)
#         anxiang_web.driver.save_screenshot("screenshots/loginerror_messguoqi.png")  # 保存到screenshots文件夹下


#与短信验证码不一致
    def test_regis_fail_messagefail(self, anxiang_web):
        sleep(2)
        login_btn=anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a")
        WebDriverWait(anxiang_web.driver,10).until(
            EC.element_to_be_clickable(login_btn)
        ).click()
        self.regis(anxiang_web,"992456789","aaa123456","8888","666667")

        # 保存截图（支持相对路径或绝对路径）
        anxiang_web.driver.save_screenshot("screenshots/loginerror_meaaasagefail.png")  # 保存到screenshots文件夹下
#     #短信验证码为空
    def test_regis_fail_messagenull(self, anxiang_web):
        sleep(2)
        # 点击登录
        anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a").click()
        self.regis(anxiang_web,"992456789","aaa123456","8888","")
        # 保存截图（支持相对路径或绝对路径）
        anxiang_web.driver.save_screenshot("screenshots/loginerror_meaaasagenull.png")  # 保存到screenshots文件夹下
#
#图片验证码为空
    def test_regis_fail_picturenull(self, anxiang_web):
        sleep(2)
            # 点击登录
        anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                            "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a").click()
        self.regis(anxiang_web,"992456789","aaa123456","","666666")
        # 保存截图（支持相对路径或绝对路径）
        anxiang_web.driver.save_screenshot("screenshots/loginerror_meaaasagenull.png")  # 保存到screenshots文件夹下
#图片验证码过期
    @pytest.mark.skip()
    def test_regis_fail_picturenull(self, anxiang_web):
        sleep(2)
        # 点击登录
        anxiang_web.driver.find_element(By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a").click()

        self.regis(anxiang_web,"992456789","aaa123456","8888","666666")
        # 保存截图（支持相对路径或绝对路径）
        anxiang_web.driver.save_screenshot("screenshots/loginerror_meaaasagenull.png")  # 保存到screenshots文件夹下
#注册失败，注册密码6位纯数字
    def test_zhucefail_mimacount6(self, anxiang_web):
        sleep(2)
        WebDriverWait(anxiang_web.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))
        ).click()
        self.regis(anxiang_web,"923456789","111111","8888","666666")

# 注册失败，注册密码长度5位
    def test_zhucefail_mimacount5(self, anxiang_web):
        sleep(2)
        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
        self.regis(anxiang_web,"923456789","11111","8888","666666")
    # 注册失败，注册密码6位纯字母
    def test_zhucefail_mimacount(self,anxiang_web):
        sleep(2)
        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
        self.regis(anxiang_web,"923456789","aaa123456","8888","666666")

        # 注册失败，注册密码17位

    def test_zhucefail_mimacount17(self, anxiang_web):
        sleep(2)

        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
        self.regis(anxiang_web,"923456789","aaaaaaaa111111111","8888","666666")

    #注册失败，手机号码为空
    def test_rejis_fail_numbernull(self, anxiang_web):
        sleep(2)
        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()


        self.regis(anxiang_web,"","111111","8888","666666")


    # @pytest.mark.skip()
    #正确注册
    def test_regis_success(self,anxiang_web):
        sleep(2)
        # 点击登录
        WebDriverWait(anxiang_web.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        "body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li:nth-child(1) > a"))).click()
        self.regis(anxiang_web,"93665678994","aaa123456","8888","666666")
#恢复原页面
    def test_renew(self,anxiang_web):
        exit=anxiang_web.driver.find_element(By.CSS_SELECTOR,"body > div.ng-scope > div.header > div > div.header-top > div > div.sub-nav.fr > li.last.regFinish2 > a.logout")
        WebDriverWait(anxiang_web,10).until(
            EC.element_to_be_clickable(exit)
        ).click()
