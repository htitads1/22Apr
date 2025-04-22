from flask import Flask, jsonify

app = Flask(__name__)



@app.route("/", methods=["GET"])
def say_welcome():
    return jsonify({"msg": "Welcome from Flask"})

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)