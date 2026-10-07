# Laborator: funcții, metode și importuri pe web
# Student: <Gorceag Vlad>
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import webtools

#webtools.get_title(webtools.fetch(BASE_URL).text)

#ex45
from webtools import get_title, security_headers
from webtools import DEFAULT_HEADERS
# Daca main.py de asemenea defineste get_Title(), functia locala va avea prioritate asupra get_title() care a fost importat
print(DEFAULT_HEADERS)