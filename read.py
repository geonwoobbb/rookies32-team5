import json

# JSON 불러오기
with open("pokemon_cache.json", "r", encoding="utf-8") as f:
    data = json.load(f)

pokemon_data = data["pokemon"]



def get_pokemon_by_type(pokemon_type):

    result = {}

    for pokemon, value in pokemon_data.items():

        # 타입 검사
        if pokemon_type in value["types"]:

            result[pokemon] = {
                "name": value["name"],
                "types": value["types"],
                "moves": value["moves"],
                "evolution": value["evolution"]
            }

    return result


def get_all_types():

    type_set = set()

    for value in pokemon_data.values():

        for t in value["types"]:
            type_set.add(t)

    return sorted(list(type_set))



while True:

    print("\n===== 포켓몬 타입 조회 =====\n")

    type_list = get_all_types()

 
    for i, pokemon_type in enumerate(type_list, start=1):
        print(f"{i}. {pokemon_type}")

    print("0. 종료")

    # 입력
    choice = input("\n번호 입력: ")

    # 종료
    if choice == "0":
        print("프로그램 종료")
        break

    # 숫자 검사
    if not choice.isdigit():
        print("숫자만 입력하세요")
        continue

    # 문자열 -> 숫자 변환
    choice = int(choice)

    # 범위 검사
    if choice < 1 or choice > len(type_list):
        print("없는 번호입니다")
        continue

    # 선택 타입
    selected_type = type_list[choice - 1]

    # 타입별 조회
    result = get_pokemon_by_type(selected_type)

    print(f"\n[{selected_type} 타입 포켓몬 리스트]\n")

    # 리스트 출력
    for idx, (pokemon, value) in enumerate(result.items(), start=1):

        print(f"{idx}. {value['name']}")

    # 다음 단계 넘길 데이터
    selected_pokemon_data = result
    print(result)

    print("\n조회 완료")