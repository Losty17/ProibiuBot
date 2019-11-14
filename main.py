# -*- coding: utf-8 -*-
import random, os, sys
import tweepy

file = open("words.txt", "r")
words = file.readlines()

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

n = random.randint(1,28627)
update = "Hoje o governo proibiu " + words[n].lower()
api.update_status(status=update)
