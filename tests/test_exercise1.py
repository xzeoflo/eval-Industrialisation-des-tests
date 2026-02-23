import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_wikipedia_registration():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10) 

    try:
        driver.get("https://fr.wikipedia.org/w/index.php?title=Spécial:Créer_un_compte")

        driver.find_element(By.ID, "wpName2").send_keys("votre_pseudo_test_2026")
        driver.find_element(By.ID, "wpPassword2").send_keys("MotDePasseSecurise123!")
        driver.find_element(By.ID, "wpRetype").send_keys("MotDePasseSecurise123!")

        submit = driver.find_element(By.ID, "wpCreateaccount")

        assert submit.is_displayed()
        assert submit.is_enabled()
        assert "Créer un compte" in driver.title

    finally:
        driver.quit()