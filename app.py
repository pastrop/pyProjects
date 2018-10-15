import time
from flask import Flask, jsonify, request, url_for, redirect
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import instance.config as appendConfig
import routes as EndPoints

app = Flask(__name__)

api = Api(app)
# app.config.from_envvar('SETTINGS')
app.config['SECRET_KEY'] = 'super-secret'
print(appendConfig.conf['SECRET_KEY'])

# USING JWT_EXTENDED MODULE

jwt = JWTManager(app)

# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
'''@app.route('/login', methods=['POST'])
def login():
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
    return jsonify(access_token=access_token), 200'''

api.add_resource(EndPoints.HelloWorld, '/', endpoint = 'Hello')
api.add_resource(EndPoints.Dashboard, '/dashboard', endpoint = 'Dashboard')
api.add_resource(EndPoints.Fileupload, '/fileUpload', endpoint = 'File')
api.add_resource(EndPoints.Protected, '/protected',  endpoint = 'Protected')
api.add_resource(EndPoints.Signup, '/protected',  endpoint = 'Signup')

if __name__ == '__main__':
    app.run(debug=True)
