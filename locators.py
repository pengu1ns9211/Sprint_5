from selenium.webdriver.common.by import By


class Locators:
    login_button_main = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт" с главной страницы
    login_button_login_page = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти" со страницы логина
    login_header_tag_h2 = By.XPATH, './/h2[text()="Вход"]'  # Заголовок "Вход"
    login_link_from_recovery_pass = By.XPATH, './/a[text()="Войти"]'  # Ссылка "Войти" со страницы восстановления пароля
    logout_button = By.XPATH, './/button[text()="Выход"]'  # Kнопка "Выход" из личного кабинета
    personal_account_button = By.XPATH, './/p[text()="Личный Кабинет"]'  # Kнопка "Личный кабинет"
    registration_button = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    recovery_pass_link = By.XPATH, './/a[text()="Восстановить пароль"]'  # Ссылка "Восстановить пароль"
    recovery_pass_button = By.XPATH, './/button[text()="Восстановить"]'  # Кнопка "Восстановить пароль"
    profile_link = By.XPATH, './/a[text()="Профиль"]'  # Ссылка "Профиль" в личном кабинете
    incorrect_password_message = By.XPATH, './/p[text() = "Некорректный пароль"]'  # Cообщение "Некорректный пароль"
    incorrect_password_check = By.XPATH, './/p[text() = "Некорректный пароль"]'  # Проверка сообщения
    input_name_field = By.XPATH, ".//label[text() = 'Имя']/following-sibling::input"  # Поле ввода имени пользователя
    input_email_field = By.XPATH, ".//label[text() = 'Email']/following-sibling::input"  # Поле ввода email пользователя
    input_password_field = By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input"  # Поле ввода пароля пользователя
    header_h2 = By.XPATH, './/h2'  # Заголовок H2
    make_burger_tag_h1 = By.XPATH, ".//h1[text()='Соберите бургер']"  # Заголовок "Соберите бургер" в конструкторе
    constructor_button = By.XPATH, './/p[text()="Конструктор"]'  # Kнопка "Конструктор"
    order_button = By.XPATH, './/button[text()="Оформить заказ"]'  # Kнопка "Оформить заказ"
    sauces_span = ".//span[contains(text(),'Соусы')]"  # Список Соусы"
    filling_span = ".//span[contains(text(),'Начинки')]"  # Список "Начинки"
    buns_span = ".//span[contains(text(),'Булки')]"  # Список "Булки"
    select_tab_constructor = ".//div[contains(@class, 'current')]/span"  # "Выбранный таб в конструкторе"
