import json
import requests

BASE_URL = "https://pokeapi.co/api/v2"
CACHE_FILE = "pokemon_cache.json"

cache = {
    "pokemon": {}
}


def request_json(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API 요청 실패: {url}")
        print(e)
        return None


def load_json():
    global cache

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)

        print("JSON 불러오기 완료")
        return cache

    except FileNotFoundError:
        print("저장된 JSON 없음. 새로 생성합니다.")
        return cache


def save_json():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(
            cache,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("JSON 저장 완료")


def get_korean_name(species_data, fallback_name):
    if species_data is None:
        return fallback_name

    for item in species_data.get("names", []):
        if item["language"]["name"] == "ko":
            return item["name"]

    return fallback_name


def get_evolution_chain(evo_url):
    evo_data = request_json(evo_url)

    if evo_data is None:
        return []

    chain = evo_data["chain"]
    evolution_list = []

    while True:
        evolution_list.append(chain["species"]["name"])

        if chain["evolves_to"]:
            chain = chain["evolves_to"][0]
        else:
            break

    return evolution_list


def save_pokemon_json(pokemon_name):
    if pokemon_name in cache["pokemon"]:
        print(f"{pokemon_name} 이미 파일에 있음")
        return

    data = request_json(
        f"{BASE_URL}/pokemon/{pokemon_name}"
    )

    if data is None:
        print(f"{pokemon_name} 불러오기 실패")
        return

    species_data = request_json(
        f"{BASE_URL}/pokemon-species/{pokemon_name}"
    )

    name_ko = get_korean_name(species_data, data["name"])

    types = [
        t["type"]["name"]
        for t in data["types"]
    ]

    moves = [
        m["move"]["name"]
        for m in data["moves"][:5]
    ]

    evolution = []

    if species_data is not None:
        evo_url = species_data["evolution_chain"]["url"]
        evolution = get_evolution_chain(evo_url)

    image = data["sprites"]["other"]["official-artwork"]["front_default"]

    cache["pokemon"][pokemon_name] = {
        "name": name_ko,
        "name_en": data["name"],
        "types": types,
        "moves": moves,
        "evolution": evolution,
        "image": image
    }

    print(f"{name_ko}({pokemon_name}) 불러오기 완료")


def setting_pokemon():
    limit = 151

    data = request_json(
        f"{BASE_URL}/pokemon?limit={limit}"
    )

    if data is None:
        print("포켓몬 리스트 불러오기 실패")
        return

    pokemon_list = data["results"]

    for pokemon in pokemon_list:
        pokemon_name = pokemon["name"]
        save_pokemon_json(pokemon_name)


if __name__ == "__main__":
    load_json()
    setting_pokemon()
    save_json()