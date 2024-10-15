#!/usr/bin/python3
"""Module"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

PORT = 5000

users = {}


@app.route("/")
def home():
    """Func"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """func"""
    user_list = list(users.keys())
    return jsonify(user_list)


@app.route("/status")
def status():
    """func"""
    return "OK"


@app.route("/users/<username>")
def retrieve_users(username):
    """func"""
    if users.get(username):
        return users.get(username)

    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """func"""
    new_user = request.get_json()
    username = new_user.get('username')

    if not username:
        return jsonify('{"error":"Username is required"}'), 400

    else:
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
