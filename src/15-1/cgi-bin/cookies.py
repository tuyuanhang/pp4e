"""
创建或使用一个存在用户名的客户端Cookie
"""

import http.cookies, os
cookstr = os.environ.get('HTTP_COOKIE')
cookies = http.cookies.SimpleCookie(cookstr)
usercook = cookies.get('user')

if usercook == None: 
    cookies = http.cookies.SimpleCookie()
    cookies['user'] = "Brian"
    print(cookies)
    greeting = "<p>His name shall be... %s</p>" %cookies["user"]
else:
    greeting = "<p>Welcome back, %s</p>" %usercook.value

print("Content-type: text/html\n")
print(greeting)