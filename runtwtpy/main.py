from datetime import date, timedelta

import numpy as np
import radar
import snscrape.modules.twitter as sntwitter
from dateutil.relativedelta import relativedelta

import pandas as pd
# import sys
# sys.path.append('/Users/kongallen/Desktop/python/func') 
# from encrypt import encrypt

start_date_list=[]
end_date_list=[]
start_everyday_list=[]

def qdate(jj, nn, rr):
    start_date = pd.to_datetime(jj)
    numbers_of_quarter = int(nn)

    for i in range(0, numbers_of_quarter*3, 3):
        x = start_date + relativedelta(months=i)
        y = start_date + relativedelta(months=i+3) - timedelta(days=1)
        start_date_list.append(x)
        end_date_list.append(y)
    # Numbers of quarter * (Numbers of random day * Numbers of tweet per day)
    # For example, 12 * (2 * 10) = 240
    nubmer_of_random_day = int(rr)
    for i in range(int(len(start_date_list))):
        for k in range(nubmer_of_random_day):
            start_everyday_list.append(radar.random_datetime(start_date_list[i].date()+timedelta(days=1), stop=end_date_list[i].date()-timedelta(days=1)))

    print('---------------------------------------------------------------------------------------------------') 
    print(f'| There are {numbers_of_quarter} quarters. For each quarter, there are {nubmer_of_random_day} random days. Total number of days = {len(start_everyday_list)} |')
    print('---------------------------------------------------------------------------------------------------') 

    for i in start_everyday_list:
        print(f'{i.year}_Q{pd.Timestamp(i).quarter}  |  start_date: {i}')
    #     print(f'{x.year}_Q{x.quarter}  |  Start:{x.date()}  |  End:{y.date()}')
    #     print('-----------------------------------------------------------') 
    # print(f'During the period between {start_date.date()} and {end_date_list[-1].date()}, there are {numbers_of_quarter} quarters in total.')
    return start_date_list, end_date_list, start_everyday_list

def tscrape(key, li):
    tweets = []
    tweets_every_crawl = []
    keyword = key
    limit = int(li)

    for i in range(len(start_everyday_list)):
        bbb = start_everyday_list[i]
        query = f'{keyword} until:{bbb} lang:en'
        print(query)

        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if len(tweets_every_crawl) == limit:
                tweets_every_crawl.clear()
                break
            else:
                tweets_every_crawl.append([tweet.date, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content, tweet.likeCount, tweet.retweetCount,  tweet.quoteCount, tweet.replyCount])
                tweets.append([tweet.date, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content, tweet.likeCount, tweet.retweetCount,  tweet.quoteCount, tweet.replyCount])
    df = pd.DataFrame(tweets, columns=['Date', 'TweetURL','User', 'Source', 'Location', 'Tweet', 'Likes_Count','Retweet_Count', 'Quote_Count', 'Reply_Count'])
    # df['encrypted'] = [encrypt(i,1) for i in df['Tweet']]
    return print(df.sample(50))



if __name__ == '__main__':
    qdate()
    tscrape()