
def show_pokemon_detail(pokemon, search_type=0):
    print("\n" + "=" * 40)
    print("포켓몬 상세 보기")
    print("=" * 40)

    print(f"이름   : {pokemon.get('name')}")

    types = pokemon.get("types", [])
    print(f"타입   : {', '.join(types)}")

    moves = pokemon.get("moves", [])
    print(f"기술   : {', '.join(moves)}")

    evolution = pokemon.get("evolution", [])
    if isinstance(evolution, list):
        print(f"진화   : {' → '.join(evolution)}")
    else:
        print(f"진화   : {evolution}")

    image = pokemon.get("image", "")
    if image:
        print(f"이미지 : {image}")

    print("\n" + "-" * 40)

    if search_type == 0:
        print("이전 경로: 타입 조회")
    elif search_type == 1:
        print("이전 경로: 포켓몬 검색")
    elif search_type == 2:
        print("이전 경로: 카드 시세")
    else:
        print("이전 경로: 알 수 없음")

    print("-" * 40)

    print("\n선택 메뉴")
    print("0. 포켓몬 리스트로 돌아가기")
    print("1. 포켓몬 검색으로 돌아가기")
    print("2. 카드 시세 보기")

    choice = input("\n번호 선택: ").strip()

    if choice == "0":
        return "LIST", pokemon
    elif choice == "1":
        return "POKEMON_LIST", pokemon
    elif choice == "2":
        return "CARD_PRICE", pokemon
    else:
        print("잘못된 입력입니다.")
        return "DETAIL", pokemon