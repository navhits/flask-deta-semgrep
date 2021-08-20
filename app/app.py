from flask import Flask, request, jsonify
from deta import Deta
from app.config import DETA_API_KEY

# deta = Deta(DETA_API_KEY) # Recommended to use enviornment variable
deta = Deta('a0wl7mn4_ALeG5ETfDGwFLHSDtEoQUaC3CuSfuQTK') # For testing we will hardcode the key
db = deta.Base('userDB')  # Name a database. If the DB doesn't exist, it will be created

app = Flask(__name__)

@app.route('/users/', methods=["POST"])
def create_user():
    name = request.json.get("name")
    department = request.json.get("department")
    
    user = db.insert({
        "name": name,
        "department": department
    })

    return jsonify({"status": "created", "user": user})

@app.route("/users/", methods=["GET"])
def list_users():
    res = db.fetch()
    items = res.items
    return jsonify({"status": "found", "users": items}) if items else jsonify({"status": "not found"})

@app.route("/users/<key>")
def get_user(key):
    user = db.get(key)
    return jsonify({"status": "found", "user": user}) if user else jsonify({"status": "not found"})

@app.route("/users/<key>", methods=["PUT"])
def update_user(key):
    name = request.json.get("name")
    department = request.json.get("department")

    user = db.put({
        "name": name,
        "key": key,
        "department": department
    })
    return jsonify({"status":"updated", "user": user})

@app.route("/users/<key>", methods=["DELETE"])
def delete_user(key):
    db.delete(key)
    return jsonify({"status": "deleted"})
