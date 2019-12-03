# -*- coding: utf-8 -*-
"""
Created on Tue Dec 3 11:06:08 2019

@author: bejoyalduse
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import io
import sys

# Refer twitter for api
# https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens


api_key = "**************"
api_secret = "**************"
access_token_key = "**************"
access_token_secret = "**************"

data1={}
tweets = {}
index = 0
class listener(StreamListener):
    index +=1
    if index == 20:
        sys.exit()  
   
    def on_data(self, data):
        try:
            #index+=1
            print data
            tweet = data.split(',"text":"')[1].split(',"source":"')[0]
            #print tweet
            saveThis = tweet
            
            saveFile = open('twitDB00.csv', 'a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
                        
            #t1 = json.load(data)
            tweets= data
            saveFiletext1 = open("twitDB01.txt","a")
            json.dump(tweets,saveFiletext1)
            saveFiletext1.close()
           
            saveFiletext = open('twitDB02.json', 'a')
            saveFiletext.write(data)
            #saveFiletext.write('\n')
            saveFiletext.close()
            #data1.append(data)

            
            
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            #time.sleep(5)
        
    def on_error(self, status):
        print status
        
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["NFL"])


