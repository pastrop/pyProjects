# MVP Backend
import time
from flask import Flask, jsonify, request, url_for, redirect
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import sqlite3
import instance.config as appendConfig
import requests
#from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

print(appendConfig.conf['SECRET_KEY'])

# jwt Object
jwt = JWTManager(app)

#SQLite Setup - Placeholder for a real database

conn=sqlite3.connect("user.db")
cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS store(id TEXT, password TEXT)')
conn.commit()
conn.close()

# App Body:

@app.route("/", methods=['GET','POST'])

def login():
	''' login only, no account creation'''
	if request.method == 'GET':
		return "Kalepa Test Site"
	if not request.is_json:
		return jsonify({"msg": "Missing JSON in request"}), 400

	username = request.json.get('username', None)
	password = request.json.get('password', None)
	if not username:
		return jsonify({"msg": "Missing username parameter"}), 400
	if not password:
		return jsonify({"msg": "Missing password parameter"}), 400
	if username != 'test' or password != 'test':
		return jsonify({"msg": "Bad username or password"}), 401
	# Identity can be any data that is json serializable
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200

@app.route("/analytics", methods=['GET'])
def analytics():
	'''staff related to pulling data from Atlas Mongo goes here as well as business rules we 
	will use to access form submossions '''
	pass

@app.route("/upload", methods=['GET'])
def upload():
	'''file upload and, evetual saving, PDF format only'''
	pass



if __name__ == '__main__':
    app.run(debug=True)
    