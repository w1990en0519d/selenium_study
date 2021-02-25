from time import sleep

from selenium import webdriver

from selenium_js.base import Base


class TestFile(Base):
    def test_file_upload(self):
        """
        文件上传案例：
        打开百度秃瓢网址：https://image.baidu.com/
        识别上传按钮
        点击上传按钮
        将本地的图片文件上传
        :return:
        """
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        sleep(3)
        self.driver.find_element_by_id("stfile").send_keys("D:\selenium\selenium_file_alert\测试.jpg")
        sleep(5)
