import requests
from bs4 import BeautifulSoup

url = "https://www.eldestapeweb.com/"

response = requests.get(url)

html_text = response.text

sopita = BeautifulSoup(html_text, "html.parser")

etiquetas_a = sopita.find_all("a")

for etiqueta_a in etiquetas_a:
    
    etiquetas_a_link = str(etiqueta_a.get("href")) 
    
    
    if etiquetas_a_link.startswith("/"):
        
        etiquetas_a_link = "https://www.eldestapeweb.com" + etiquetas_a_link
        
        response2 = requests.get(etiquetas_a_link)

        html_text2 = response2.text

        sopita2 = BeautifulSoup(html_text, "html.parser")

        h1 = sopita2.find_all("h1")
        p = sopita2.find_all("p")
        
        

# print(etiquetas_h1)




