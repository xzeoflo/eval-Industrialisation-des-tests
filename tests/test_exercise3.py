import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )
    yield driver
    driver.quit()

def test_wikipedia_registration(driver):
    driver.get("https://fr.wikipedia.org/w/index.php?title=Spécial:Créer_un_compte")
    driver.find_element(By.ID, "wpName2").send_keys("votre_pseudo_test_2026")
    submit = driver.find_element(By.ID, "wpCreateaccount")
    assert submit.is_displayed()
    assert "Créer un compte" in driver.title

def test_extract_full_wiki_news(driver):
    driver.get("https://fr.wikipedia.org/wiki/Wikipédia:Accueil_principal")
    breves = driver.find_elements(By.CSS_SELECTOR, ".accueil_2017_cadre > ul > li")
    assert len(breves) > 0