import time

from framework.elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from framework.elements.dropdown_element import DropdownElement


class TopBarLangsElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def get_language_dropdown(self) -> DropdownElement:
        locator = (By.CLASS_NAME, "dropdown")
        dropdown = self.element.find_elements(*locator)[1]
        return DropdownElement(dropdown)


class TopBarElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def get_top_bar_langs(self) -> TopBarLangsElement:
        locator = (By.CLASS_NAME, "top-bar__langs")
        top_bar_langs = self.element.find_element(*locator)
        return TopBarLangsElement(top_bar_langs)

    def select_language(self, language: str) -> None:
        dropdown = self.get_top_bar_langs().get_language_dropdown()
        if dropdown.get_selected_value() == language:
            return
        dropdown.click_element_from_list_and_return_href(language)
