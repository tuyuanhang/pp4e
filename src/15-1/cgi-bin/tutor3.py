#!/usr/bin/python
"""
runs on the server, reads form input, prints HTML;
url=http://server-name/cgi-bin/tutor3.py
"""

import cgi
form = cgi.FieldStorage()  #parse form data
print('Content-type: text/html')

html="""
<TITLE>tutor3.py</TITLE>
<H1>Greetings</H1>
<hr>
<P>%s</P>
<HR>"""

if not 'user' in form:
    print(html % 'who are you?')
else:
    print(html %('Hello, %s.' %form['user'].value))
