from urllib.parse import urlencode
from urllib.request import urlopen, Request

httpresponse = urlopen('https://www.example.com')
print(type(httpresponse))      # <class 'http.client.HTTPResponse'>

body = httpresponse.read()
print(body)


# post
data = {
    'email': 'ydhwa_18@naver.com',
    'password': '1234',
    'name': '양동화'
}
data = urlencode(data).encode('utf-8')
print(data)

# Request객체가 있어야 POST 방식으로 보낼 수 있다.
request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')
# request.add_header('cookies:jsessionid=165413548643')     # session id hijacking

httpresponse = urlopen(request)
print(httpresponse.read())
