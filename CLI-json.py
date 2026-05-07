import requests
import json

BASE_URL = "https://pokeapi.co/api/v2"
cache = {
    "pokemon": {}
}
#진화트리
def get_evolution_chain(pokemon_name):
    species_res = requests.get(
        f"{BASE_URL}/pokemon-species/{pokemon_name}"
    )
    species_data = species_res.json()
    evo_url = species_data["evolution_chain"]["url"]
    evo_data = requests.get(evo_url).json()
    chain = evo_data["chain"]
    evolution_list = []
    while True:
        evolution_list.append(chain["species"]["name"])
        if chain["evolves_to"]:
            chain = chain["evolves_to"][0]
        else:
            break
    return evolution_list
#포켓몬 json
def save_pokemon_json(pokemon_name):
    if pokemon_name in cache["pokemon"]:
        print("이미 파일에 있음")
        return
    res = requests.get(f"{BASE_URL}/pokemon/{pokemon_name}")
    if res.status_code != 200:
        print("포켓몬 없음")
        return
    data = res.json()
    # 타입
    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])
    # 기술
    moves = []
    for m in data["moves"][:5]:
        moves.append(m["move"]["name"])
    # 진화트리
    evolution = get_evolution_chain(pokemon_name)
    # json 
    cache["pokemon"][pokemon_name] = {
        "name": data["name"],
        "types": types,
        "moves": moves,
        "evolution": evolution
    }
    print(f"{pokemon_name} 불러오는중..")
# 초기값 세팅
def setting_pokemon() :
     #  불러올 포켓몬수
     limit = 151
     res = requests.get(
        f"{BASE_URL}/pokemon?limit={limit}"
    )
     data = res.json()
     pokemon_list = data["results"]
     for pokemon in pokemon_list:
        pokemon_name = pokemon["name"]
        save_pokemon_json(pokemon_name)
def save_json():
    with open("pokemon_cache.json", "w", encoding="utf-8") as f:
        json.dump(
            cache,
            f,
            ensure_ascii=False,
            indent=4
        )
    print("JSON 저장 완료")
def load_json():
    global cache
    try:
        with open("pokemon_cache.json", "r", encoding="utf-8") as f:
            cache = json.load(f)
        print("JSON 불러오기 완료")
        return cache
    except FileNotFoundError:
        print("저장된 JSON 없음")



data = load_json()
setting_pokemon()
save_json()