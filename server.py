from flask import Flask

app = Flask(__name__)


@app.route("/login")
def login():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)