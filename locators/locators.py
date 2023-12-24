from selenium.webdriver.common.by import By


class Locators:
    user_profile_button_in_header = (By.XPATH, './/a[@href="/account"]')  # поиск кнопки [Личный Кабинет]

    user_profile_button_under_order_form = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # поиск кнопки [Войти в аккаунт]

    login_header = (By.XPATH, './/h2[text()="Вход"]')  # заголовок страницы логина

    reset_pass_link = (By.XPATH, './/a[@href="/forgot-password"]')  # поиск ссылки для восстановления пароля

    reset_pass_header = (By.XPATH, './/h2[text()="Восстановление пароля"]')  # заголовок формы восстановления пароля

    login_link = (By.XPATH, './/a[@href="/login"]')  # поиск ссылки для входа в личный кабинет в форме восстановления пароля

    email_input_login_form = (By.XPATH, './/label[text()="Email"]/following-sibling::input')  # поиск поля для ввода Email

    pass_input_login_form = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')   # поиск поля для ввода Пароль

    login_button = (By.XPATH, './/button[text()="Войти"]')  # поиск кнопки [Войти]

    registration_link = (By.XPATH, './/a[@href="/register"]')  # поиск ссылки для регистрации пользователя

    name_input_registration_form = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')  # поиск поля для ввода Имя

    email_input_registration_form = (By.XPATH, './/label[text()="Email"]/following-sibling::input')  # поиск поля для ввода Email

    password_input_registration_form = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')  # поиск поля для ввода Пароль

    registration_button = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # поиск кнопки [Зарегистрироваться]

    registration_header = (By.XPATH, './/h2[text()="Регистрация"]')  # Заголовок формы регистрации

    error_input_pass = (By.XPATH, './/p[text()="Некорректный пароль"]')  # поиск сообщения о неверном вводе пароля

    profile_section_link = (By.XPATH, './/nav[@class="Account_nav__Lgali"]/ul/li[1]')  # поиск раздела "Профиль" в личном кабинете

    exit_button = (By.XPATH, './/nav[@class="Account_nav__Lgali"]/ul/li[3]/button')  # поиск кнопки [Выход]

    constructor_button = (By.XPATH, './/nav[@class="AppHeader_header__nav__g5hnF"]/ul/li[1]')  # поиск кнопки "Конструктор" в хэдере страницы

    logo_stellar_burgers = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # поиск кнопки логотипа Stellar Burgers в хэдере страницы

    buns_section = (By.XPATH, './/span[text()="Булки"]/parent::div')  # поиск раздела "Булки"

    sauces_section = (By.XPATH, './/.//span[text()="Соусы"]/parent::div')  # поиск раздела "Соусы"

    fillings_section = (By.XPATH, './/.//span[text()="Начинки"]/parent::div')  # поиск раздела "Начинки"

    buns_section_name = (By.XPATH, './/h2[text()="Булки"]')  # поиск заголовка раздела "Булки"

    sauces_section_name = (By.XPATH, './/h2[text()="Соусы"]')  # поиск заголовка раздела "Соусы"

    fillings_section_name = (By.XPATH, './/h2[text()="Начинки"]')  # поиск заголовка раздела "Соусы"
