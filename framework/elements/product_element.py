from framework.elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from framework.elements.dropdown_element import DropdownElement
from selenium.webdriver.common.by import By


class ProductElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def get_dropdown(self) -> DropdownElement:
        dropdown = self.element.find_element(By.CLASS_NAME, "dropdown")
        return DropdownElement(dropdown)
