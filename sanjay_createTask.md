{% include nav_jekyll.html %}

# Sanjay Create Task

## 3a

### Describe the overall purpose of the program

The overall purpose of the program is to provide the user with a set of movie recommendations, personalized and based on the users preferences, be it what genres the user enjoys, or how old the user is willing to see. The program is meant to take this factors into account and provide recommendations that the user will like. 

### Describe what functionality of the program is in the Video
The entire program is demonstrated in the video. In the video, the user selects the genres that they wish to view, and then selects how recent the movie should be. After submitting these preferences, a list of movies appears on the screen. 

### Describe the input and output in the video
The input is the genre choices and recency requirement, the output is the list of movies. 

## 3b

### The first code segment shows how data is stored in a list

``` py
    for x in range(2,len(movies)):
        try:
            rating = (ratings.loc[x,"rating"])
            x_genres = movies.loc[x,"genres"].split("|")
            common = len(set(x_genres).intersection(genres))
            yearRegex = re.search("\((\d\d\d\d)\)",movies.loc[x,"title"])
            year = int(yearRegex.groups()[0])
            if common>=3 and rating >=3 and 2022-year < age:
                results[x] = spatial.distance.cosine([rating,common,year],[5,5,2022])
        except:
            continue

```
### Show the Data in the list being used

```py
    for x in list(results.keys())[:10]:
        tmdbId = links.loc[x,"tmdbId"]
        movie_data = requests.get("https://api.themoviedb.org/3/movie/{id}?api_key={api-key}".format(id=tmdbId)).json()
        output[tmdbId] = {
            "title":movie_data["title"],
            "poster":"https://image.tmdb.org/t/p/w500" + movie_data["poster_path"],
            "plot": movie_data["overview"],
        }
```

### The name of the list
The dictionary being used is called "results". 

### Describe what the data in the list represents

The data in the list represents each movie in the database of thousands of movies, along with its corresponding similarity constant. The similarity constant indicates how similar it is to the ideal movie.

### Explain complexity management

Without the dictionary being used, the program would be exceptionally difficult to write, as in order for the program to be written, this dictionary must be sorted. Without it being sorted, the ratings can't be ranked. This sorting cannot occur without a dictionary to hold the values. 

## 3c

### Paste a Student-Developed Procedure
```py
def recommendation(genres,age=None):
    if genres==None or age==None:
        output = {}
        return output
    movies = readData("movieData/movies.csv","movieId")
    dtype_dic= {'imdbId': str,
                'tmdbId' : str}

    links = readData("movieData/links.csv","movieId")
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
            yearRegex = re.search("\((\d\d\d\d)\)",movies.loc[x,"title"])
            year = int(yearRegex.groups()[0])
            if common>=3 and rating >=3 and 2022-year < age:
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
```
###  Implementation
```py
    if age==None or age < 10:
        output = recommendation(genres,None)
```

### General Description
The procedure takes a set of inputs from the user, describing their preferences, and returns 10 movies the user may like. 


### Explanation
Pre existing databases are converted to easy-to-use formats and parsed (based on number of ratings.) After this, the movies dataset is iterated through, and the genres, ratings, and year for the movie are all extracted. Built in pandas functions are used for the first two, while ReGex is used to extract the year (since it is a part of the movie title). Then, if the movie has more than 3 genres in common, a rating of more than 3/5, and if the movie is recent enough (based on user input), we consider it for the next step. In the next step, cosine similarity is used to determine the similarity between this movies stats (common genres, rating, recency), and the ideal movie (all genres in common, 5 stars, made in 2022). After this, the dictionary is sorted by ascending distance (big number means less similar). The top 10 movies are selected, and their unique IDs are used to get more data using the tMDB API. A dictionary with all this  is returned to be displayed to the user. 

## 3d

### First Implementation
```py
    if age==None or age < 10 or genres==None or genres ==[]:
        output = recommendation(None,None)
```

### Second Implementation
```py
output = recommendation(genres,age)
```

### Input for First
The first procedure takes None types as parameters, as the user has failed to provide proper inputs (invalid or none). 

### Input for second
The second procedure takes two variables as inputs. The first variable is "genres". This is a list of genres the user likes, provided by the user through an HTML form. The second input is an integer value for age, provided by the user. This is an integer represeting how recent the user wants the movies to be.

### Output for first
The result of the first call is an empty dictionary, since both parameters were None types, since user inputs were invalid. 

### Output for second
The output for the second dynamically changes each time the program is executed, as it depends on the input parameters, which in turn depend on what the user passes in. However, in all cases, the program will output a dictionary with 10 keys. Each key will be a separate movie id. Each corressponding value will be another dictionary. This dictionary will have items for the movie title, the movie description/plot, and an image link for the movies poster. These will all be used by the HTML to display a list of movies with neccessary data to the user. 
