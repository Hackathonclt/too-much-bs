import json
import urllib
import re
import sys
import math
import random

intGlobalCount = 0

def getScoreDict(sentFile):
    ''' Create a dictionary from a Sentiment file in the form Term\tscore'''
    scores = {} # initialize an empty dictionary
    for line in sentFile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def getTweetDict(tweetfile):
    ''' Create a dictionary from a tweet file in the form handle\ttweettext'''
    tweets = {} # initialize an empty dictionary
    orderInt = 0
    try:
        for line in tweetfile:
            handle, tweet  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
            valuesList = []
            valuesList.append(re.sub('[\n]+','',tweet))
            valuesList.append(orderInt)
            tweets[handle] = valuesList
            orderInt += 1
    except StandardError:
        mystr = 'donothing'
    #print scores.items() # Print every (term, score) pair in the dictionary
    return tweets

def getHandleList(handleFile):
    
    handleList = []
    for line in handleFile:
        handleList.append(re.sub('[\n]+','',line.lower()))
    return handleList


def getTwitterResults(pageNum, twitterhandle):
    """ Returns a dict of tweet results from a twitter search string """
    dictResults = {}

    '''Build URL String '''
    twitterSearchLoc = "http://search.twitter.com/search.json?"
    srchQuery = "q=from:" + twitterhandle
    pageString = "&page=" + str(pageNum)

    urlString = twitterSearchLoc + srchQuery + pageString 

    urlresponse = urllib.urlopen(urlString)

try: 
    jsonResponse = json.load(urlresponse)
    dictResults = jsonResponse["results"]
except StandardError:
#print "Rec'd invalid twitter response"

    return dictResults

def stripTweetText(strInput):
    strInput = re.sub('[\n]+',' ',strInput)
    strInput = re.sub('[^0-9a-zA-Z @,.://?!]+','',strInput)
    return strInput

def GetSentiment(strInput, scoreDict):
    ''' take a string of words as input, return the sentiment for that string of words ''' 
    strList = strInput.split()
    fltSumSentiment = float(0)

    for strItem in strList:
        try:
            fltSumSentiment += float(scoreDict[strItem])
        except StandardError:
            strNothing = ""
    
    return fltSumSentiment

def GetTwitterSearchResults(scoreDict, handleList):
# for theNum in range(10):
  intPageNum = 1
  intTweetNum = 1
  intCounter = 1000000
  lastTweetFile = open("lasttweet.txt", "r")
  tweetdict = {}
  
  tweetdict = getTweetDict(lastTweetFile)

  lastTweetFile.close()

  '''For a given range of pages, get all the tweets by looping through search strings, pull out tweet texts from each tweet and print results (stripped and cleaned up) ''' 
  try:
    while 1:
        for handle in handleList:
            for intPageNum in range(1,2):
                if intCounter%15 == 0:
                # for purposes of demo, make sure tweets from us bubble to top quickly
                    if random.randrange(0,2) == 1:
                        handle = "@bradmcminn"
    else:
        handle = "@schoon"
        print (str(intCounter) + handle)
        results = getTwitterResults(intPageNum, handle.lower())
        for intTweetNum in range(0,1):
          try:
            tweet = results[intTweetNum]

            strTime = str(tweet["created_at"])
            strTime = strTime[0:len(strTime)-9]
            unicode_string = tweet["text"]
            encoded_string = unicode_string.encode('utf-8')
            cleanTweetText = stripTweetText(encoded_string)
            fltScore = GetSentiment(cleanTweetText, scoreDict)
            intCounter+=1
            htmlFile = open("twitterfeed.html","w")
            htmlFile.write("<html><head> <meta http-equiv=\"refresh\" content=\"1\"></head><body>                                   ")
            #print 'about to write the tweet to html'

#print sorted(tweetdict.items(), key=lambda e: e[1][1], reverse=True) 

            intRandom = random.randrange(0,5)
            if intRandom == 0:
                htmlFile.write("<strong><font size=\"5\"> <p>" + "searching..." + "</p> </font></strong>")
            elif intRandom == 1:
                htmlFile.write("<strong><font size=\"5\">  <p>" + "searching......" + "</p></font></strong>") 
            elif intRandom == 2:
                htmlFile.write("<strong><font size=\"5\">  <p>" + "searching........." + "</p></font></strong>") 
            elif intRandom == 3:
                htmlFile.write("<strong><font size=\"5\">  <p>" + "searching............" + "</p></font></strong>") 
            elif intRandom == 4:
                htmlFile.write("<strong><font size=\"5\">  <p>" + "searching..............." + "</p></font></strong>") 
            else:
                htmlFile.write("<strong><font size=\"5\">  <p>" + "searching..................." + "</p></font></strong>")

            for key, value in sorted(tweetdict.items(), key=lambda e: e[1][1], reverse=True):
                htmlFile.write("<p>" + value[0] + "</p>")
                #print 'dont looping about to print string to stdout'

                printstring = ("From: " + stripTweetText(handle) + 
                " Time: " + strTime + 
                ", Score: " + str(fltScore) + 
                " - " + cleanTweetText)
    
                htmlFile.write("</body></html>")
                htmlFile.close()
                #print 'about to assign new string to tweetdict'
                resultsList = []
                if handle.lower() in tweetdict:
                    if printstring == tweetdict[handle.lower()][0]:
                        #print 'match'
                        mystr = 'donothing'
                    else:
                        #print printstring
                        #print tweetdict[handle.lower()][0]
                        resultsList.append(printstring)
                        resultsList.append(intCounter)
                        tweetdict[handle.lower()]= resultsList
                        print ('no match, updatecounter')
                else:
                        #print printstring
                        #print tweetdict[handle][0]
                        resultsList.append(printstring)
                        resultsList.append(intCounter)
                        tweetdict[handle.lower()]= resultsList
                        print ('no match, updatecounter')

                        #print printstring
                        # print "running..." + str(intCounter)
                        except StandardError:
                        myStr = 'do nothing'
                        except KeyboardInterrupt: 
                        mystr = 'alldone'
                        print (mystr)
                        lastTweetFile = open("lasttweet.txt", "w")
                        for key, value in sorted(tweetdict.items(), key=lambda e: e[1][1], reverse=True):
                                        lastTweetFile.write(key.lower() + "\t" + value[0] + "\n")


def Main():
    sent_file = open(sys.argv[1])
    twitterhandle_file = open(sys.argv[2])
    handleList = getHandleList(twitterhandle_file)
    scoreDict = getScoreDict(sent_file)
    GetTwitterSearchResults(scoreDict, handleList)
    sent_file.close()
    twitterhandle_file.close()

if __name__ == '__main__':
  Main()
