import pytest
import allure
from selenium import webdriver
from User_api import Api


@allure.title("Фикстура URL для API-тестов")
@pytest.fixture(scope="session")
def api():
    return Api("https://www.sibdar-spb.ru")

@allure.title("Фикстура для Браузера для Ui-тестов")
@pytest.fixture
def driver():
    with allure.step("Записать в переменную {browser},\
                     браузер 'Microsoft Edge'"):
        browser = webdriver.Edge()
    with allure.step("Задать ожидание браузера"):
        browser.implicitly_wait(6)
    with allure.step("Задать размеры окна браузера"):
        browser.maximize_window()

    with allure.step("Вернуть браузер"):
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()
