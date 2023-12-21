from abc import ABC
from typing import Union

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(ABC):
    """Базовый класс для всех страниц. При создании страницы происходит переход на её url и ожидание загрузки"""

    def __init__(self, driver: Union[Chrome, Firefox, Edge], wait: WebDriverWait, url: str):
        self.driver = driver
        self.wait = wait
        self.driver.get(url)
        self.wait_for_page_load()

    # https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
    def wait_for_page_load(self):
        old_page = self.driver.find_element(By.TAG_NAME, 'html')
        yield
        self.wait.until(EC.staleness_of(old_page))
