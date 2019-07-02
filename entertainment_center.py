import media
import fresh_tomatoes

from bs4 import BeautifulSoup
import requests

# list of movies element
movies = []


# Request data for the movie Arrival from the OMDB Api
def get_movie_info(title):
    req = requests.get("http://www.omdbapi.com/?t="+title+"&apikey=4191762b")
    # Check if there is a response from the Api
    if req.status_code == 200:
        data = req.json()
        movie = media.Movie(data["Title"],
                            data["Runtime"],
                            data["Plot"],
                            data["Poster"],
                            get_trailer_url(title))
        movies.append(movie)
    else:
        print("filme nao encontrado")


# Fetch trailer URL for the given movie title using Youtube DOM parsing
def get_trailer_url(title):
    # Use the youtube search results url to find the movie trailer
    response = requests.get("https://youtube.com/results", params={
        'search_query': title+" trailer"
    })

    soup = BeautifulSoup(response.content, "html.parser")

    for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        return "https://youtube.com" + video["href"]


# Creating a list of objects of Movie class
movies_names = ["Arrival", "Interstellar", "A Separation", "Waking Life"]
movies_names.extend(["The Dark Knight", "Dr. Strangelove"])
for i in movies_names:
    print(i)
    get_movie_info(i)

# Generating the HTML file with the list of movies objects
fresh_tomatoes.open_movies_page(movies)
