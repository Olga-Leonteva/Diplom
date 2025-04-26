from selenium.webdriver.common.by import By
from config_UI import UI_URL
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Kinopoisk_UI:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(UI_URL)
        self._driver.maximize_window()

    # Заголовок главной страницы
    def home_page(self):
        title_hp = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.kinopoisk-header-logo__img'))
                ).get_attribute('alt')
        return title_hp

    # Ввести названия фильма Мастер и Маргарита
    def name_film(self):
        film = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[name="kp_query"]')))
        film.send_keys("Мастер и Маргарита")
        return film

    # Просмотреть результат поиска фильма Мастер и Маргарита
    def result_film(self):
        seach_film = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#suggest-item-film-1115471'))).text
        return seach_film

    # Нажать кнопку Войти
    def click_button_login(self):
        login = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.styles_loginButton__LWZQp')))
        login.click()

    # Найти заголовок страницы Войти
    def search_title_login(self):
        button_login = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.passp-add-account-page-title'))).text
        return button_login

    # Нажать кнопку Смотреть кино бесплатно
    def click_free_movie(self):
        free_movie = WebDriverWait(self._driver, 25).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.style_buttonLight____6ma')))
        free_movie.click()

    # Найти заголовок страницы Смотреть кино бесплатно
    def search_free_movie(self):
        title_free_movie = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.passp-add-account-page-title'))).text
        return title_free_movie

    # Нажать кнопку Лупа
    def click_random_search(self):
        random_search = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.search-form-submit-button__icon')))
        random_search.click()

    # Нажать кнопку Случайный фильм
    def click_random_film(self):
        button_random_film = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#search')))
        button_random_film.click()

    # Сделать скриншот результата поиска
    def screenshot(self, test_name):
        self._driver.save_screenshot(f"screenshots/{test_name}.png")

    # Результат поиска Случайный фильм
    def random_movie(self):
        result_random_movie = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.filmName')))
        return result_random_movie is not None
