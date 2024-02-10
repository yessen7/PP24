movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def is_high_score(movie):
    return movie["imdb"] > 5.5


def high_score_movies(movies):
    return [movie for movie in movies if is_high_score(movie)]


def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]


def average_imdb_score(movies):
    if not movies:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)


def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)


single_movie = {"name": "Hitman", "imdb": 6.3, "category": "Action"}


print(is_high_score(single_movie))
high_score_list = high_score_movies(movies)
print(high_score_list)

romance_movies = movies_by_category(movies, "Romance")
print(romance_movies)

average_score_all = average_imdb_score(movies)
print(f"Average IMDB score for all movies: {average_score_all}")

average_score_romance = average_imdb_score_by_category(movies, "Romance")
print(f"Average IMDB score for Romance movies: {average_score_romance}")

