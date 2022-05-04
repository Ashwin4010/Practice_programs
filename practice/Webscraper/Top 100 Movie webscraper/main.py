import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/chart/top/")
response.raise_for_status()
soup = BeautifulSoup(response.content,"html.parser")

movie_name = []
year = []
rank = []

movie_data = soup.find_all('div',attrs={"class":"lister-list"})


def main():
    for movie in movie_data:
        name = movie.h3.a.text
        movie_name.append(name)
        print(movie_name)
        year_of_release = movie.h3.find('span',class_="secondaryInfo").text
        year.append(year_of_release)
        print(year)
        movie_rank = movie.h3.find("td",class_="titleColumn").text
        rank.append(movie_rank)
        print(rank)

if __name__ == '__main__':
    main()