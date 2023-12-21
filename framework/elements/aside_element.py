from framework.elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from framework.elements.menu_element import MenuElement


class AsideElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def get_menu(self) -> MenuElement:
        locator = (By.CLASS_NAME, "js_menu")
        menu = self.element.find_element(*locator)
        return MenuElement(menu)
