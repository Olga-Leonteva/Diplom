import allure
import pytest
from Kinopoisk_UI import Kinopoisk_UI


@allure.epic("UI")
@allure.title("Проверка заголовка на главной странице")
@pytest.mark.ui
@pytest.mark.pos
@pytest.mark.smoke
def test_home_page_01(browser):
    with allure.step("Открыть окно Кинопоиск"):
        h_page = Kinopoisk_UI(browser)

    with allure.step("Найти заголовок страницы"):
        title_hp = h_page.home_page()

    with allure.step("Проверить заголовок"):
        assert title_hp == ('Кинопоиск')


@allure.epic("UI")
@allure.title("Быстрый поиск фильма")
@pytest.mark.ui
@pytest.mark.pos
def test_quick_search(browser):
    with allure.step("Открыть окно Кинопоиск"):
        film_page = Kinopoisk_UI(browser)

    with allure.step("Ввести названия фильма Мастер и Маргарита"):
        film_page.name_film()

    with allure.step("Просмотреть результат поиска"):
        search_film = film_page.result_film()

    with allure.step("Проверить поиск"):
        assert search_film == ("Мастер и Маргарита")


@allure.epic("UI")
@allure.title("Вход в личный кабинет")
@pytest.mark.ui
@pytest.mark.pos
def test_button_login(browser):
    with allure.step("Открыть окно Кинопоиск"):
        button_login_page = Kinopoisk_UI(browser)

    with allure.step("Нажать кнопку Войти"):
        button_login_page.click_button_login()

    with allure.step("Найти заголовок страницы"):
        button_login = button_login_page.search_title_login()

    with allure.step("Проверить заголовок"):
        assert button_login == ("Введите номер телефона")


@allure.epic("UI")
@allure.title("Смотреть кино бесплатно")
@pytest.mark.ui
@pytest.mark.pos
def test_watch_free_movie(browser):
    with allure.step("Открыть окно Кинопоиск"):
        watch_free_movie = Kinopoisk_UI(browser)

    with allure.step("Нажать кнопку Смотреть кино бесплатно"):
        watch_free_movie.click_free_movie()

    with allure.step("Найти заголовок страницы"):
        title_free_movie = watch_free_movie.search_free_movie()

    with allure.step("Проверить заголовок"):
        assert title_free_movie == ("Введите номер телефона")


@allure.epic("UI")
@allure.title("Случайный поиск")
@pytest.mark.ui
@pytest.mark.pos
def test_random_search(browser):
    with allure.step("Открыть окно Кинопоиск"):
        button_random_film_page = Kinopoisk_UI(browser)

    with allure.step("Нажать кнопку Лупа"):
        button_random_film_page.click_random_search()

    with allure.step("Нажать кнопку Случайный фильм"):
        button_random_film_page.click_random_film()

    with allure.step("Сделать скриншот результата поиска"):
        button_random_film_page.screenshot("test_random_search")

    with allure.step("Проверить результат поиска"):
        assert button_random_film_page.random_movie()
