import time
from flask import Flask, jsonify, request, url_for, redirect
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import sqlite3
import instance.config as appendConfig
import routes as EndPoints

app = Flask(__name__)

api = Api(app)
# app.config.from_envvar('SETTINGS')
app.config['SECRET_KEY'] = 'super-secret'
print(appendConfig.conf['SECRET_KEY'])

# jwt Object
jwt = JWTManager(app)

#SQLite Setup

conn=sqlite3.connect("user.db")
cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS store(id TEXT, password TEXT)')
conn.commit()
conn.close()

# ENDPOINTS:
api.add_resource(EndPoints.HelloWorld, '/', endpoint = 'Hello')
api.add_resource(EndPoints.Dashboard, '/dashboard', endpoint = 'Dashboard')
api.add_resource(EndPoints.Fileupload, '/fileUpload', endpoint = 'File')
api.add_resource(EndPoints.Protected, '/protected',  endpoint = 'Protected')
api.add_resource(EndPoints.Signup, '/protected',  endpoint = 'Signup')


if __name__ == '__main__':
    app.run(debug=True)
    