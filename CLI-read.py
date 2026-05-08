import json
from pokemon_detail import show_pokemon_detail
from crawling import crawling
from make_excel import create_excel_report

# Type 한글화 작업
TYPE_KO = {
    "normal": "노말",
    "fire": "불꽃",
    "water": "물",
    "electric": "전기",
    "grass": "풀",
    "ice": "얼음",
    "fighting": "격투",
    "poison": "독",
    "ground": "땅",
    "flying": "비행",
    "psychic": "에스퍼",
    "bug": "벌레",
    "rock": "바위",
    "ghost": "고스트",
    "dragon": "드래곤",
    "dark": "악",
    "steel": "강철",
    "fairy": "페어리"
}

# JSON 파일 가져오기
with open("pokemon_cache.json", "r", encoding="utf-8") as f:
    data = json.load(f)

pokemon_data = data["pokemon"]

# 타입별 리스트 조회
def make_pokemon_object(value):
    return {
        "name": value.get("name", ""),
        "types": value.get("types", []),
        "moves": value.get("moves", []),
        "evolution": value.get("evolution", []),
        "image": value.get("image", "")
    }


def get_all_types():
    type_set = set()

    for value in pokemon_data.values():
        for t in value.get("types", []):
            type_set.add(t)

    return sorted(list(type_set))


def get_pokemon_by_type(pokemon_type):
    result = []

    for value in pokemon_data.values():
        if pokemon_type in value.get("types", []):
            result.append(make_pokemon_object(value))

    return result


def search_pokemon(keyword):
    keyword = keyword.strip().lower()

    for key, value in pokemon_data.items():
        name = value.get("name", "").lower()

        if keyword in key.lower() or keyword in name:
            return make_pokemon_object(value)

    return None


def show_type_page():
    while True:
        print("\n===== 포켓몬 타입 조회 =====\n")

        type_list = get_all_types()

        for i, pokemon_type in enumerate(type_list, start=1):
            print(f"{i}. {TYPE_KO.get(pokemon_type, pokemon_type)}")

        print("0. 종료")

        choice = input("\n번호 입력: ").strip()

        if choice == "0":
            return "EXIT", None

        if not choice.isdigit():
            print("숫자만 입력하세요.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(type_list):
            print("없는 번호입니다.")
            continue

        selected_type = type_list[choice - 1]
        pokemon_list = get_pokemon_by_type(selected_type)

        return "POKEMON_LIST",{
            "type": selected_type,
            "list": pokemon_list
        }


def show_list_page(selected_type, pokemon_list):
    while True:
        print(f"\n[{selected_type} 타입 포켓몬 리스트]\n")

        for idx, pokemon in enumerate(pokemon_list, start=1):
            print(f"{idx}. {pokemon['name']}")

        print("\n0. 다시 조회 페이지로")
        print("\n번호 입력 상세 보기")

        choice = input("\n선택: ").strip()

        if choice == "0":
            return "LIST", None

        if choice.isdigit():
            choice = int(choice)

            if choice < 1 or choice > len(pokemon_list):
                print("없는 번호입니다.")
                continue

            selected_pokemon = pokemon_list[choice - 1]
            return "DETAIL", selected_pokemon

        selected_pokemon = search_pokemon(choice)

        if selected_pokemon is None:
            print("검색 결과가 없습니다.")
            continue

        return "DETAIL", selected_pokemon



def show_card_price_page(pokemon):
    print("\n=== 포켓몬 카드 시세 출력 ===")

    pokemon_name = pokemon.get("name", "")
    print(f"검색어: {pokemon_name} 카드")

    card_data = crawling(pokemon_name)

    if not card_data:
        print("카드 시세 데이터를 찾지 못했습니다.")
        input("\nEnter를 누르면 상세보기로 돌아갑니다.")
        return "DETAIL", pokemon

    # 터미널에도 검색 결과 출력
    print("\n[중고나라 검색 결과]\n")

    for idx, item in enumerate(card_data, start=1):
        print(f"{idx}. {item['title']}")
        print(f"   가격: {item['price']}")
        print()

    # 엑셀 파일 생성
    create_excel_report(card_data, pokemon_name)

    input("\nEnter를 누르면 상세보기로 돌아갑니다...")

    return "DETAIL", pokemon

def main():
    state = "LIST"
    selected_pokemon = None
    search_type = 0

    current_type = None
    current_pokemon_list = []

    while True:
        if state == "LIST":
            state, result = show_type_page()
            search_type = 0

            if state == "POKEMON_LIST":
                current_type = result["type"]
                current_pokemon_list = result["list"]

            elif state == "EXIT":
                selected_pokemon = None

        elif state == "POKEMON_LIST":
            state, selected_pokemon = show_list_page(
                current_type,
                current_pokemon_list
            )

        elif state == "DETAIL":
            if selected_pokemon is None:
                state = "LIST"
                continue

            state, selected_pokemon = show_pokemon_detail(
                selected_pokemon,
                search_type
            )

        elif state == "CARD_PRICE":
            state, selected_pokemon = show_card_price_page(selected_pokemon)
            search_type = 2

        elif state == "EXIT":
            print("프로그램 종료")
            break

        else:
            print("알 수 없는 상태입니다.")
            break

if __name__ == "__main__":
    main()