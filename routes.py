import os
from flask_restful import Resource, reqparse
from flask import request, url_for, redirect
from flask_jwt_extended import (
    JWTManager, jwt_required, jwt_optional, create_access_token,
    get_jwt_identity
)
import concurrent.futures
import urllib.request
import requests


URLS = ['https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/todos/2',
        'https://jsonplaceholder.typicode.com/todos/3']

# Index page placeholder
class HelloWorld(Resource):
    def get(self):
    	return {'hello':'world'}

# Dashboard paceholder
class Dashboard(Resource):
	def get(self):
		# Retrieve a single page and report the URL and contents
		def load_url(url, timeout):
			result = requests.get(url, timeout=5).json()
			return result
		# We can use a with statement to ensure threads are cleaned up promptly
		with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		    # Start the load operations and mark each future with its URL
		    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
		    for future in concurrent.futures.as_completed(future_to_url):
		        url = future_to_url[future]
		        try:
		            data = future.result()
		        except Exception as exc:
		            print('%r generated an exception: %s' % (url, exc))
		        else:
		            print('%r page is %d bytes' % (url, len(data)))
		            print(data)  

		return {'Call': 'External APIs'}

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
	def post(self):
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
	def post(self):
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
	@jwt_optional
	def get(self):
	# Access the identity of the current user with get_jwt_identity	
		current_user = get_jwt_identity()
		if current_user:
			return jsonify(logged_in_as=current_user), 200
		else:
			return redirect(url_for('Hello'))


	
	
	
