from flask import Flask, jsonify, request
from api.password_module import  password_generator

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "This is my API"
    })

@app.route("/password_generator")
def get_password():
    password_length = request.args.get("len")
    password = password_generator(password_length)
    return  jsonify({
        "password": password
    })

#if __name__ == "__main__":
    #app.run(port=9000, debug=True)