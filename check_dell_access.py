
import requests
from bs4 import BeautifulSoup

url = "https://www.dellstore.com/xps-13-laptop-cdx13260cto02mino.html"

response = requests.get(
    url,
    timeout=15,
    headers={"User-Agent": "Mozilla/5.0"},
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(" ", strip=True)

for price in ["₹84,990", "84,990.00", "84990"]:
    position = page_text.find(price)

    if position != -1:
        start = max(0, position - 100)
        end = min(len(page_text), position + 150)
        print("Found price text:", page_text[start:end])
        break
else:
    print("Price not found in visible page text.")
    print("Checking HTML metadata...")

    for tag in soup.find_all("meta"):
        content = tag.get("content", "")
        if "84990" in content or "84,990" in content:
            print("Metadata:", tag)
