import Movie_class
import tomatoes


toy_story = Movie_class.Movie("Toy Story",
                              "Story of toys",
                              "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                              "https://www.youtube.com/watch?v=vwyZH85NQC4")
#toy_story.show_poster()

avatar = Movie_class.Movie("Avatar",
                           "A marine on an alien planet",
                           "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                           "https://www.youtube.com/watch?v=uZNHIU3uHT4")
#print avatar.storyline
#avatar.show_trailer()

gladiator = Movie_class.Movie("Gladiator",
                              "Movie about brave gladiators",
                              "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                              "https://www.youtube.com/watch?v=AxQajgTyLcM")

#print gladiator.poster_image_url
#gladiator.show_poster()

braveheart = Movie_class.Movie("BraveHeart",
                              "William Wallace",
                              "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                              "https://www.youtube.com/watch?v=WtO3CsleMDg")

king_kong = Movie_class.Movie("King Kong",
                              "The story of giant monkey",
                              "https://upload.wikimedia.org/wikipedia/en/6/6a/Kingkong_bigfinal1.jpg",
                              "https://www.youtube.com/watch?v=9extfjDZCts")

how_to_train_your_dragon = Movie_class.Movie("How To Train Your Dragon",
                              "The story of the boy that trains a special dragon",
                              "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                              "https://www.youtube.com/watch?v=fVr3J3Ddz70")

movies = [toy_story, avatar, gladiator, braveheart, king_kong, how_to_train_your_dragon]
tomatoes.open_movies_page(movies)
#print Movie_class.Movie.VALID_RATINGS
#print Movie_class.Movie.__doc__
