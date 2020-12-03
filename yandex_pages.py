from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib


class YandexLocators:
    YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "input[name=text]")
    YANDEX_MINI_SUGGEST = (By.CSS_SELECTOR, "div.mini-suggest__popup")
    YANDEX_SEARCH_RESULT_TABLE = (By.CSS_SELECTOR, "ul.serp-list")
    YANDEX_SEARCH_RESULTS = (By.CSS_SELECTOR, "div.path > a.link")
    YANDEX_IMAGES = (By.CSS_SELECTOR, "a[data-id='images']")
    YANDEX_IMAGES_FIRST_CATEGORY = (By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0")
    YANDEX_FIRST_IMAGE = (By.CSS_SELECTOR, "div.serp-item:nth-child(2)")
    YANDEX_BIG_IMAGE = (By.CSS_SELECTOR, "img.MMImage-Origin")
    YANDEX_MODAL_WINDOW_FORWARD_BUTTON = (By.CSS_SELECTOR, "div.CircleButton_type_next")
    YANDEX_MODAL_WINDOW_BACKWARD_BUTTON = (By.CSS_SELECTOR, "div.CircleButton_type_prev")


class YandexPages(BasePage):
    def should_be_search_field(self):
        """Проверка на наличие поля поиска"""
        self.find_element_on_the_page(YandexLocators.YANDEX_SEARCH_FIELD)

    def enter_word_in_the_search_field(self, word="Тензор"):
        """Ввод слова в окно поиска"""
        search_field = self.find_element_on_the_page(YandexLocators.YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)

    def should_be_mini_suggest(self):
        """Проверка на наличие всплывающей подсказки"""
        mini_suggest = self.find_element_on_the_page(YandexLocators.YANDEX_MINI_SUGGEST)
        WebDriverWait(mini_suggest, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li:nth-child(2)')),
                                              message=f"Can't find mini suggest")

    def click_enter_key(self):
        """Нажатие клавиши Enter в поле поиска"""
        search_field = self.find_element_on_the_page(YandexLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys('\ue007')

    def should_be_result_table_after_search(self):
        """Проверка на наличие таблицы результатов"""
        return self.find_element_on_the_page(YandexLocators.YANDEX_SEARCH_RESULT_TABLE)

    def should_be_link_in_the_first_five_results(self, result_table, expected_link="tensor.ru"):
        """Проверка на наличие ожидаемой ссылки в первых 5 результатах выдачи"""
        results = self.find_elements_on_the_page(YandexLocators.YANDEX_SEARCH_RESULTS)
        flag = False
        for result in results[:4]:
            if expected_link in result.text:
                flag = True
        assert flag, f"There is no expected link in the result table"

    def should_be_link_to_images(self):
        """Проверка на наличие ссылки на главной странице на сервис Яндекс.Картинки"""
        images_object = self.find_element_on_the_page(YandexLocators.YANDEX_IMAGES)
        return images_object

    def go_to_images_page(self, images_object):
        """Переход в Картинки"""
        link = images_object.get_attribute("href")
        return self.go_to_page(link)

    def is_current_url_correct(self, url):
        """Проверка что перешли именно в картинки"""
        assert url in self.browser.current_url, f"{self.browser.current_url} is not {url}"

    def open_first_category(self):
        """Открываем первую категорию. Возвращает название категории"""
        first_category = self.find_element_on_the_page(YandexLocators.YANDEX_IMAGES_FIRST_CATEGORY)
        category = first_category.get_attribute("data-grid-text")
        first_category.click()
        return category

    def category_should_be_opened(self, category):
        """Проверка что категория открылась"""
        url = urllib.parse.unquote(self.browser.current_url)
        assert category in url, f"{category} isn't right"

    def should_be_right_text_in_the_search_field(self, text):
        """Проверка что в поле поиска нужный текст"""
        search_input = self.find_element_on_the_page(YandexLocators.YANDEX_SEARCH_FIELD)
        assert search_input.get_attribute("value") == text, "Search request in the search field is not right"

    def open_first_image(self):
        """Открытие первой картинки"""
        first_image = self.find_element_on_the_page(YandexLocators.YANDEX_FIRST_IMAGE)
        first_image.click()

    def image_should_appear_in_modal_window(self):
        """Проверка что открылась картинка"""
        image = self.find_element_on_the_page(YandexLocators.YANDEX_BIG_IMAGE)
        return image.get_attribute("src")

    def click_next_button(self):
        """Нажатие кнопки вперед"""
        next_button = self.find_element_on_the_page(YandexLocators.YANDEX_MODAL_WINDOW_FORWARD_BUTTON)
        next_button.click()

    def click_prev_button(self):
        """Нажатие кнопки назад"""
        prev_button = self.find_element_on_the_page(YandexLocators.YANDEX_MODAL_WINDOW_BACKWARD_BUTTON)
        prev_button.click()

    def get_image_link(self):
        """Получение ссылки на изображение в модальном окне"""
        return self.find_element_on_the_page(YandexLocators.YANDEX_BIG_IMAGE).get_attribute("src")

    @staticmethod
    def image_should_be_changed(origin_image_url, next_image_url):
        """Проверка на то, что изображение изменилось"""
        assert origin_image_url != next_image_url, "Images are the same"

    @staticmethod
    def images_should_be_same(origin_image_url, next_image_url):
        """Проверка на совпадение изображений"""
        assert origin_image_url == next_image_url, "Images are different"
