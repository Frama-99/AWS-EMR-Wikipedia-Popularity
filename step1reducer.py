#!/usr/bin/env python3

import os
import sys

# Initialize with information from the first line
firstline = sys.stdin.readline()
while len(firstline.strip().rsplit("\t", 1)) != 2: # get rid of empty lines at the start
    firstline = sys.stdin.readline()
pagename_date, pageviews = firstline.strip().rsplit("\t", 1)

prev_page_date = pagename_date
prev_views = int(pageviews)

# Loop for subsequent lines
for line in sys.stdin:
    # use rsplit in case there are spaces in the article title
    split_line = line.strip().rsplit("\t", 1)
    if len(split_line) != 2:
        continue
    curr_page_date, curr_views = split_line
    curr_views = int(curr_views)

    if curr_page_date == prev_page_date:
        # If the current page and date are the same as previous entry,
        # accumulate the page views
        prev_views += curr_views
    else:
        # If we encounter something new, then we need to print the (finished)
        # previous entry 
        print(prev_page_date + ' ' + str(prev_views))
        # Then we need to set all prev to curr
        prev_page_date = curr_page_date
        prev_views = curr_views

print(prev_page_date + ' ' + str(prev_views))

# TODO: somehow even though keys are sorted locally (and we have one single
# key that contains both the page and teh date), they're not
# sorted in the cloud, leading to multiple entries with the same name and
# date. (See also piazza @420)

    