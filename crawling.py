# import re
# 중고 나라 페이지 HTML 불러오기위한 라이브러리
import requests

#HTMl 문서에서 원하는 태그/텍스트를 뽑는 라이브러
from bs4 import BeautifulSoup

# import 변경 (한글 검색어를 URL 에서 사용 가능한 라이브러리)
import urllib.parse


def to_korean_name(pokemon_name):

    KOREAN_NAMES = {
        "bulbasaur":"이상해씨","ivysaur":"이상해풀","venusaur":"이상해꽃",
        "charmander":"파이리","charmeleon":"리자드","charizard":"리자몽",
        "squirtle":"꼬부기","wartortle":"어니부기","blastoise":"거북왕",
        "caterpie":"캐터피","metapod":"단데기","butterfree":"버터플",
        "weedle":"뿔충이","kakuna":"딱구리","beedrill":"독침붕",
        "pidgey":"구구","pidgeotto":"피죤","pidgeot":"피죤투",
        "rattata":"꼬렛","raticate":"레트라",
        "spearow":"깨비참","fearow":"폴켓",
        "ekans":"아보","arbok":"아보크",
        "pikachu":"피카츄","raichu":"라이츄",
        "sandshrew":"모래두지","sandslash":"고지",
        "nidoran-f":"니드런♀","nidorina":"니드리나","nidoqueen":"니드퀸",
        "nidoran-m":"니드런♂","nidorino":"니드리노","nidoking":"니드킹",
        "clefairy":"삐삐","clefable":"픽시",
        "vulpix":"식스테일","ninetales":"나인테일",
        "jigglypuff":"푸린","wigglytuff":"푸크린",
        "zubat":"주뱃","golbat":"골뱃",
        "oddish":"뚜벅초","gloom":"냄새꼬","vileplume":"라플레시아",
        "paras":"파라스","parasect":"파라섹트",
        "venonat":"콘팡","venomoth":"도나리",
        "diglett":"디그다","dugtrio":"닥트리오",
        "meowth":"나옹","persian":"페르시온",
        "psyduck":"고라파덕","golduck":"골덕",
        "mankey":"망키","primeape":"성원숭",
        "growlithe":"가디","arcanine":"윈디",
        "poliwag":"발챙이","poliwhirl":"슈륙챙이","poliwrath":"강챙이",
        "abra":"케이시","kadabra":"윤겔라","alakazam":"후딘",
        "machop":"알통몬","machoke":"근육몬","machamp":"괴력몬",
        "bellsprout":"모다피","weepinbell":"우츠동","victreebel":"우츠보트",
        "tentacool":"왕눈해","tentacruel":"독파리",
        "geodude":"꼬마돌","graveler":"돌돌이","golem":"golem",
        "ponyta":"포니타","rapidash":"날쌩마",
        "slowpoke":"야돈","slowbro":"야부",
        "magnemite":"코일","magneton":"레어코일",
        "farfetchd":"파오리","doduo":"두두","dodrio":"두트리오",
        "seel":"쥬쥬","dewgong":"쥬레곤",
        "grimer":"질퍽이","muk":"질뻐기",
        "shellder":"셀러","cloyster":"파르셀",
        "gastly":"고오스","haunter":"고우스트","gengar":"팬텀",
        "onix":"롱스톤","drowzee":"슬리프","hypno":"슬리퍼",
        "krabby":"크랩","kingler":"킹크랩",
        "voltorb":"찌리리공","electrode":"붐볼",
        "exeggcute":"아라리","exeggutor":"나시",
        "cubone":"탕구리","marowak":"마로왁",
        "hitmonlee":"시라소몬","hitmonchan":"에비몬",
        "lickitung":"내루미","koffing":"또가스","weezing":"독독이",
        "rhyhorn":"뿔카노","rhydon":"강철톤",
        "chansey":"럭키","tangela":"덩쿠리","kangaskhan":"캥카",
        "horsea":"쏘드라","seadra":"시드라",
        "goldeen":"콘치","seaking":"왕콘치",
        "staryu":"별가사리","starmie":"아쿠스타",
        "mr-mime":"마임맨","scyther":"스라크","jynx":"루주라",
        "electabuzz":"에레브","magmar":"마그마",
        "pinsir":"쁘사이저","tauros":"켄타로스",
        "magikarp":"잉어킹","gyarados":"갸라도스",
        "lapras":"라프라스","ditto":"메타몽",
        "eevee":"이브이","vaporeon":"샤미드","jolteon":"쥬피썬더","flareon":"부스터",
        "porygon":"폴리곤",
        "omanyte":"암나이트","omastar":"암스타",
        "kabuto":"투구","kabutops":"투구푸스",
        "aerodactyl":"프테라","snorlax":"잠만보",
        "articuno":"프리져","zapdos":"썬더","moltres":"파이어",
        "dratini":"미니룡","dragonair":"신룡","dragonite":"망나뇽",
        "mewtwo":"뮤츠","mew":"뮤",
    }

    kor_name = KOREAN_NAMES.get(pokemon_name, pokemon_name)

    return kor_name


# 함수 변수 수정 (임시로 만들어 놓은 부분 입력받은 포켓몬나오게설계)
def crawling(pokemon_name):
    pokemon_name = to_korean_name(pokemon_name)
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