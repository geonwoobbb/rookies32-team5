import json
from flask import Flask, render_template

app = Flask(__name__)

# JSON 로드 함수
def load_data():
    with open("pokemon_cache.json", "r", encoding="utf-8") as f:
        return json.load(f)["pokemon"]

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", pokemon=data)


@app.route("/pokemon/<name>")
def detail(name):
    data = load_data()
    pokemon = data.get(name)

    if not pokemon:
        return "포켓몬 없음", 404

    evolution_list = []

    for evo_name in pokemon["evolution"]:
        evo = data.get(evo_name)
        if evo:
            evolution_list.append(evo)

    return render_template(
        "detail.html",
        pokemon=pokemon,
        evolution_list=evolution_list
    )


if __name__ == "__main__":
    app.run(debug=True)