import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = "https://only.digital/"

FOOTER_SELECTORS = [
    (By.TAG_NAME, "footer"),
    (By.LINK_TEXT, "Политика конфиденциальности"),
    (By.CSS_SELECTOR, "footer a[href*='linkedin']"),
    (By.CSS_SELECTOR, "footer a[href*='t.me']"),
    (By.CSS_SELECTOR, "footer address"),
]

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_footer_elements_present(driver):
    driver.get(URL)
    for by, value in FOOTER_SELECTORS:
        element = driver.find_elements(by, value)
        assert element, f"Element not found: {value}"
