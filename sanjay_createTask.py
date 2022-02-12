import pandas as pd
import requests
import re
from scipy import spatial
def recommendation(genres):
    if genres == []:
        output = {
            0: {
                "title":"Please Select Genres",
                "poster":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fthefactfactor.com%2Ffacts%2Fpure_science%2Fphysics%2Ferrors-and-their-types%2F9495%2F&psig=AOvVaw1f_QhudjPQGawlDD786uWL&ust=1644299433670000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjJ0fDy7PUCFQAAAAAdAAAAABAD",
                "plot": "We can not provide accurate recommendations without having information from the form.",
            }
        }
        return output
    movies = pd.read_csv('movieData/movies.csv')
    movies.set_index("movieId",inplace=True, drop=True)
    dtype_dic= {'imdbId': str,
                'tmdbId' : str}

    links = pd.read_csv("movieData/links.csv", dtype = dtype_dic)
    links.set_index("movieId",inplace=True,drop=True)
    ratings = pd.read_csv("movieData/ratings.csv")
    newRatings = ratings.groupby("movieId")["rating"].agg("count")
    ratings = ratings.groupby("movieId").mean()
    del ratings["userId"]
    del ratings["timestamp"]
    for index in range(1,len(newRatings)):
        try:
            if newRatings[index] <= 30:
                ratings.drop(
                    labels=[index],
                    axis=0,
                    inplace=True
                )
        except:
            continue
    movies['title'] = movies['title'].str.lower()
    results = {}
    for x in range(2,len(movies)):
        try:
            rating = (ratings.loc[x,"rating"])
            x_genres = movies.loc[x,"genres"].split("|")
            common = len(set(x_genres).intersection(genres))
            yearRegex = re.search("\((\d\d\d\d)\)","Toy Story (1995)")
            year = int(yearRegex.groups()[0])
            if common>=3 and rating >=3:
                results[x] = spatial.distance.cosine([rating,common,year],[5,5,2022])
        except:
            continue
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
    results = {k:results[k] for k in list(results.keys())[:10]}
    output = {}
    for x in list(results.keys())[:10]:
        tmdbId = links.loc[x,"tmdbId"]
        movie_data = requests.get("https://api.themoviedb.org/3/movie/{id}?api_key=da1fef95c8fac680ac2ada0bcce7339b".format(id=tmdbId)).json()
        output[tmdbId] = {
            "title":movie_data["title"],
            "poster":"https://image.tmdb.org/t/p/w500" + movie_data["poster_path"],
            "plot": movie_data["overview"],
        }
    return output

