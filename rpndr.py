import requests, json, jwt
import aiohttp, asyncio
from  aiohttp import web 
#from datetime import datetime, timedelta

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

async def handle(request):
    headers = request.headers.get('Host')
    print(headers)
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

async def do_login(request):
    data = await request.post()
    login = data['login']
    password = data['password']
    payload = {
        'user_id': login
#		'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)   
    }
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_post('/login', do_login)

web.run_app(app)


'''req_url1 = "https://jsonplaceholder.typicode.com/todos/1"
req_url2 = "https://jsonplaceholder.typicode.com/todos/2"
req_url3 = "https://jsonplaceholder.typicode.com/todos/3"


async def fetch(session, url):
	async with session.get(url) as response:
		return await response.json()



async def main():
	result = []
	async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
		result1 = await fetch(session, req_url1)
		result2 = await fetch(session, req_url2)
		result3 = await fetch(session, req_url3)
		result.extend((result1,result2,result3))
	print (result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


async def get_user(request):
    return json_response({'user': str(request.user)})

async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return json_response({'message': 'Token is invalid'}, status=400)

            request.user = User.objects.get(id=payload['user_id'])
        return await handler(request)
    return middleware

app = web.Application(middlewares=[auth_middleware])
app.router.add_route('GET', '/get-user', get_user)




'''

