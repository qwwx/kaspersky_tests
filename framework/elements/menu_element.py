from framework.elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from framework.elements.menu_item_element import MenuItemElement


class MenuElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)

    def get_menu_item(self, text: str) -> MenuItemElement:
        # Текст почему-то был выделен пробелами с начала и конца, поэтому указала их здесь, чтобы не смущали
        locator = (By.XPATH, f'//a[text()=" {text} "]/parent::*')
        # Распаковываем локатор, т.к. ожидаются 2 параметра
        menu_item = self.element.find_element(*locator)
        return MenuItemElement(menu_item)

    def get_and_toggle_menu_item(self, text: str) -> MenuItemElement:
        element = self.get_menu_item(text)
        if not element.is_toggled():
            element.toggle()
        return element
