from json import load


path="movies/mdb.json"
with open(path) as f:
    movies=load(f)


# print(len(movies))
#name of all movies
# movie_names=[m.get("title") for m in movies]

# print(movie_names)
#movie year 2005
# movieyear=[m.get("title")for m in movies if m.get ("year")=="2005"]

# print(movieyear)

#comedy movie

# comedymovies=[m.get("title")for m in movies if "Comedy" in m.get ("genres")]

# print(comedymovies)

#longest duration

# movieduration=[m.get("title")for m in movies if m.get ("runtime")]

# movieduration=max(movies ,key=lambda m:int(m.get("runtime")))

# print(movieduration)

# print all generes

# moviegenres={ g for m in movies for g in m.get("genres")}
# print(moviegenres)

# comedy movies released in 2015

# comedymovies=[m.get("title")for m in movies if "Comedy" in m.get ("genres") if m.get ("year")=="2015"]
# print(comedymovies)

# highest movie relesed year

wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
print(max(wc,key=lambda k:wc.get(k)))


