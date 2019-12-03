# -*- coding: utf-8 -*-
"""
Created on Tue Dec 3 13:23:00 2019

@author: bejoyalduse
"""

#import json
import sys
import json


afinnfile =  open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

##########

## create tweet file ####

file2 = open(sys.argv[2], "r") #open(filename,"r")# list of tweets
tweets_input  = file2.readlines();
file2.close()

##########
  
##create two lists - one for words and other for scores
listofword = (scores.keys())
score2 = list(scores.values())

index= 0
temp = 0
tweetscore = [0]


tweets = []


###########

new_list = []
new_list_score = []
for sentence in tweets_input: # loop for al tweets
    jsonData = json.loads(sentence)
    createdAt = jsonData['created_at']
    text = jsonData['text']
    line1 = createdAt + " :: " + text
    temp = 0# score for existing words
    
    
    #print(sentence)
    line = line1.split()
    #print(line)
    index=0
    id_thistweet = []
    templast = 0
    countnew_score = []
    
    for eachword in line: # loop for each term in tweet
        onewordintweet = eachword.lower()#.strip('~!@#$%^&*()_+\/')
        #print(onewordintweet)
        index +=1
        count = -1
        m = -1
        
        for word1 in listofword: # loop for old list of words
            lower1 = word1.lower()#
#            #print(lower1)
            count = count + 1
            wordyesno = 0# 1 for word is in old list, 0 for word not in old list
            #lower = 'great'
            #print(lower)
            if lower1 == onewordintweet: # check if tweet matches words
               temp = temp + score2[count] # score for the tweet
               templast = temp;
               wordyesno = 1# 1 for yes, word is in old list
               break
        # if not available in old list add the word to new list
        # this happens outside of for loop for old list (listofword)
        
        if wordyesno == 0:# word was not found in old list
           m +=1
                #id_thistweet.append(j)
           new_list.append(onewordintweet)
           countnew_score.append(1)# id for words not in old list
               
                      
    if index == len(line): #when all words in tweet are checked
       tweetscore.append(templast) # add score of this tweet
       #index_now = 0
       for k in countnew_score: # multiply the ones array with templast
           #new_score[index_now] = k*templast
           new_list_score.append(templast) # 
#           index_now += 1
           
       
            
#del tweetscore[0]
#dict1 = {new_list[i]: new_list_score[i] for i in range(len(new_list))}
index2=0
for mm in new_list_score:                   
#    sys.stdout.write(str([new_list[mm],' ']))
#    sys.stdout.write(str(new_list_score[mm] ))
#    sys.stdout.write('\n')
    print new_list[index2],' ',new_list_score[index2]
    index2 +=1