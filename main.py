import requests
from bs4 import BeautifulSoup
import json


def obtener_texto_html(url):
    try:
        response = requests.get(url)
        # raise_for_status: metodo que lanza una excepcion si el servidor nos devuelve un codigo de error
        response.raise_for_status()
        # RequestsExeption: excepcion que se lanza si hay un error en la peticion
        # HTTPError: excepcion que se lanza si el servidor nos devuelve un codigo de error
    except (requests.RequestException, requests.exceptions.HTTPError) as e:
        print(f"Errpr al obtener texto del HTML {e}")
        return None
    return response.text


# print(obtener_texto_html("https://www.eldestapeweb.com"))


# Obtener las urls del html
def extraer_urls(html_text):
    try:
        # BeautifulSoup: clase que se encarga de parsear el texto HTML
        sopa = BeautifulSoup(html_text, "html.parser")
        # busqueda de etriquetas a
        etiquetas_a = sopa.find_all("a")
        # De las etiquetas a, extraemos las urls en forma de array, mediante el metodo get("href"), por cada etiqueta a en etiqueras a, junto al condicional en donde la etiqueta a debe comenzar con el predijo correspondiente
        urls = [
            a.get("href")
            for a in etiquetas_a
            if str(a.get("href")).startswith("https://store.steampowered.com/")
        ]
    # Exeception: excepcion que se lanza si hay un error en la extraccion de las urls
    except Exception as e:
        print(f"Error al extraer las urls:{e}")
        return []
    # Devolver las urls en forma de array.
    return urls


# prueba:
# print(extraer_urls(obtener_texto_html("https://www.eldestapeweb.com")))


def extraer_contenido_sitioweb(url_inicial):
    # definimos el texto de html con la funcion de obtener texto html y elparametro url es el mismo que le pasamos a la funcion scraping
    # Si el html tiene contenido, se extraen las urls
    html_text = obtener_texto_html(url_inicial)
    if html_text is None:
        return {}
    urls = extraer_urls(html_text)

    # Creamos un diccionario vacio
    datos_extraidos = {}

    # for para urls. para cada url, obtener el texto html, posteriormente preguntar si el html tiene contenido, si no tiene contenido, se continua con el siguiente ciclo, si tiene contenido, se parsea el html y se extraen las etiquetas h1 y p, se guardan en una lista y se guardan en el diccionario datos_extraidos
    for url in urls:
        html_text = obtener_texto_html(url)
        if html_text is None:
            continue
        sopa = BeautifulSoup(html_text, "html.parser")
        obtener_etiquetas_h1_y_ps = [
            str(etiqueta) for etiqueta in sopa.find_all(["h1", "p"])
        ]
        datos_extraidos[url] = obtener_etiquetas_h1_y_ps
    # Devolvemos los datos extraidos
    return datos_extraidos


# Almacenamos los datos.
almacenar_datos = extraer_contenido_sitioweb("https://store.steampowered.com/")
# Creamos el archivo.json y con el metodo json.dump guardamos los datos en el archivo.
with open("datos_extraidos.json", "w") as f:
    json.dump(almacenar_datos, f)
