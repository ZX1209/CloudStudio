```py
response = requests.post(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    json={'key':'value'},
    headers={'key':'value'},
    auth=('username','password')
    )
# params,[json|data],headers,
response.requests

response.status_code
response.encoding
response.headers

response.content
response.text
requests.json()


```

# 返回状态
response.status_code
__bool__() is an overloaded method on Response.
response.raise_for_status() # HTTPError

# 返回文本
response.text

# 返回 json 数据
response.json()

# 返回元数据
> To see the response’s content in bytes, you use .content:

response.content

# 定制 消息
## params
```py
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'})

requests.get(
     'https://api.github.com/search/repositories',
     params=[('q', 'requests+language:python')])

requests.get(
     'https://api.github.com/search/repositories',
     params=b'q=requests+language:python')
```
## headers
```py
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'})
```


# Other HTTP Methods (requests.[post|put|delete|head|patch|options])
Aside from GET, other popular HTTP methods include POST, PUT, DELETE, HEAD, PATCH, and OPTIONS. requests provides a method, with a similar signature to get(), for each of these HTTP methods:
```py
>>> requests.post('https://httpbin.org/post', data={'key':'value'})
>>> requests.put('https://httpbin.org/put', data={'key':'value'})
>>> requests.delete('https://httpbin.org/delete')
>>> requests.head('https://httpbin.org/get')
>>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
>>> requests.options('https://httpbin.org/get')
Each function call makes a request to the httpbin service using the corresponding HTTP method. For each method, you can inspect their responses in the same way you did before:

>>> response = requests.head('https://httpbin.org/get')
>>> response.headers['Content-Type']
'application/json'

>>> response = requests.delete('https://httpbin.org/delete')
>>> json_response = response.json()
>>> json_response['args']
{}
```
Headers, response bodies, status codes, and more are returned in the Response for each method. Next you’ll take a closer look at the POST, PUT, and PATCH methods and learn how they differ from the other request types.

# The Message Body (requests.post(url,[data|json]={'key',value}))
According to the HTTP specification, POST, PUT, and the less common PATCH requests pass their data through the message body rather than through parameters in the query string. Using requests, you’ll pass the payload to the corresponding function’s data parameter.

data takes a dictionary, a list of tuples, bytes, or a file-like object. You’ll want to adapt the data you send in the body of your request to the specific needs of the service you’re interacting with.

For example, if your request’s content type is application/x-www-form-urlencoded, you can send the form data as a dictionary:
```py
>>> requests.post('https://httpbin.org/post', data={'key':'value'})
<Response [200]>
You can also send that same data as a list of tuples:

>>> requests.post('https://httpbin.org/post', data=[('key', 'value')])
<Response [200]>
If, however, you need to send JSON data, you can use the json parameter. When you pass JSON data via json, requests will serialize your data and add the correct Content-Type header for you.

httpbin.org is a great resource created by the author of requests, Kenneth Reitz. It’s a service that accepts test requests and responds with data about the requests. For instance, you can use it to inspect a basic POST request:

>>> response = requests.post('https://httpbin.org/post', json={'key':'value'})
>>> json_response = response.json()
>>> json_response['data']
'{"key": "value"}'
>>> json_response['headers']['Content-Type']
'application/json'
```
You can see from the response that the server received your request data and headers as you sent them. requests also provides this information to you in the form of a PreparedRequest.

# Inspecting Your Request (response.request[.bady|headers|url])
When you make a request, the requests library prepares the request before actually sending it to the destination server. Request preparation includes things like validating headers and serializing JSON content.

You can view the PreparedRequest by accessing .request:
```py
>>> response = requests.post('https://httpbin.org/post', json={'key':'value'})
>>> response.request.headers['Content-Type']
'application/json'
>>> response.request.url
'https://httpbin.org/post'
>>> response.request.body
b'{"key": "value"}'
Inspecting the PreparedRequest gives you access to all kinds of information about the request being made such as payload, URL, headers, authentication, and more.
```
So far, you’ve made a lot of different kinds of requests, but they’ve all had one thing in common: they’re unauthenticated requests to public APIs. Many services you may come across will want you to authenticate in some way.


# Authentication (requests.get(url, auth=('username', 'pass')))
Authentication helps a service understand who you are. Typically, you provide your credentials to a server by passing data through the Authorization header or a custom header defined by the service. All the request functions you’ve seen to this point provide a parameter called auth, which allows you to pass your credentials.

One example of an API that requires authentication is GitHub’s Authenticated User API. This endpoint provides information about the authenticated user’s profile. To make a request to the Authenticated User API, you can pass your GitHub username and password in a tuple to get():
```py
>>> from getpass import getpass
>>> requests.get('https://api.github.com/user', auth=('username', getpass()))
<Response [200]>
The request succeeded if the credentials you passed in the tuple to auth are valid. If you try to make this request with no credentials, you’ll see that the status code is 401 Unauthorized:

>>> requests.get('https://api.github.com/user')
<Response [401]>
When you pass your username and password in a tuple to the auth parameter, requests is applying the credentials using HTTP’s Basic access authentication scheme under the hood.

Therefore, you could make the same request by passing explicit Basic authentication credentials using HTTPBasicAuth:

>>> from requests.auth import HTTPBasicAuth
>>> from getpass import getpass
>>> requests.get(
...     'https://api.github.com/user',
...     auth=HTTPBasicAuth('username', getpass())
... )
<Response [200]>
Though you don’t need to be explicit for Basic authentication, you may want to authenticate using another method. requests provides other methods of authentication out of the box such as HTTPDigestAuth and HTTPProxyAuth.

You can even supply your own authentication mechanism. To do so, you must first create a subclass of AuthBase. Then, you implement __call__():

import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r
```

requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
Here, your custom TokenAuth mechanism receives a token, then includes that token in the X-TokenAuth header of your request.

Bad authentication mechanisms can lead to security vulnerabilities, so unless a service requires a custom authentication mechanism for some reason, you’ll always want to use a tried-and-true auth scheme like Basic or OAuth.

While you’re thinking about security, let’s consider dealing with SSL Certificates using requests.




# encoding problem handle
Because the decoding of bytes to a str requires an encoding scheme, requests will try to guess the encoding based on the response’s headers if you do not specify one. You can provide an explicit encoding by setting .encoding before accessing .text:

```py
>>> response.encoding = 'utf-8' # Optional: requests infers this internally
>>> response.text
'{"current_user_url":"https:'
```

# HTTPError or other handle
```py
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
```


# 返回 Header
The response headers can give you useful information, such as the content type of the response payload and a time limit on how long to cache the response. To view these headers, access .headers:
```py
>>> response.headers
{'Server': 'GitHub.com', 'Date': 'Mon, 10 Dec 2018 17:49:54 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Status': '200 OK', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '59', 'X-RateLimit-Reset': '1544467794', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept', 'ETag': 'W/"7dc470913f1fe9bb6c7355b50a0737bc"', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': 'E439:4581:CF2351:1CA3E06:5C0EA741'}
# .headers returns a dictionary-like object, allowing you to access header values by key. For example, to see the content type of the response payload, you can access Content-Type:

>>> response.headers['Content-Type']
'application/json; charset=utf-8'
# There is something special about this dictionary-like headers object, though. The HTTP spec defines headers to be case-insensitive, which means we are able to access these headers without worrying about their capitalization:

>>> response.headers['content-type']
'application/json; charset=utf-8'
# Whether you use the key 'content-type' or 'Content-Type', you’ll get the same value.
```


## 使用代理

proxies={'http':'127.0.0.1:1080','https':'127.0.0.1:1080'}

requests.get('http://www.google.com',proxies=proxies)

// ok

# download file
```python
r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
```
> reference:https://realpython.com/python-requests/


Performance
When using requests, especially in a production application environment, it’s important to consider performance implications. Features like timeout control, sessions, and retry limits can help you keep your application running smoothly.

Timeouts
When you make an inline request to an external service, your system will need to wait upon the response before moving on. If your application waits too long for that response, requests to your service could back up, your user experience could suffer, or your background jobs could hang.

By default, requests will wait indefinitely on the response, so you should almost always specify a timeout duration to prevent these things from happening. To set the request’s timeout, use the timeout parameter. timeout can be an integer or float representing the number of seconds to wait on a response before timing out:

>>> requests.get('https://api.github.com', timeout=1)
<Response [200]>
>>> requests.get('https://api.github.com', timeout=3.05)
<Response [200]>
In the first request, the request will timeout after 1 second. In the second request, the request will timeout after 3.05 seconds.

You can also pass a tuple to timeout with the first element being a connect timeout (the time it allows for the client to establish a connection to the server), and the second being a read timeout (the time it will wait on a response once your client has established a connection):

>>> requests.get('https://api.github.com', timeout=(2, 5))
<Response [200]>
If the request establishes a connection within 2 seconds and receives data within 5 seconds of the connection being established, then the response will be returned as it was before. If the request times out, then the function will raise a Timeout exception:

import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')
Your program can catch the Timeout exception and respond accordingly.

The Session Object
Until now, you’ve been dealing with high level requests APIs such as get() and post(). These functions are abstractions of what’s going on when you make your requests. They hide implementation details such as how connections are managed so that you don’t have to worry about them.

Underneath those abstractions is a class called Session. If you need to fine-tune your control over how requests are being made or improve the performance of your requests, you may need to use a Session instance directly.

Sessions are used to persist parameters across requests. For example, if you want to use the same authentication across multiple requests, you could use a session:

import requests
from getpass import getpass

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# You can inspect the response just like you did before
print(response.headers)
print(response.json())
Each time you make a request with session, once it has been initialized with authentication credentials, the credentials will be persisted.

The primary performance optimization of sessions comes in the form of persistent connections. When your app makes a connection to a server using a Session, it keeps that connection around in a connection pool. When your app wants to connect to the same server again, it will reuse a connection from the pool rather than establishing a new one.

Max Retries
When a request fails, you may want your application to retry the same request. However, requests will not do this for you by default. To apply this functionality, you need to implement a custom Transport Adapter.

Transport Adapters let you define a set of configurations per service you’re interacting with. For example, let’s say you want all requests to https://api.github.com to retry three times before finally raising a ConnectionError. You would build a Transport Adapter, set its max_retries parameter, and mount it to an existing Session:

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
When you mount the HTTPAdapter, github_adapter, to session, session will adhere to its configuration for each request to https://api.github.com.

Timeouts, Transport Adapters, and sessions are for keeping your code efficient and your application resilient.

Conclusion
You’ve come a long way in learning about Python’s powerful requests library.

You’re now able to:

Make requests using a variety of different HTTP methods such as GET, POST, and PUT
Customize your requests by modifying headers, authentication, query strings, and message bodies
Inspect the data you send to the server and the data the server sends back to you
Work with SSL Certificate verification
Use requests effectively using max_retries, timeout, Sessions, and Transport Adapters
Because you learned how to use requests, you’re equipped to explore the wide world of web services and build awesome applications using the fascinating data they provide.


```py
    :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
```