import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "https://www.imdb.com/title/tt0114709/",
                        "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

school = media.Movie("School of Rock",
                     "https://www.imdb.com/title/tt0332379/",
                     "https://m.media-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


ratatouille = media.Movie("Ratatouille",
                        "https://www.imdb.com/title/tt0382932/",
                        "https://m.media-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")


midnight_paris = media.Movie("Midnight in Paris",
                        "https://www.imdb.com/title/tt1605783/",
                        "https://m.media-amazon.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")


hunger_games = media.Movie("Hunger Games",
                        "https://www.imdb.com/title/tt1392170/",
                        "https://m.media-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, school, ratatouille, midnight_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
