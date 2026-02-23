import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_extract_full_wiki_news(driver):
    driver.get("https://fr.wikipedia.org/wiki/Wikipédia:Accueil_principal")

    print("\n--- BRÈVES D'ACTUALITÉ ---")
    breves = driver.find_elements(By.CSS_SELECTOR, ".accueil_2017_cadre > ul > li")
    for b in breves:
        print(f"- {b.text}")

    print("\n--- ÉVÉNEMENTS EN COURS ---")
    events = driver.find_elements(By.CSS_SELECTOR, ".liste-horizontale a")
    for event in events:
        href = event.get_attribute("href")
        if href and "wiki" in href and ":" not in href.split("/")[-1]:
            print(f"- {event.text} : {href}")

    print("\n--- NÉCROLOGIE ---")
    deces = driver.find_elements(By.CSS_SELECTOR, ".accueil-actualites-necrologie li")
    for d in deces:
        if d.text and not d.text[0].isdigit():
            print(f"- {d.text}")

    assert len(breves) > 0
