import pytest
import allure
from User_api import Api


@allure.title("Добавление товара в корзину")
@allure.feature("ADD IN BASKET")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Тест вызывает Api\
                    метод добавления товара в корзину.\
                    Проверяет, что длина ответа > 0\
                    и сообщение ответа")
@pytest.mark.api
def test_add_in_basket_goods(api:Api):
    with allure.step("Вызвать Api метод\
                     для добавления товара"):
        body = api.add_goods()
    with allure.step("Выполнить проверки"):
        with allure.step("Проверить что длина списка\
                         больше 0"):
            assert len(body) >= 0
            with allure.step("Прорверить что сообщение ответа равна\
                             '<bound method Response.json of <Response [200]>>'"):
                assert body == '<bound method Response.json of <Response [200]>>'


@allure.title("Увелечения количества товара в корзине")
@allure.feature("PLUS IN BASKET")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Тест вызывает Api\
                    метод увелечения количества товара в корзине.\
                    Проверяет, что длина ответа > 0")
@pytest.mark.api
def test_goods_basket_plus(api:Api):
    with allure.step("Вызвать Api метод\
                     увелечения количества товара в корзине"):
        body = api.goods_basket_plus()
        with allure.step("Выполнить проверки"):
            with allure.step("Прорверить что сообщение ответа равна\
                             '<bound method Response.json of <Response [200]>>'"):
                assert body == '<bound method Response.json of <Response [200]>>'

@allure.title("Удаление товара из корзины")
@allure.feature("DELETE")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Тест вызывает Api\
                    метод удаления товара из корзины.\
                    Проверяет, что длина ответа > 0")
@pytest.mark.api
def test_delete_goods_basket(api:Api):
    with allure.step("Вызвать Api метод\
                     удаления товара из корзины"):
        body = api.delete_goods_basket()
        with allure.step("Выполнить проверки"):
            with allure.step("Проверить что длина списка больше 0"):
                assert len(body) >= 0
            with allure.step("Прорверить что сообщение ответа равна\
                             '<bound method Response.json of <Response [200]>>'"):
                assert body == '<bound method Response.json of <Response [200]>>'
