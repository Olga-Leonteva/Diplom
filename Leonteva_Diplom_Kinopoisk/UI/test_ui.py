import allure
import pytest
from selenium import webdriver
from Kinopoisk_UI import Kinopoisk_UI


@allure.epic("UI")
@allure.title("Проверка заголовка на главной странице")
@pytest.mark.test_01_ui
def test_home_page_01():
    with allure.step("Открыть окно Кинопоиск"):
        browser = webdriver.Chrome()
        h_page = Kinopoisk_UI(browser)

    with allure.step("Найти заголовок страницы"):
        title_hp = h_page.home_page()

    with allure.step("Проверить заголовок"):
        assert title_hp == ('Кинопоиск')

    with allure.step("Закрыть браузер"):
        h_page.close_driver()


@allure.title("Быстрый поиск фильма")
@pytest.mark.test_02_ui
def test_quick_search():
    with allure.step("Открыть окно Кинопоиск"):
        browser = webdriver.Chrome()
        film_page = Kinopoisk_UI(browser)

    with allure.step("Ввести названия фильма Мастер и Маргарита"):
        film_page.name_film()

    with allure.step("Просмотреть результат поиска"):
        seach_film = film_page.result_film()

    with allure.step("Проверить поиск"):
        assert seach_film == ("Мастер и Маргарита")

    with allure.step("Закрыть браузер"):
        film_page.close_driver()


@allure.title("Вход в личный кабинет")
@pytest.mark.test_03_ui
def test_button_login():
    with allure.step("Открыть окно Кинопоиск"):
        browser = webdriver.Chrome()
        button_login_page = Kinopoisk_UI(browser)

    with allure.step("Нажать кнопку Войти"):
        button_login_page.click_button_login()

    with allure.step("Найти заголовок страницы"):
        button_login = button_login_page.seach_title_login()

    with allure.step("Проверить заголовок"):
        assert button_login == ("Введите номер телефона")

    with allure.step("Закрыть браузер"):
        button_login_page.close_driver()


@allure.title("Смотреть кино бесплатно")
@pytest.mark.test_04_ui
def test_film_reee():
    with allure.step("Открыть окно Кинопоиск"):
        browser = webdriver.Chrome()
        film_free_page = Kinopoisk_UI(browser)

    with allure.step("Нажать кнопку Смотреть кино бесплатно"):
        film_free_page.click_film_free()

    with allure.step("Найти заголовок страницы"):
        title_film_free = film_free_page.seach_film_free()

    with allure.step("Проверить заголовок"):
        assert title_film_free == ("Введите номер телефона")

    with allure.step("Закрыть браузер"):
        film_free_page.close_driver()


@allure.title("Случайный поиск")
@pytest.mark.test_05_ui
def test_random_seach():
    with allure.step("Открыть окно Кинопоиск"):
        browser = webdriver.Chrome()
        button_random_film_page = Kinopoisk_UI(browser)

    with allure.step("Нажать кнопку Лупа"):
        button_random_film_page.click_random_seach()

    with allure.step("Нажать кнопку Случайный фильм"):
        button_random_film_page.click_random_film()

    with allure.step("Сделать скриншот результата поиска"):
        button_random_film_page.screenshot()

    with allure.step("Закрыть браузер"):
        button_random_film_page.close_driver()
