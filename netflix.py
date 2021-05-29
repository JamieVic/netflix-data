#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("c:/Users/TechFast Australia/Dropbox/Programming/Python/Netflix/netflix.csv", index_col = 0)

movies = []
for lab, row in df.iterrows():
    if row['type'] == 'Movie':
        movies.append(row)
movies_df = pd.DataFrame(movies)
movie_year = np.array(movies_df.iloc[:, 6]).astype(int)
movie_duration = np.array(movies_df.iloc[:, 8]).astype(int)
sorted_duration = np.sort(movie_duration)

colours = []
for lab, row in movies_df.iterrows():
    if row['rating'] == 'G' or row['rating'] == 'TV-G':
        colours.append('green')
    elif row['rating'] == 'NC-17' or row['rating'] == 'TV-MA':
        colours.append('red')
    elif row['rating'] == 'NR' or row['rating'] == 'UR':
        colours.append('purple')
    elif row['rating'] == 'TV-14':
        colours.append('blue')
    elif row['rating'] == 'PG' or row['rating'] == 'PG-13' or row['rating'] == 'TV-PG':
        colours.append('yellow')
    elif row['rating'] == 'R':
        colours.append('black')
    elif row['rating'] == 'TV-Y' or row['rating'] == 'TV-Y7' or row['rating'] == 'TV-Y7-FV':
        colours.append('pink')
    else:
        colours.append('grey')

plt.subplot(2, 1, 1)
plt.hist(sorted_duration)
plt.title('Distribution of Netflix Movies Duration')
plt.xlabel('Minutes')
plt.ylabel('Number of Movies')
plt.subplot(2, 1, 2)
plt.scatter(movie_year, movie_duration, c = colours)
plt.title('Distribution of Netflix Movies Duration and Years')
plt.xlabel('Years')
plt.ylabel('Minutes')
plt.show()