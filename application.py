from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Flask App with Github Action"


if __name__ == "__main__":
    app.run("localhost", "5001")
