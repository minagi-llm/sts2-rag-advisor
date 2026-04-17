# scrape.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

OUTPUT_DIR = config["output_dir"]
os.makedirs(OUTPUT_DIR, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

def scrape_page(url):
    driver.get(url)
    time.sleep(3)
    text = driver.find_element(By.TAG_NAME, "body").text
    return text if text else None

for source in config["sources"]:
    name = source["name"]
    url = source["url"]
    print(f"\nScraping: {name}")

    text = scrape_page(url)
    if text:
        filepath = os.path.join(OUTPUT_DIR, f"{name}.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {name}\nSource: {url}\n\n{text}")
        print(f"  保存完了: {filepath}（{len(text)}文字）")
    else:
        print(f"  取得失敗: {url}")

driver.quit()
print("\n完了！")