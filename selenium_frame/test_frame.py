from selenium_frame.base import Base


class TestFrame(Base):
    def test_frame(self):
        """
        frame网页：https://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols
        打开包含frame的web页面：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        打印'请拖拽我'元素的文本
        打印'点击运行'元素的文本
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # self.driver.switch_to.frame("iframeResult")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()
        # self.driver.switch_to_default_content()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
