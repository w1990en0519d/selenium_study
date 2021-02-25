from time import sleep

from selenium_js.base import Base


class TestJS(Base):
    def test_js(self):
        """
        场景：页面显示的数据比较多，需要点击底部的对象，我们就需要
        把鼠标移动到底部，才可以点击对象
        案例一：滑动到浏览器底部或者顶部
        打开百度首页
        输入搜索关键字
        点击搜索后，跳转到搜索结果页
        滑动到底部点击'下一页'
        :return:
        """
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)

    def test_testerhome(self):
        """
        案例二：
        打开网址：https://testerhome.com/
        获取当前页面的title，与性能数据
        关闭网页
        :return:
        """
        self.driver.get("https://testerhome.com/")
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        """
        案例三：
        打开网址：https://www.12306.cn/index/
        修改出发日期为2021-02-25
        打印出发日期
        关闭网址
        :return:
        """
        self.driver.get("https://www.12306.cn/index/")
        sleep(3)
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-02-25'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)
