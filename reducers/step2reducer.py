#!/usr/bin/env python3

import sys

def calc_popularity_and_print(page, date_arr, views_arr):
    assert len(date_arr) == len(views_arr)

    date_arr = [int(date) for date in date_arr]
    views_arr = [int(views) for views in views_arr]

    # sort date indices
    date_views_sorted = sorted(zip(date_arr, views_arr), key = lambda x: x[0])
    date_arr = [date_views[0] for date_views in date_views_sorted]
    views_arr = [date_views[1] for date_views in date_views_sorted]

    total_views_str = str(sum(views_arr))

    views_day_3_5 = 0
    views_day_1_2 = 0
    for date, views in zip(date_arr, views_arr):
        if date % 10 <= 2:
            views_day_1_2 += views
        else:
            views_day_3_5 += views
    popularity_str = str(views_day_3_5 - views_day_1_2)

    date_str = str(date_arr).replace(' ', '')
    views_str = str(views_arr).replace(' ', '')

    print(page + '\t' + date_str + '\t' + views_str + '\t' 
                + total_views_str + '\t' + popularity_str)


# Initialize with information from the first line
firstline = sys.stdin.readline()
while len(firstline.strip().rsplit("\t", 2)) != 3:
    firstline = sys.stdin.readline()
pagename, date, pageviews = firstline.strip().rsplit('\t', 2)

prev_page = pagename
prev_date = [date]
prev_views = [pageviews]

# Loop for subsequent lines
for line in sys.stdin:
    # use rsplit in case there are spaces in the article title
    split_line = line.strip().rsplit("\t", 2)
    if len(split_line) != 3:
        continue
    curr_page, curr_date, curr_views = split_line

    if curr_page == prev_page:
        # If the current page and date are the same as previous entry,
        # accumulate the page views
        prev_date.append(curr_date)
        prev_views.append(curr_views)
    else:
        # If we encounter something new, then we need to print the (finished)
        # previous entry 
        calc_popularity_and_print(prev_page, prev_date, prev_views)
        # Then we need to set all prev to curr
        prev_page = curr_page
        prev_date = [curr_date]
        prev_views = [curr_views]

calc_popularity_and_print(prev_page, prev_date, prev_views)


    