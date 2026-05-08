# import re
# 중고 나라 페이지 HTML 불러오기위한 라이브러리
import requests

#HTMl 문서에서 원하는 태그/텍스트를 뽑는 라이브러
from bs4 import BeautifulSoup

# import 변경 (한글 검색어를 URL 에서 사용 가능한 라이브러리)
import urllib.parse

# 함수 변수 수정 (임시로 만들어 놓은 부분? 입력받은 포켓몬나오게설계)
def crawling(pokemon_name):
    keyword = pokemon_name + " 카드"
# 한글과 공백이 들어간 검색어를 URL 에서 안전하게 쓰도록 변환   
    encoded_keyword = urllib.parse.quote(keyword) 

# 중고 나라 검색 페이지 URL 생성
    url = f"https://web.joongna.com/search/{encoded_keyword}"

    headers = { 
        'User-Agent' : (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/147.0.0.0 Safari/537.36'
        )
    }
   
   # 중고나라 검색 페이지에 요청 Time out 10초 이상 응답없으면 중단, 
    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

      # 404,500 에러발생  
        response.raise_for_status()
    
    # 오류 발생시 리턴
    except requests.exceptions.RequestException as e:
      print("중고나라 요청 실패", e)
      return []
    
# HTML 문자열을 BeautifulSoup으로 분석 가능한 형태로 변환
    soup = BeautifulSoup(
        response.text, 
        'html.parser'
    )

    # 상품 카드 전체
    pockemon_list = soup.select("div.z-auto")
    
    result = []


    for item in pockemon_list:
        title = item.select_one(".whitespace-pre-line")  # 제목
        price = item.select_one(".text-18")      # 가격

        if title and price:

         # 텍스트만 뽑아서 딕셔너리 형태로 저장   
            result.append({
                "title": title.get_text(strip=True),
                "price": price.get_text(strip=True),
            })


# 결과가 하나도 없으면 안내메세지 출력          
    if not result:
        print("검색 결과 없음")
  
# 상품 리스트 반환  
    return result

# # 직접 실행 했을때만 코드 실
# if __name__ == "__main__":
#     print(crawling())