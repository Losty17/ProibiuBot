# -*- coding: utf-8 -*-
from random import randint
from time import sleep
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

while True:
    update = "Hoje o governo mandou proibir " + words[random.randint(1,28627)].lower()
    api.update_status(status=update)
    sleep(1800)
