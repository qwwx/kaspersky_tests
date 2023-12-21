from typing import Union

from framework.elements.product_element import ProductElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.support.wait import WebDriverWait


class HelpPage(BasePage):
    """Набор методов для работы со страницей https://support.kaspersky.com/help/"""
    def __init__(self, driver: Union[Chrome, Firefox, Edge], wait: WebDriverWait):
        super().__init__(driver, wait, "https://support.kaspersky.com/help/")

    def get_product(self, product_name: str) -> ProductElement:
        locator = (By.XPATH, f'//span[text()="{product_name}"]/ancestor::div[@class="product"][1]')
        product = self.wait.until(EC.presence_of_element_located(locator))
        return ProductElement(product)

    def click_product_version_and_return_link_to_next_page(self, product_name: str, product_version: str) -> str:
        """Метод, отвечающий за переход на страницу продукта с выбранной версией"""
        product = self.get_product(product_name)
        dropdown = product.get_dropdown()
        href = dropdown.click_element_from_list_and_return_href(product_version)
        return href

