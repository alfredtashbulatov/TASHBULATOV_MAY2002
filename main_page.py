from time import sleep
from selenium.webdriver.common.by import By
import allure


class Main_Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.sibdar-spb.ru/")

    @allure.title("Добавление товара в корзину")
    def add_in_basket(self):
        with allure.step("Скрол страницы до нужного элемента"):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
                )
            element = self.driver.find_element(
                By.CSS_SELECTOR,
                'button[attr_item="Рыжики солёные"]')
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", element)
            sleep(5)
        with allure.step("Клик по кнопке 'В корзину'"):
            self.driver.find_element(
                By.CSS_SELECTOR,
                'button[attr_item="Рыжики солёные"]'
                ).click()
            sleep(5)

    @allure.title("Добавление количества товара в корзине")
    def plus_goods_in_basket(self):
        with allure.step("Вызвать метод для\
                         добавления товара в корзину"):
            self.add_in_basket()
        with allure.step("Переход в корзину корзину'"):
            self.driver.find_element(
                By.CSS_SELECTOR,'span[class="count_bask_right"]'
                ).click()
            sleep(2)
        with allure.step("Клик по кнопке  '+'"):
            self.driver.find_element(
                By.XPATH,
                '/html/body/div[3]/div[1]/form/div[1]/div/div[2]/div[1]/div[2]/span[2]'
                ).click()
            sleep(3)

    @allure.title("Удаление товара из корзины")
    def delete_goods_from_basket(self):
        with allure.step("Скрол страницы до нужного элемента"):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            element = self.driver.find_element(
                By.CSS_SELECTOR,
                'button[attr_item="Грибная икра из опят"]')
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", element)
            sleep(3)
        with allure.step("Клик по кнопке 'В корзину'"):
            self.driver.find_element(
                By.XPATH,
                '/html/body/section[2]/div/div/div[2]/div[1]/div[4]/div[3]/button'
                ).click()
            sleep(3)
        with allure.step("Переход в корзину корзину'"):
            self.driver.find_element(
                By.CSS_SELECTOR,
                'span[class="count_bask_right"]'
                ).click()
            sleep(1)
        with allure.step("Клик по кнопке удаления товара из корзины"):
            self.driver.find_element(
                By.XPATH,
                '/html/body/div[3]/div[1]/form/div[1]/div/div[2]/button/img'
                ).click()
            sleep(1)
    