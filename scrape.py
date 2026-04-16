# scrape.py
import requests
from bs4 import BeautifulSoup
import os
import time

BASE = "https://sts2-wiki.org"

PAGES = [
    "/slay-the-spire-2-characters/ironclad",
    "/slay-the-spire-2-characters/silent",
    "/slay-the-spire-2-characters/regent",
    "/slay-the-spire-2-characters/necrobinder",
    "/slay-the-spire-2-characters/defect",
]

OUTPUT_DIR = "./sts2_wiki_docs_v2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def scrape_page(url):
    res = requests.get(url, headers=HEADERS)
    print(f"  HTTPステータス: {res.status_code}")
    if res.status_code != 200:
        return None

    soup = BeautifulSoup(res.text, "html.parser")

    content = (
        soup.find("main") or
        soup.find("article") or
        soup.find("div", class_="content") or
        soup.find("div", id="content")
    )
    if not content:
        content = soup.find("body")

    for tag in content.find_all(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    return content.get_text(separator="\n", strip=True)

for path in PAGES:
    url = BASE + path
    page_name = path.split("/")[-1]
    print(f"\nScraping: {page_name}")

    text = scrape_page(url)
    if text:
        filepath = os.path.join(OUTPUT_DIR, f"{page_name}.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {page_name}\nSource: {url}\n\n{text}")
        print(f"  保存完了: {filepath}（{len(text)}文字）")
    else:
        print(f"  取得失敗: {url}")

    time.sleep(2)

print("\n完了！")