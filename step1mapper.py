#!/usr/bin/env python3

import os
import sys
from urllib import parse

# when testing locally, run export
# map_input_file="/mnt/c/Users/Ma990/OneDrive/Downloads/pagecounts-20160601-000000"
# in the shell 
# on EMR, the map_input_file environment variable is automatically set to
# the absolute path of the current file 
_, filename = os.path.split(os.getenv('map_input_file'))
date = filename.split('-')[1]

start_excludes = ['Media', 'Special', 'Talk', 'User', 'User_talk', 'Project',
'Project_talk', 'File','File_talk', 'MediaWiki', 'MediaWiki_talk', 'Template', 
'Template_talk', 'Help', 'Help_talk', 'Category', 'Category_talk', 'Portal', 
'Wikipedia', 'Wikipedia_talk']

end_excludes = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.ico', '.txt']

full_excludes = ['404_error', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Favicon.ico', 'Search']

char_excludes = ['%0A', '%0a', '%0D', '%0d', '%09']

class ExcludeInOutput(Exception): pass

for line in sys.stdin:
    split_line = line.strip().rsplit(" ", 3)
    if len(split_line) != 4:
        continue

    projectcode, pagename, pageviews, _ = split_line
    try:
        if projectcode != 'en':
            raise ExcludeInOutput
        for start_exclude in start_excludes:
            if pagename.startswith(start_exclude):
                raise ExcludeInOutput
        for end_exclude in end_excludes:
            if pagename.endswith(end_exclude):
                raise ExcludeInOutput
        for full_exclude in full_excludes:
            if pagename == full_exclude:
                raise ExcludeInOutput
        if pagename and pagename[0].isalpha() and pagename[0].islower():
            raise ExcludeInOutput
        # exclude new line and tab characters per @416 and @452
        for char_exclude in char_excludes:
            if char_exclude in pagename:
                raise ExcludeInOutput
        
        print(parse.unquote_plus(pagename) + '}' + date + '\t' + str(pageviews))        

    except ExcludeInOutput:
        continue