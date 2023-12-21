from typing import Union

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from framework.elements.aside_element import AsideElement
from framework.elements.top_bar_element import TopBarElement
from framework.pages.base_page import BasePage


class KICSforNetworkPage(BasePage):
    """Набор методов для работы со страницей https://support.kaspersky.com/KICSforNetworks"""
    def __init__(self, driver: Union[Chrome, Edge, Firefox], wait: WebDriverWait, url: str):
        super().__init__(driver, wait, url)

    def get_aside(self) -> AsideElement:
        locator = (By.CLASS_NAME, "aside")
        aside = self.wait.until(EC.presence_of_element_located(locator))
        return AsideElement(aside)

    def get_top_bar(self) -> TopBarElement:
        locator = (By.CLASS_NAME, "top-bar__links-box")
        top_bar = self.wait.until(EC.presence_of_element_located(locator))
        return TopBarElement(top_bar)

    def with_english_language(self):
        self.get_top_bar().select_language("English")

    def with_russian_language(self):
        self.get_top_bar().select_language("Русский")

    def get_ram_information_when_sensor_functions(self) -> str:
        locator = (By.CLASS_NAME, "listbullet2")
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        # Через XPATH сделать не получилось, поэтому находим таким образом, пусть и ненадёжно
        # При XPATH ловила ошибку "элемент не существует", пришлось использовать presence_of_all_elements_located
        return elements[6].text
