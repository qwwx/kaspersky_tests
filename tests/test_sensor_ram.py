from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from framework.pages.KICSforNetworks_page import KICSforNetworkPage
from framework.pages.help_page import HelpPage

chrome_options = webdriver.ChromeOptions()
# Добавила, т.к. иначе не запускалось с ошибкой "DevToolsActivePort file doesn't exist"
# https://stackoverflow.com/questions/50642308/webdriverexception-unknown-error-devtoolsactiveport-file-doesnt-exist-while-t
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
# Эти две опции нужны, чтобы аргумент "--headless" нормально работал (иначе тесты жаловались, что элемент не кликабельный)
# https://stackoverflow.com/questions/63783983/element-not-interactable-in-selenium-chrome-headless-mode
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException))

# Пометки в тестах оставляю, чтобы раскрыть свою идею, почему реализовала именно так
# При написании кода в реальном проекте, естественно, не стала бы каждую строчку комментировать
# Подробно распишу только первый тест, т.к. остальные аналогично работают, в них укажу только на отличия

def test_check_sensor_ram_v40():
    # Одна из идей, которых хотелось добиться этой строкой - убрать знание об адресе страницы при написании тестов
    # (тестировщики, как я думаю, вряд ли везде ссылку указывают)
    # Таким образом, при создании страницы мы в коде сразу переходим на неё, и можем взаимодействовать со страницей
    help_page = HelpPage(driver, wait)

    # Этот метод объединил в себе сразу несколько действий, я просто точно не знаю, как принято у вас делать
    # Поэтому сделала двумя способами (второй ниже будет)
    # Список действий: найти продукт, выбрать нужную версию, кликнуть и перейти на страницу
    # При этом в конце мы получаем url страницы, куда хотим перейти, чтобы создать следующую страницу с этим url-ом
    href = help_page.click_product_version_and_return_link_to_next_page("Industrial CyberSecurity for Networks", "4.0")

    # Дожидаемся загрузки страницы KICSforNetwork, хотим получить доступ к методам работы с ней
    kics_page = KICSforNetworkPage(driver, wait, href)

    # Устанавливаем английскую версию страницы
    # Здесь, думаю, можно расписать, каким образом старалась выделять объекты для тестирования
    # Через devtools заходила на элемент и искала наиболее общего родителя (для этой страницы им являлся top_bar)
    # Идея в том, чтобы сразу выделить общего родителя, и при необходимости дальнейшего написания тестов
    # меньше кода переписывать. Например, если бы захотелось тестировать здесь не только переключение языка, но и
    # смену версии, код поиска общего родителя у нас уже есть, и нужно было бы взять не второй dropdown, а первый
    # Сам dropdown, кстати, получилось переиспользовать в двух местах
    kics_page.with_english_language()

    # Здесь сделала вторым способом (явно расписала набор элементов, с которыми нужно взаимодействовать)
    # Идея, почему появились aside -> menu -> menu item -> content, аналогична комментарию у строки смены языка
    # (выделяем общего родителя и от него спускаемся к более мелким элементам)
    kics_page\
        .get_aside()\
        .get_menu()\
        .get_and_toggle_menu_item("About Kaspersky Industrial CyberSecurity for Networks")\
        .select_content("Hardware and software requirements")

    # Тут было не совсем понятно условие "найдите элемент по имени и сравните с заданным текстом"
    # Как будто если нашли, сравнивать с текстом бессмысленно?
    # Поэтому решила вместо этого найти элемент по локатору расположения на странице, и сравнивать уже его текст
    # Однако, если захотим добавить что-то новое перед ним (или перенести в другое место), тест придётся чинить
    text = kics_page.get_ram_information_when_sensor_functions()
    assert text == "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"


def test_check_sensor_ram_v30():
    help_page = HelpPage(driver, wait)
    # Всё, что поменялось в этом тесте - вместо "4.0" стало "3.0"
    href = help_page.click_product_version_and_return_link_to_next_page("Industrial CyberSecurity for Networks", "3.0")

    kics_page = KICSforNetworkPage(driver, wait, href)
    kics_page.with_english_language()

    kics_page\
        .get_aside()\
        .get_menu()\
        .get_and_toggle_menu_item("About Kaspersky Industrial CyberSecurity for Networks")\
        .select_content("Hardware and software requirements")

    text = kics_page.get_ram_information_when_sensor_functions()
    # И в конце сравниваем с другим значением
    assert text == "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."


def test_check_sensor_ram_v40_rus():
    help_page = HelpPage(driver, wait)
    href = help_page.click_product_version_and_return_link_to_next_page("Industrial CyberSecurity for Networks", "4.0")

    kics_page = KICSforNetworkPage(driver, wait, href)
    # Всё, что поменялось в этом тесте - выбрали другой язык (русский)
    kics_page.with_russian_language()

    # И далее работаем с русскими текстами
    kics_page \
        .get_aside() \
        .get_menu() \
        .get_and_toggle_menu_item("О Kaspersky Industrial CyberSecurity for Networks") \
        .select_content("Аппаратные и программные требования")

    text = kics_page.get_ram_information_when_sensor_functions()
    assert text == "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"
