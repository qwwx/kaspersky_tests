from selenium.webdriver.remote.webelement import WebElement
from framework.elements.base_element import BaseElement
from selenium.webdriver.common.by import By


class MenuItemElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def is_toggled(self) -> bool:
        button = self.get_toggle_button()
        return "is-toggled" in button.get_attribute("class")

    def toggle(self) -> None:
        button = self.get_toggle_button()
        button.click()

    def get_toggle_button(self) -> WebElement:
        locator = (By.TAG_NAME, "button")
        return self.element.find_element(*locator)

    def select_content(self, name: str) -> None:
        locator = (By.LINK_TEXT, name)
        # Распаковываем локатор, т.к. ожидаются 2 параметра
        content = self.element.find_element(*locator)
        content.click()
