#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from config import *

if __name__ == "__main__":
   
    # Set this first variable to False, or nothing will be deleted
    test_mode = True
    verbosenot = True
    verboseyes = True
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)    
    
    timeline = tweepy.Cursor(api.user_timeline).items()
        
    n = 0
    for tweet in timeline:
        n += 1
        if n > n_keep:
            if verboseyes:
                print "Will delete tweet %d (%s): %s" % (tweet.id, 
                                                         tweet.created_at, 
                                                         tweet.text.encode('utf-8'))
            if not test_mode:
                api.destroy_status(tweet.id)
        elif verbosenot:
            print "Will NOT delete tweet %d (%s): %s" % (tweet.id, 
                                                         tweet.created_at, 
                                                         tweet.text.encode('utf-8'))
