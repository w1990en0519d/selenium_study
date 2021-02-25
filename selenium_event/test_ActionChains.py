from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        """
        用法一：点击、右键、双击操作
        action = ActionChains(driver)
        action.click(element)
        action.double_click(element)
        action.context_click(element)
        action.perform()
        案例：
        打开页面：http://sahitest.com/demo/clicks.htm
        分别对按钮'click me'，'dbl click me','right click me',执行
        点击，双击，右键操作
        打印上面展示框中的内容
        :return:
        """

        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_rightclick = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        sleep(5)
        action.perform()
        print(self.driver.find_element_by_name("t2").get_attribute("value"))
        sleep(5)

    @pytest.mark.skip
    def test_moveto(self):
        """
        用法二：鼠标移动到某个元素上
        action = ActionChains(driver)
        action.move_to_element(element)
        action.perform()
        案例：
        打开网页：https://www.baidu.com/
        将光标移动到右上角的'设置'上
        :return:
        """

        self.driver.get("https://www.baidu.com/")
        move = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(move)
        sleep(3)
        action.perform()
        self.driver.find_element_by_css_selector("#s-user-setting-menu a:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#se-setting-3 > span:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary").click()
        sleep(5)

    def test_dragdrop(self):
        """
        用法三：将一个元素拖拽到另一个元素的位置上
        action = ActionChains(driver)
        action.drag_and_drop(element_start,element_end).perform()
        或者
        action.click_and_hold(element_start).move_to_element(element_end).re
        lease().perform()
        案例：
        打开网址：http://sahitest.com/demo/dragDropMooTools.htm
        定位两个元素，拖拽原色e1和被拖拽元素e2
        :return:
        """

        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(5)

    def test_keys(self):
        """
        用法四：ActionChains模拟按键方法
        模拟按键有多种方法，能用win32api来实现，能用SendKeys来实现，也可以用selenium的WebElenment对象
        的send_keys()方法来实现，这里ActionChains类也提供了几个模拟按键的方法。
        用法：
        action = ActionChains(driver)
        action.send_keys(Keys.SPACE)
        action.perform()
        案例：
        打开网址：
        定位一个输入框e1
        向输入框e1中输入文字'username'，输入空格
        再输入'tom',再使用删除键删除一个空格
        :return:
        """
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACKSPACE).perform()
        sleep(5)
