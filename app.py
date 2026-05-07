from flask import Flask, render_templates

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>ㅎㅇㅎㅇ</h1>"



if __name__ == "__main__":
    app.run(debug=True)