-- Summary: This sample shows you how to analyze CloudFront logs stored in S3 using Hive

-- Create table using sample data in S3.  Note: you can replace this S3 path with your own.
CREATE EXTERNAL TABLE wiki_views (
    page STRING,
    dates STRING,
    views STRING,
    total_views INT,
    trend INT
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'
LOCATION '${INPUT}';


INSERT OVERWRITE DIRECTORY '${OUTPUT}' 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
SELECT page, trend FROM wiki_views ORDER BY trend DESC LIMIT 100;