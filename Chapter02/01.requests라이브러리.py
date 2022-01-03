import requests

# get 요청을 통해 response 받음
response = requests.get("https://www.naver.com")

# response body -> content(binary), text(utf-8), json 으로 받아올 수 있음 
html = response.text 
print(html)