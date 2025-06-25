import bs4
import requests

# Crear url sin numero de pagina
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

#Lista de titulos con 4 o 5 estrellas
br = []

#iterar paginas

for p in range(1,51):

    #crear sopa de cada pagina
    result = requests.get(url_base.format(p))
    sopa = bs4.BeautifulSoup(result.text,'lxml')
    book = sopa.select(".product_pod")

    #iterar libros
    for b in book:
        #chequear si tienen 4 o 5 estrellas
        if len(b.select('.star-rating.Four')) != 0 or len(b.select('.star-rating.Five')) != 0:
            
            #guardar titulo en variable
            title = b.select('a')[1]['title']
            print(title)
            #agrega libro a lista
            br.append(title)

for b in br:
    print(b)