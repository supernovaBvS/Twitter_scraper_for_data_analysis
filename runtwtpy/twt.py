from main import qdate, tscrape

# qdate(startdate, numbers_of_quarters, numbers_of_random days)
qdate('2021-01-01', 4, 4)
# tscrape(keyword, limit tweet from each date)
tscrape('#netflix', 10)