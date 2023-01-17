from bs4 import BeautifulSoup
import requests

reponse = requests.get("https://www.imdb.com/list/ls055592025/")
website_html = reponse.text

soup = BeautifulSoup(website_html, "html.parser")

films = [element.getText() for element in soup.select(".lister-item-header a")]
print(films)

text_for_file = ""
for i, film in enumerate(films):
    text_for_file += f"{i+1}) {film}\n"

with open("filmek.txt", "w", encoding="utf-8") as file:
    file.write(text_for_file)
