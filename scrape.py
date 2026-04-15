# scrape.py
import requests
from bs4 import BeautifulSoup
import os
import time

BASE = "https://slaythespire.wiki.gg"

# STS2の対象ページ一覧
PAGES = [
    "/wiki/Slay_the_Spire_2:Ironclad",
    "/wiki/Slay_the_Spire_2:Silent",
    "/wiki/Slay_the_Spire_2:Regent",
    "/wiki/Slay_the_Spire_2:Necrobinder",
    "/wiki/Slay_the_Spire_2:Defect",
    "/wiki/Slay_the_Spire_2:All_Cards",
    "/wiki/Slay_the_Spire_2:All_Relics",
    "/wiki/Slay_the_Spire_2:All_Potions",
    "/wiki/Slay_the_Spire_2:All_Events",
    "/wiki/Slay_the_Spire_2:Acts",
    "/wiki/Slay_the_Spire_2:Timeline",
]

OUTPUT_DIR = "./sts2_wiki_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def scrape_page(url):
    res = requests.get(url, headers=HEADERS)
    print(f"  HTTPステータス: {res.status_code}")
    if res.status_code != 200:
        return None
    
    soup = BeautifulSoup(res.text, "html.parser")
    content = soup.find("div", class_="mw-parser-output")
    if not content:
        return None
    
    # 不要タグ除去
    for tag in content.find_all(["script", "style", "sup", "figure"]):
        tag.decompose()
    
    return content.get_text(separator="\n", strip=True)

for path in PAGES:
    url = BASE + path
    page_name = path.split(":")[-1]  # "Ironclad" など
    print(f"\nScraping: {page_name}")
    
    text = scrape_page(url)
    if text:
        filepath = os.path.joi