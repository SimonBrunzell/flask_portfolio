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

