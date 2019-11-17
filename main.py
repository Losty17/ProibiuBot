# -*- coding: utf-8 -*-
from random import randint
import tweepy
from time import sleep

####palavras
file = open("words.txt", "r")
words = file.readlines()

####login do bot
consumer_key = 'iC8KiB6mzDgL9xhCp5IF45wDV'
consumer_secret = 'NmsinPXvIX4DA9dKR4Mtdg4Pr5KN3UaRlA9v4ZLLdcfYSOsRTx'
access_token = '1194773307234639873-lUH5j86nltPvxUKH6smRhKsO0IOS58'
access_token_secret = 'wo5TTgfusLwS3M7Ck00B7Paotju88PSR4ghUuXHxHmsb3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####variaveis
user = api.get_user('ProibiuBOT')
contador = user.statuses_count
TOTAL = 28627

####main loop
while True:
    update = "Hoje o governo mandou proibir " + words[randint(1,TOTAL)].lower()
    api.update_status(status=update)
    contador += 1
    if contador % 100 == 0:
        porcentagem = str(round(contador / TOTAL * 100, 2))
        update='O governo ja proibiu ' + porcentagem + '% do dicionario'
        api.update_status(status=update)
    sleep(3600)