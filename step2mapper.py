#!/usr/bin/env python3

import sys

for line in sys.stdin:
    pagename_date, pageviews = line.strip().rsplit(" ", 1)
    pagename, date = pagename_date.strip().rsplit("}", 1)

    print(pagename + '\t' + date + '\t' + pageviews)