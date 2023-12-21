from abc import ABC

from selenium.webdriver.remote.webelement import WebElement


class BaseElement(ABC):
    """Базовый класс для всех элементов, сюда можно добавлять общую логику"""
    def __init__(self, element: WebElement):
        self.element = element

    def click(self):
        self.element.click()
