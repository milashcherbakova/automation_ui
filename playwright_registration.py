from playwright.sync_api import sync_playwright
from urllib3.util import timeout

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('milana_shcherbakova_2000@list.ru')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('mila')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('123456789')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")
page.wait_for_timeout(5000)