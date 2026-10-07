# Laborator: funcții, metode și importuri pe web
# Student: <Gorceag Vlad>
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
DEFAULT_HEADERS = {"User-Agent": "WebLab-Gorceag Vlad"}
TIMEOUT = 10  # secunde
import requests
def fetch(url:str,timeout = 10)->requests.Response:
    response = requests.get(url,timeout=timeout)
    return response.status_code 



def get_status(url:str)->int:
    response = requests.get(BASE_URL + url)
    return response.status_code
def get_title(html:str):
    """Get the title from a page by getting text content from <title> tags."""
    findtext = html.find("<title>")
    endtext = html.find("</title>")
    title = html[findtext + len("<title>"):endtext]
    cleantitle = title.strip()
    print(cleantitle)
def security_headers(url:str)->list:
    headers_list = ["Strict-Transport-Security","Content-Security-Policy","X-Frame-Options","X-Content-Type-Options","Referrer-Policy"]
    response = requests.get(url)
    result = []

    for i in range(len(headers_list)):
        if response.headers.get(headers_list[i]):
            result.append({
                "antet":headers_list[i],
                "valoare":True
                
            })
        else:
            result.append({
                "antet":headers_list[i],
                "valoare":False                
            })
    return result

if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
    