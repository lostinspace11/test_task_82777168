from yandex_pages import YandexPages
import time


def test_main_yandex_page(browser):
    """
    Тестирование основной страницы:
    1)	Зайти на yandex.ru
    2)	Проверить наличия поля поиска
    3)	Ввести в поиск Тензор
    4)	Проверить, что появилась таблица с подсказками (suggest)
    5)	При нажатии Enter появляется таблица результатов поиска
    6)	 В первых 5 результатах есть ссылка на tensor.ru
    """
    yandex_main_page = YandexPages(browser)
    yandex_main_page.go_to_main_page()
    yandex_main_page.should_be_search_field()
    yandex_main_page.enter_word_in_the_search_field()
    yandex_main_page.should_be_mini_suggest()
    yandex_main_page.click_enter_key()
    result_table = yandex_main_page.should_be_result_table_after_search()
    yandex_main_page.should_be_link_in_the_first_five_results(result_table, expected_link="tensor.ru")
    time.sleep(10)


def test_images_yandex_page(browser):
    """
    Тестирование Яндекс.Картинки
    1)	Зайти на yandex.ru
    2)	Ссылка «Картинки» присутствует на странице
    3)	Кликаем на ссылку
    4)	Проверить, что перешли на url https://yandex.ru/images/
    5)	Открыть 1 категорию, проверить что открылась, в поиске верный текст
    6)  Открыть 1 картинку , проверить что открылась
    7)  При нажатии кнопки вперед  картинка изменяется
    8)  При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо проверить,
    что это то же изображение.
    """
    yandex_images_page = YandexPages(browser)
    yandex_images_page.go_to_main_page()
    images_object = yandex_images_page.should_be_link_to_images()
    images_page = yandex_images_page.go_to_images_page(images_object)
    yandex_images_page.is_current_url_correct("https://yandex.ru/images/")
    category = yandex_images_page.open_first_category()
    yandex_images_page.category_should_be_opened(category)
    yandex_images_page.should_be_right_text_in_the_search_field(category)
    yandex_images_page.open_first_image()
    origin_image_url = yandex_images_page.image_should_appear_in_modal_window()
    yandex_images_page.click_next_button()
    next_image_link = yandex_images_page.get_image_link()
    yandex_images_page.image_should_be_changed(origin_image_url, next_image_link)
    yandex_images_page.click_prev_button()
    next_image_link = yandex_images_page.get_image_link()
    yandex_images_page.images_should_be_same(origin_image_url, next_image_link)
    time.sleep(10)
