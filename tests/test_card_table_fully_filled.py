# ЗАДАНИЕ 30.5.1
# НЕЯВНЫЕ ОЖИДАНИЯ

import pytest
from selenium.webdriver.common.by import By
from config import valid_email, valid_password


def test_card_table_fully_filled():


    '''Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода, возраст)'''

    # Установка неявного ожидания
    pytest.driver.implicitly_wait(10)

    # Ввод эл.почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопке "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка того, что осуществлен переход на главную страницу пользователя
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert names[0].text != ''
    # Проверка того, что поля карточек не пустые со счетчиком i для санити.
    for i in range(len(names)):
        assert len(images[i].get_attribute('src')) > 0
        assert len(names[i].text) > 0
        assert len(descriptions[i].text) > 0
        assert ',' in descriptions[i].text
        print(i) #добавлен для санити


