from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://search.bilibili.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_bi(self):
        self.driver.find_element(By.ID, "search-keyword").send_keys("白月黑羽")
        self.driver.find_element(By.XPATH, '//*[@class="searchBtn"]').click()
        sleep(3)
        # self.driver.find_element(By.XPATH,'//*[@class="video-list clearfix"]//li[last()]//a').click()
        self.driver.find_element(By.CSS_SELECTOR, ".mixin-list li:nth-last-child(1) a").click()
