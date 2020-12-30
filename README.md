# Wikipedia Popularity Analysis Using AWS EMR

Tufts COMP 118 (Cloud Computing) project that leverages AWS EMR to create a
MapReduce application that analyzes the popularity of Wikipedia articles
between June 1-5, 2016. 

The raw data can be found
[here](http://dumps.wikimedia.org/other/pagecounts-raw/).

Results can be found in the `results/` folder. 
- `top_100_pageviews.txt` contains the top 100 most viewed articles during
  the time period.
- `top_100_trending.txt` contains the top 100 most trending articles during
  the time period, where a page's "trendiness" is defined by the views in
  the last three days minus the views in the first two days.
- `x_pageviews.txt` contains a ranked list of article names that contain
  the word `x`. 