import requests
from bs4 import BeautifulSoup

def get_joongonara():
    url = "https://web.joongna.com/search/포켓몬카드"


    # 페이지 요청
    
    # 헤더 추가
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)

    # 파싱

    soup = BeautifulSoup(res.text, 'html.parser')

    # 데이터 추출
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
    print(result)

get_joongonara()

