import omdb
import auth
import pandas as pd

omdb.set_default('apikey', auth.api_key)

movies = [
    { 'title': 'It Follows', 'year': 2014 },
    { 'title': 'The Last Shift', 'year': 2014 },
    { 'title': 'The Conjuring', 'year': 2013 },
    { 'title': 'The Conjuring 2', 'year': 2016 },
    { 'title': 'Hereditary', 'year': 2018 },
    { 'title': 'The Ritual', 'year': 2017 },
    { 'title': 'Cargo', 'year': 2017 },
    { 'title':'It Comes at Night', 'year': 2017 },
    { 'title': 'It', 'year': 2017 },
    { 'title': 'I Am the Pretty Thing That Lives in the House', 'year': 2016 },
    { 'title': 'The Void', 'year': 2016 },
    { 'title': 'Calibre', 'year': 2018 },
    { 'title': 'Ravenous', 'year': 2017 },
    { 'title': 'Train To Busan', 'year': 2016 },
    { 'title': 'The Wailing', 'year': 2016 },
    { 'title': 'Parasite', 'year': 2019 },
    { 'title': '28 Days Later', 'year': 2002 },
    { 'title': 'The Witch', 'year': 2015 },
    { 'title': 'A Quiet Place', 'year': 2018 },
    { 'title': 'Veronica', 'year': 2017 },
    { 'title': 'Creep', 'year': 2014 },
    { 'title': 'The Open House', 'year': 2018 },
    { 'title': 'A Dark Song', 'year': 2016 }
]

desiredKeys = ['title', 'year', 'genre', 'ratings']
movieRatings = []
for d in movies:
    res = omdb.get(title=d['title'], year=d['year'], fullplot=False, tomatoes=True)
    if res['response']:
        temp = { key: res[key] for key in desiredKeys }
        movieRatings.append(temp)

# https://stackoverflow.com/questions/54017178/pandas-flatten-a-column-which-is-a-list-of-dictionaries
newList = []
for movie in movieRatings:
    temp = {}
    for d in movie['ratings']:
        temp[list(d.values())[0]] = list(d.values())[1]
    movie.pop('ratings', None)
    movie = {**movie, **temp}
    newList.append(movie)

movieDF = pd.DataFrame(newList, columns = [key for key in newList[0].keys()], dtype='object')
# print(movieDF.head(5))
movieDF.to_csv('movie_ratings.csv', index=False)
