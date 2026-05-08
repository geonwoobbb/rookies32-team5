import json

def load_pokemon_data(file_path):
    try:
        with open("pokemon_cache.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return None


type_list = [ "grass","fire", "water", "bug", "normal","poison", "electric", "ground", "fairy", "fighting",
    "psychic", "rock", "ghost", "ice", "dragon", "steel", "flying", "dark"]
print(f"타입: {type_list}")
print(f"보고싶은 포켓몬 타입을 고르세요: ")

def filter_by_type(data_dict, target_type):
    result = []
    target_data = data_dict.get("pokemon", {})

    for poke_id in target_data:
        poke_type = target_data[poke_id]

        if target_type in poke_type["types"]:
            result.append(poke_type["name"])
            
    return result

file_name = 'pokemon_cache.json'
data = load_pokemon_data(file_name)

if data:
    target = input("검색할 타입을 입력하세요 (예: grass, fire): ").lower().strip()
    filtered_list = filter_by_type(data, target)