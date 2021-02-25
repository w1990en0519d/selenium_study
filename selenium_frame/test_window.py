from time import sleep

from selenium_frame.base import Base

"""
打开百度首页
点击登录
弹窗中点击立即注册，输入用户名和手机号
返回刚才的登录页，点击登录
输入用户名和密码，点击登录
"""


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)  # 打印当前窗口的句柄
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)  # 打印当前窗口的句柄
        print(self.driver.window_handles)  # 打印所有窗口的句柄
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("15800002368")
        sleep(2)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_passwaord")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)
