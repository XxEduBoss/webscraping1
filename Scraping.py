import requests
import bs4


def web_scraping():

    # Paso 1 --> Tomar el código HTML de la página.
    html = requests.get("https://www.tiendanimal.es/perros/pienso-para-perros/")

    # Paso 2 --> Convertir nuestro hmtl en una sopa.
    soup = bs4.BeautifulSoup(html.content, "html.parser")

    # Paso 3 --> Crearnos un diccionario con la estructura.
    plantilla = {
        "imagen": None,
        "nombre": None,
        "precio": None,
        "marca": None
    }

    # Paso 4 --> Utilizar los métodos de bs4 (Encontrar los datos que quiero obtener).
    perros = soup.find_all("div", {"class": "col-sm-6 col-md-6 col-lg-4 col-xl-3 tile-col p-2"})

    lista_perros = []

    for perro in perros:

        # Creamos una copia del diccionario plantilla.
        dic_perros = plantilla.copy()

        # Buscar los campos y asignarlos en el diccionario.

        # IMAGEN
        if perro.find("img", {"class": "isk-card-product__img"})["src"] == None:
            dic_perros["imagen"] = "Sin Imagen"
        else:
            dic_perros["imagen"] = perro.find("img", {"class": "isk-card-product__img"})["src"]

        # NOMBRE
        if perro.find("p", {"class": "isk-card-product__title__description ta-product-card__title__description gtm-product-name"}) == None:
            dic_perros["nombre"] = "Sin Nombre"
        else:
            dic_perros["nombre"] = perro.find("p", {"class": "isk-card-product__title__description ta-product-card__title__description gtm-product-name"}).text.replace("\n", "")

        # PRECIO
        if perro.find("span", {"class": "value ta-product-card__price"}) == None:
            dic_perros["precio"] = "Sin Precio"
        else:
            dic_perros["precio"] = perro.find("span", {"class": "value ta-product-card__price"}).text.replace("\n", "")

        #MARCA
        if perro.find("p", {"class": "isk-card-product__title__name js-product-tile-brand"}) == None:
            dic_perros["marca"] = "Sin Marca"
        else:
            dic_perros["marca"] = perro.find("p", {"class": "isk-card-product__title__name js-product-tile-brand"}).text

        # Añadir el jugador a mi lista de jugadores.

        lista_perros.append(dic_perros)

    return lista_perros
    print("Web Scraping finalizado")

web_scraping()