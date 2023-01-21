from flask import Flask

app = Flask(__name__)


@app.route("/members")
def memebers():
    return {"memebers" :  ["members", "eee", "eeee"]}


if __name__ == "__main__":
    app.run(debug=True)