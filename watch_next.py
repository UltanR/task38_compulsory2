import spacy
import numpy as np

nlp = spacy.load('en_core_web_md')

movies = []
movie_plots = []

f = open("movies.txt", "r")

for line in f:  # stores each title in a list, and stores just the plots in a separate list

    contents = line.replace("\n","")

    movies.append(contents[:7])

    movie_plots.append(contents[9:])

f.close()

# description of Planet Hulk movie
planet_hulk = nlp('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.''')

def watch_next(movie):  # takes description of movie as an argument

    similarities = []

    for i in movie_plots:   # calculates similarity between description given as argument and each movie in the file

        similarities.append(movie.similarity(nlp(i)))   # adds value to list
    
    index = np.argmax(similarities) # finds index of max value (most similar movie)

    print(f"The most similar movie on file is {movies[index]}") # gives recommendation
    

watch_next(planet_hulk)