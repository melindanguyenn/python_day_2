# testing routes in postman with GET and POST routes

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "POST"):
        some_json = request.get_json()
        return jsonify({"you sent": some_json}), 201
    else:
        return jsonify({"about": "hello!"})

if __name__ == "__main__":
    app.run(debug=True)