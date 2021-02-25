from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestForm():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        """
        案例：
        打开testerhome登录地址：https://testerhome.com/account/sign_in
        输入用户名
        输入密码
        点击'记住'标签
        点击登录，提交表单
        :return:
        """
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        # self.driver.find_element(By.CSS_SELECTOR,'#user_remember_me').click() 不能用，报错
        ele = self.driver.find_element_by_id("user_remember_me")
        action = ActionChains(self.driver)
        action.move_to_element(ele).click().perform()
        # webdriver.ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(5)
