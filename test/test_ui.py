import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from main_page import Main_Page as MP


@allure.title("Добавление товара в корзину")
@allure.description("Тест вызывает метод\
                    для добавления товара\
                    в корзину")
@allure.feature("ADD GOODS")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.ui
def test_add_in_basket(driver: WebDriver):
    with allure.step("Передать браузер в конструктор класса\
                     Main_Page"):
        res = MP(driver)
    with allure.step("Вызвать метод для\
                     добавления товара в корзину"):
          res.add_in_basket()

@allure.title("Прибовление количества товара в корзине")
@allure.description("Тест вызывает метод\
                    для прибавления количества\
                    добавленного товара\
                    в корзине")
@allure.feature("PLUS GOODS")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.ui
def test_plus_goods_in_basket(driver: WebDriver):
    with allure.step("Передать браузер в конструктор класса\
                     Main_Page"):
        plus = MP(driver)
    with allure.step("Вызвать метод для\
                     прибовления количества товара в корзине"):
        plus.plus_goods_in_basket()

@allure.title("Удаление товара из корзины")
@allure.description("Тест вызывает метод\
                    для удаления товара\
                    из корзины")
@allure.feature("DELETE GOODS")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.ui
def test_dellete_from_basket(driver: WebDriver):
    with allure.step("Передать браузер в конструктор класса\
                     Main_Page"):
        dell = MP(driver)
    with allure.step("Вызвать метод для\
                     удаления товара из корзины"):
        dell.delete_goods_from_basket()