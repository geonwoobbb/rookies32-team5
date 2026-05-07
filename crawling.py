import requests
from bs4 import BeautifulSoup
import re

keyword = "라이츄" + "카드"

def crawling():
    url = f"https://web.joongna.com/search/{keyword}"

    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 상품 카드 전체
    pocketmon_list = soup.select("div.z-auto")
    
    result = []
    for item in pocketmon_list:
        title = item.select_one(".whitespace-pre-line")  # 제목
        price = item.select_one(".text-18")      # 가격

        if title and price:
            result.append({
                "title": title.get_text(strip=True),
                "price": price.get_text(strip=True),
            })

    return result

print(crawling())