import requests

response = requests.get('https://pypi.org/')   

#print(response.text)
#print(response.status_code)

payload = { "q": "tu busqueda" }
response = requests.get("https://pypi.org", params=payload)
print(response.url) # https://pypi.org/?q=astro