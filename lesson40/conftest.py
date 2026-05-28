import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    print("🌐 Запускаем браузер...")

    chrome_options = Options()
    # Словарь настроек для отключения уведомлений
    prefs = {
        "credentials_enable_service": False,  # Отключаем предложение сохранить пароль
        "profile.password_manager_enabled": False,  # Отключаем сам менеджер паролей
        "profile.password_manager_leak_detection": False,  # Отключаем проверку утечек паролей
        "safebrowsing.enabled": False  # Отключаем антивирус (Safe Browsing)
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")  # Отключаем функцию проверки утечек паролей

    # Отключаем табличку "Chrome управляется тестовым ПО"
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(ChromeDriverManager().install())
    my_driver = webdriver.Chrome(service=service, options=chrome_options)
    my_driver.maximize_window()

    yield my_driver

    print('🚪 Закрываем браузер...')
    my_driver.quit()
