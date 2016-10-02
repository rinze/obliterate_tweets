# -*- coding: utf-8 -*-
import tweepy
import time
import csv
from config import *

if __name__ == "__main__":

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Assume the .csv file with the archive is in the current directory.
    tweets = []
    with open("tweets.csv", "r") as tweet_file:
        tweet_data = csv.DictReader(tweet_file)
        for row in tweet_data:
            tweets.append(row['tweet_id'])
    ids = tweets[n_keep:]
    
    for tid in ids:    
        try:
            tweet = api.destroy_status(tid)
            print "[DELETED] %s (%s) %s" % (tweet.user.screen_name, 
                                            tweet.created_at, 
                                            tweet.text.encode('utf8'))
        except:
            pass
    time.sleep(1)
