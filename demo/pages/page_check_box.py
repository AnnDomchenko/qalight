from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckBox:
    URL = 'https://demoqa.com/checkbox'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.folder_target_loc = '//span[@class="rct-title"][text()="{}"]//ancestor::span[@class="rct-text"]//button'
        self.folder_loc = '//span[@class="rct-title"][text()]//ancestor::span[@class="rct-text"]//button'

    def open(self) -> None:
        self.driver.get(self.URL)

    def expand(self, folder_name):
        loc = self.folder_target_loc.format(folder_name)
        svg = f'{loc}//*[@class]'
        element = self.driver.find_element(By.XPATH, svg)
        if 'close' in element.get_attribute('class'):
            self.driver.find_element(By.XPATH, loc).click()

    def collapse(self, folder_name):
        loc = self.folder_target_loc.format(folder_name)
        svg = f'{loc}//*[@class]'
        element = self.driver.find_element(By.XPATH, svg)
        if 'open' in element.get_attribute('class'):
            self.driver.find_element(By.XPATH, loc).click()


PageCheckBox('').expand('WorkSpace')
