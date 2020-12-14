#!/usr/bin/env python3

import os
import sys

# Initialize with information from the first line
firstline = sys.stdin.readline()
while len(firstline.strip().split()) != 3: # get rid of empty lines at the start
    firstline = sys.stdin.readline()
pagename, date, pageviews = firstline.strip().split()

prev_page = pagename
prev_date = date
prev_views = int(pageviews)

# Loop for subsequent lines
for line in sys.stdin:
    # use rsplit in case there are spaces in the article title
    split_line = line.strip().rsplit(" ", 2)
    if len(split_line) != 3:
        continue
    curr_page, curr_date, curr_views = split_line
    curr_views = int(curr_views)

    if curr_page == prev_page and curr_date == prev_date:
        # If the current page and date are the same as previous entry,
        # accumulate the page views
        prev_views += curr_views
    else:
        # If we encounter something new, then we need to print the (finished)
        # previous entry 
        print(prev_page + '}' + prev_date + ' ' + str(prev_views))
        # Then we need to set all prev to curr
        prev_page = curr_page
        prev_date = curr_date
        prev_views = curr_views

print(prev_page + '}' + prev_date + ' ' + str(prev_views))

# TODO: somehow even though keys are sorted locally, they're not
# sorted in the cloud, leading to multiple entries with the same name and
# date. 

    