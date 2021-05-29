# Netflix Data
## About this Project
This project contains observations on Netflix data where distribution of movie duration in years and rating have been determined.
## The Data
![data plots](https://i.imgur.com/Z4FxfmH.png)

The histogram shows a simple distribution of Netflix movies duration in minutes. It shows that the typical movie on Netflix is between 75 - 125 minutes long. No surprise there, many movies tend to be that long anyways.

The scatter plot below goes more in depth on the observed data, this time categorising it with release years and movie rating. The table below details each colours' representation in the scatter plot:

| Colour | Rating |
| --- | --- |
| Green | G/TV-G |
| Red | NC-17/TV-MA |
| Purple | NR/UR |
| Blue | TV-14 |
| Yellow | PG/PG-13/TV-PG |
| Black | R |
| Pink | TV-Y/TV-Y7/TV-Y7-FV |
| Grey | Other |

We can see that between 1940 and 1950, movies were generally less than 100 minutes. After that decade, we see the huge trend of movies being within that 75 - 125 minute duration that was previously mentioned in the histogram. With the addition of ratings, it makes the scatter plot more interesting. From observation, TV-14 movies are the longest, followed by the PG category and then NC-17. It's also worth noting the increased frequency of the NC-17 rating in the 2010s. We can also see that children's movies (TV-Y) are much shorter than the rest.

## How it Works
Numpy, Pandas and Matplotlib are imported to access and visualise the data. A for loop runs through the datafram and appends the movies into a list. The list is then converted to a dataframe and two variables are created to store the values of columns 6 and 8 (release_year and duration). The duration column is sorted so that the data appears correctly in the histogram. Another for loop is created to loop through each movie's rating and appends a colour accordingly for the scatter plot.

To visualise the histogram and scatter plot, a subplot is created to host both diagrams. Titles and labels are created for each diagram to make them readable.
