import requests as r
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

page = r.get(url=URL).text
bs = BeautifulSoup(page, "html.parser")
movies_list = []

titles = bs.find_all(name="h3", class_ = "title")

for name in bs.find_all(name="h3", class_ = "title"):
    movies_list.append(name.text)

print(movies_list)

for item in reversed(movies_list):
    try:
        with open(file="list_of_movies.txt", mode="a") as file:
            file.write(f"{item}\n")
    except FileNotFoundError:
        with open(file="list_of_movies.txt", mode="w") as file:
            file.write(f"{item}\n")


#Create a movies.txt file that lists out all movies with numbers + movie title