# displays to the web browser at "/" or "/(your name)"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello! <h1>helloooo<h1>"

@app.route("/<name>")
def user(name):
    return f"hello {name}"

if __name__ == "__main__":
    app.run(debug=True)