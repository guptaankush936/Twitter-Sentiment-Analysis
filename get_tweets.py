# -*- coding: utf-8 -*-
"""
we will define a function “get_related_tweets” that will take the parameter 
text_query and return 50 tweets related to that particular\text query. 
We will use the search API to get the results from Twitter.
"""

# import required libraries
import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "lFBpbxs0ydHQguCs1xYkuiCAO"
# api secret key
api_secret_key = "1F0lDAyiqhGSwGXgtTpYKuCFP8NJ0HOvNT0QTzWEvLLZ7Kb2Sv"
# access token
access_token = "972928033299472384-1vnIPGs7FYvAIji5TEshbAqWN20ny2r"
# access token secret
access_token_secret = "Wb0sOPe8pIIKTxPNtBQFBa76ieCS7OnzrTSKWeWEfrcOK"

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 60
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)