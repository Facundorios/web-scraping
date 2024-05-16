# Web Crawler en Python

Este proyecto es un web crawler implementado en Python que recorre un sitio web, extrae todas las etiquetas `<a>` con sus respectivos enlaces, y accede a cada página enlazada. Por cada enlace encontrado, obtiene todas las etiquetas `<h1>` y `<p>` y las almacena en un archivo JSON.

## Definición de Web Crawler

Un web crawler, también conocido como araña web o rastreador web, es un programa informático diseñado para explorar automáticamente la World Wide Web de manera metódica y sistemática. Utiliza algoritmos para navegar por las páginas web, recopilar información y seguir enlaces a otras páginas.

## Aplicaciones de un Web Crawler

### Recuperación de Información
Los motores de búsqueda utilizan web crawlers para indexar páginas web y recopilar información sobre el contenido de estas páginas, permitiendo a los usuarios realizar búsquedas efectivas.

### Monitoreo y Análisis de Contenido
Las empresas pueden utilizar web crawlers para monitorear la web en busca de contenido relevante sobre su marca, productos o competidores, facilitando análisis de mercado y decisiones informadas.

### Obtención de Datos
Los web crawlers pueden extraer datos específicos de sitios web, como precios de productos, información de contacto o noticias, útiles para análisis de datos, investigación de mercado o creación de bases de datos.

## Criterios del Proyecto

- **Funcionalidad:** El web crawler debe recorrer el sitio web de manera efectiva, extraer todas las etiquetas `<a>` y obtener el contenido completo de las páginas enlazadas, almacenando la información en un archivo JSON.
- **Manejo de Errores:** El programa debe manejar adecuadamente errores como páginas no encontradas, errores de conexión o problemas de formato de HTML.
- **Legibilidad y Organización del Código:** El código debe estar bien organizado y estructurado, con nombres descriptivos de variables y funciones.
- **Presentación del Trabajo Práctico:** La presentación debe realizarse en un repositorio público de GitHub.

## Objetivo

Implementar un web crawler en Python que recorra un sitio web, extraiga todas las etiquetas `<a>` con sus respectivos enlaces y acceda a cada página enlazada. Para cada enlace encontrado, se deben obtener todas las etiquetas `<h1>` y `<p>` y almacenarlas en un archivo JSON. Si no se encuentran dichos elementos, guardar el array como vacío.

### Ejemplo de Formato JSON Esperado

```json
{
    "https://example.com/pagina1": ["<h1>Titulo 1</h1>", "<p>Texto parrafo</p>"],
    "https://example.com/pagina2": ["<h1>Titulo 1</h1>"],
    "https://example.com/pagina3": []
}
```

## Instalación y Uso

### Prerrequisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Configuración del Entorno Virtual

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. A continuación se explica cómo crear y activar un entorno virtual.

1. **Crear un entorno virtual**

   ```sh
   python -m venv nombre_del_entorno
   ```

2. **Activar el entorno virtual**

   - En Windows:

     ```sh
     .\nombre_del_entorno\Scripts\activate
     ```

   - En macOS y Linux:

     ```sh
     source nombre_del_entorno/bin/activate
     ```

### Instalación de Dependencias

Instalar las dependencias necesarias usando `pip`:

```sh
pip install requests beautifulsoup4
```

### Ejecución del Web Crawler

Para ejecutar el web crawler, use el siguiente comando:

```sh
python nombre_del_archivo.py
```

## Estructura del Proyecto

- `nombre_del_archivo.py`: Contiene el código principal del web crawler.
- `datos_extraidos.json`: Archivo JSON donde se almacenan los datos extraídos.

## Código del Proyecto

```python
import requests
from bs4 import BeautifulSoup
import json

def obtener_texto_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.RequestException, requests.exceptions.HTTPError) as e:
        print(f"Error al obtener texto del HTML: {e}")
        return None
    return response.text

def extraer_urls(html_text):
    try:
        sopa = BeautifulSoup(html_text, "html.parser")
        etiquetas_a = sopa.find_all("a")
        urls = [
            a.get("href")
            for a in etiquetas_a
            if str(a.get("href")).startswith("https://store.steampowered.com/")
        ]
    except Exception as e:
        print(f"Error al extraer las urls: {e}")
        return []
    return urls

def extraer_contenido_sitioweb(url_inicial):
    html_text = obtener_texto_html(url_inicial)
    if html_text is None:
        return {}
    urls = extraer_urls(html_text)

    datos_extraidos = {}

    for url in urls:
        html_text = obtener_texto_html(url)
        if html_text is None:
            continue
        sopa = BeautifulSoup(html_text, "html.parser")
        obtener_etiquetas_h1_y_ps = [
            str(etiqueta) for etiqueta in sopa.find_all(["h1", "p"])
        ]
        datos_extraidos[url] = obtener_etiquetas_h1_y_ps
    return datos_extraidos

almacenar_datos = extraer_contenido_sitioweb("https://store.steampowered.com/")
with open("datos_extraidos.json", "w") as f:
    json.dump(almacenar_datos, f)
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, cree un *fork* del repositorio, realice sus cambios y envíe una *pull request* para su revisión.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.