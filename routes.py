import os
from flask_restful import Resource, reqparse
from flask import request, url_for, redirect
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# Index page placeholder
class HelloWorld(Resource):
    def get(self):
    	return {'hello':'world'}

# Dashboard paceholder
class Dashboard(Resource):
	def get(self):
		return {'Dashboard': 'page'}

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('framework')
		parser.add_argument('language')
		args = parser.parse_args()
		framework = args['framework']
		language = args['language']
		return '''cool staff on {} brought to you by {}'''.format(framework, language)

# File upload functionality
class Fileupload(Resource):
	def post(self):
		if 'testfile' not in request.files:
			return ''''no files!'''
		file = request.files['testfile']
		filename = 'test.txt'
		file.save(os.path.join('tmp/', filename))
		return ''' upload success!'''

# Provide methods to create access tokens at login or signup. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
class Login(Resource):
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
		return jsonify(access_token=access_token), 200

class Signup(Resource):
	def Signup():
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

# Protected endpoint placehoolder
# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
class Protected(Resource):
	@jwt_required
	def protected():
	# Access the identity of the current user with get_jwt_identity	
		current_user = get_jwt_identity()
		if current_user:
			return jsonify(logged_in_as=current_user), 200
		else:
			return redirect(url_for('Hello'))

	
	
	
