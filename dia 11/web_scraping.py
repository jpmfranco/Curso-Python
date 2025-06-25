import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2024/07/buscas-trabajo-y-no-has-certificado-en.html")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# print(sopa.select("title")[0].get_text())
# parrafo_esp  = sopa.select("p")[0].get_text()
# columna_lateral = sopa.select(".r-snippetized")

# for p in columna_lateral:
#     print(p.get_text())
imagenes = sopa.select("img")[1]['src']
print(imagenes)

imagencurso1 = requests.get(imagenes)
# print(imagencurso1.content)
f = open("mi_imagen.jpg", "wb")
f.write(imagencurso1.content)
f.close()