import tweepy
import configparser
import pandas as pd
api_key = 'ietuiQAMZ5E0hUvGnJ2txlzuj'
api_key_secret = 'z09Oif7SCYcFSUvPrxtUQclHlNbZMPvw8pnccb9qLyaxcrApf5'
access_token = '1571506386051399680-EI2R3E8G3DVHWkBbmhPMyjg4qtLrYK'
access_token_secret = '2axVtmZuwpO1sKxNmOd2JLKrYAM6oi6p60OFnSdM8HZsd'
# read configs


# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
#user = 'veritasium'
#limit=300
# search tweets
date_since = '2020-03-01'
date_until = '2020-06-01'
keywords = 'Vaccination'
limit=1000
#tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)
tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended',start_time=date_since,end_time=date_until).items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'created_at','Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.created_at,tweet.full_text ])

df = pd.DataFrame(data, columns=columns)

print(df)