import time

from framework.elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class DropdownElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def click_element_from_list_and_return_href(self, element_name: str) -> str:
        self.click()
        # Дожидаемся отрисовки выпадающего списка после нажатия
        time.sleep(0.25)
        elem1: WebElement = self.element.find_element(By.LINK_TEXT, element_name)
        # Получаем атрибут заранее, т.к. после нажатия он изменится, и при попытке получить значение получим ошибку
        href = elem1.get_attribute("href")
        elem1.click()
        return href

    def get_selected_value(self) -> str:
        locator = (By.CLASS_NAME, "dropdown__btn")
        button: WebElement = self.element.find_element(*locator)
        return button.text
