import tweepy
import pandas as pd

api_key = 'ietuiQAMZ5E0hUvGnJ2txlzuj'
api_key_secret = 'z09Oif7SCYcFSUvPrxtUQclHlNbZMPvw8pnccb9qLyaxcrApf5'
access_token = '1571506386051399680-EI2R3E8G3DVHWkBbmhPMyjg4qtLrYK'
access_token_secret = '2axVtmZuwpO1sKxNmOd2JLKrYAM6oi6p60OFnSdM8HZsd'
# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = 'joebiden'
limit=7000

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# create DataFrame
columns = ['User', 'Tweet', 'created_at']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text, tweet.created_at])

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('tweets.csv')