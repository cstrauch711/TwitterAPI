import twitter
from twitter import *
import datetime

#the consumer_key, consumer_secret, access_token_key, and access_token_secret must be added here
api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='')

#User_ID is the ID number of the twitter account wanting to be analyzed
# http://gettwitterid.com/ was utilized for gaining User_ID
User_ID =
#'time' is the number of seconds between 1970 and today to later establish tweets in the past month only
time = (datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds()

#This function pulls the the most retweeted tweet and the most favorited tweet in the last month
def topFAndRT():
    most_favorites = 0
    most_rt = 0
    top_favorite ={} #initializing top_favorite and its attributes below
    top_favorite['favorite_count'] = 0
    top_favorite['date'] = ""
    top_favorite['text'] = ""
    top_rt = {} #initializing top_rt and its attributes below
    top_rt['retweet_count'] = 0
    top_rt['date'] = ""
    top_rt['text'] = ""
    timestamp = time - 1 #initializing the timestamp before tweets to a second ago
    n = 1
    while (time - timestamp) <= 2.628e6 :
        statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*n)
        for s in statuses:
            if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 :
                if s.favorite_count > most_favorites:
                    most_favorites = s.favorite_count
                    top_favorite['favorite_count'] = s.favorite_count
                    top_favorite['date'] = s.created_at
                    top_favorite['text'] = s.text
                if s.retweet_count > most_rt:
                    most_rt = s.retweet_count
                    top_rt['retweet_count'] = s.retweet_count
                    top_rt['date'] = s.created_at
                    top_rt['text'] = s.text
        timestamp = s.created_at_in_seconds
        n += 1
    print ("Most Favorites: " + str(most_favorites))
    print (top_favorite)
    print ("Most retweets: " + str(most_rt))
    print (top_rt)

#This function pulls the most retweeted tweet in the alst month.
def topRT():
    most_rt = 0
    top_rt = {} #initializing top_rt and its attributes below
    top_rt['retweet_count'] = 0
    top_rt['date'] = ""
    top_rt['text'] = ""
    timestamp = time - 1 #initializing the timestamp before tweets to a second ago
    n = 1
    while (time - timestamp) <= 2.628e6 :
        statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*n)
        for s in statuses:
            if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 :
                if s.retweet_count > most_rt:
                    most_rt = s.retweet_count
                    top_rt['retweet_count'] = s.retweet_count
                    top_rt['date'] = s.created_at
                    top_rt['text'] = s.text
        timestamp = s.created_at_in_seconds
        n += 1
    print("Most Retweets: " + str(most_rt))
    print(top_rt)

#This function pulls the most favorited tweet in the last month.
def topF():
    most_favorites = 0
    top_favorite ={} #initializing top_favorite and its attributes below
    top_favorite['favorite_count'] = 0
    top_favorite['date'] = ""
    top_favorite['text'] = ""
    timestamp = time - 1 #initializing the timestamp before tweets to a second ago
    n = 1
    while (time - timestamp) <= 2.628e6 :
        statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*n)
        for s in statuses:
            if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 :
                if s.favorite_count > most_favorites:
                    most_favorites = s.favorite_count
                    top_favorite['favorite_count'] = s.favorite_count
                    top_favorite['date'] = s.created_at
                    top_favorite['text'] = s.text
        timestamp = s.created_at_in_seconds
        n += 1
    print("Most Favorites: " + str(most_favorites))
    print(top_favorite)

#This function pulls the 'k' most retweeted tweets in the last month.
def topKRT():
    top_tweets = []
    seconds = [] #The seconds list is used to ensure that previous tweets are not included in the top_tweets list
    k = 5
    for i in range(k):
        top_tweet = {} #initializing top_tweet and its attributes below
        top_tweet['retweets'] = 0
        top_tweet['date'] = ""
        top_tweet['seconds'] = 0
        top_tweet['text'] = ""
        most_rt = 0
        timestamp = time - 1 #initializing the timestamp before tweets to a second ago
        n = 1
        while (time - timestamp) <= 2.628e6 :
            statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*(n))
            for s in statuses:
                if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 and not(s.created_at_in_seconds in seconds):
                    if s.retweet_count > most_rt:
                        most_rt = s.retweet_count
                        top_tweet['retweets'] = s.retweet_count
                        top_tweet['date'] = s.created_at
                        top_tweet['seconds'] = s.created_at_in_seconds
                        top_tweet['text'] = s.text
            timestamp = s.created_at_in_seconds
            n += 1
        top_tweets.append(top_tweet)
        seconds.append(top_tweet['seconds'])
    print( "Top " + str(k) + " Retweeted tweets: ")
    for top_tweet in top_tweets:
        print (top_tweet)

#This function pulls the 'k' most favorited tweets in the last month.
def topKF():
    top_tweets = []
    seconds = [] #The seconds list is used to ensure that previous tweets are not included in the top_tweets list
    k = 5
    for i in range(k):
        top_tweet = {} #initializing top_tweet and its attributes below
        top_tweet['favorites'] = 0
        top_tweet['date'] = ""
        top_tweet['seconds'] = 0
        top_tweet['text'] = ""
        most_f = 0
        timestamp = time - 1 #initializing the timestamp before tweets to a second ago
        n = 1
        while (time - timestamp) <= 2.628e6 :
            statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*(n))
            for s in statuses:
                if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 and not(s.created_at_in_seconds in seconds):
                    if s.favorite_count > most_f:
                        most_f = s.favorite_count
                        top_tweet['favorites'] = s.favorite_count
                        top_tweet['date'] = s.created_at
                        top_tweet['seconds'] = s.created_at_in_seconds
                        top_tweet['text'] = s.text
            timestamp = s.created_at_in_seconds
            n += 1
        top_tweets.append(top_tweet)
        seconds.append(top_tweet['seconds'])
    print ("Top " + str(k) + " Favorited tweets: ")
    for top_tweet in top_tweets:
        print (top_tweet)

#This function pulls the tweet with the highest 'score' in the last month.
#The 'score' is calculated by each retweet being worth a set number of points
#and each favorite being worth a certain number of points. The points are then
#added together into a 'score'. The values for retweets and favorites can be changed in line 178
def topScore():
    #Favorites are worth 1 point and retweets are worth 2 points (flexible)
    top_score = 0
    top_tweet = {}#initializing top_tweet and its attributes below
    top_tweet['score'] = 0
    top_tweet['date'] = ""
    top_tweet['text'] = ""
    timestamp = time - 1 #initializing the timestamp before tweets to a second ago
    n = 1
    while (time - timestamp) <= 2.628e6 :
        statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*(n))
        for s in statuses:
            temp_score = 1 * s.favorite_count + 2 * s.retweet_count
            if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 :
                if temp_score > top_score:
                    top_score = temp_score
                    top_tweet['score'] = temp_score
                    top_tweet['date'] = s.created_at
                    top_tweet['text'] = s.text
        timestamp = s.created_at_in_seconds
        n += 1
    print ("Top Score: " + str(top_score))
    print (top_tweet)

#This function performs the same function as the function score(), but it pulls a
#'k' number of highest scored tweets in the last month
def topKScore():
    #Favorites are worth 1 point and retweets are worth 2 points (flexible)
    top_tweets = []
    seconds = [] #The seconds list is used to ensure that previous tweets are not included in the top_tweets list
    k = 5
    for i in range(k):
        top_tweet = {} #initializing top_tweet and its attributes below
        top_tweet['score'] = 0
        top_tweet['date'] = ""
        top_tweet['seconds'] = 0
        top_tweet['text'] = ""
        top_score = 0
        timestamp = time - 1 #initializing the timestamp before tweets to a second ago
        n = 1
        while (time - timestamp) <= 2.628e6 :
            statuses = api.GetUserTimeline(User_ID,exclude_replies=True, count=100*n)
            for s in statuses:
                temp_score = 1 * s.favorite_count + 2 * s.retweet_count
                if getattr(s, 'retweeted_status') is None and (time - s.created_at_in_seconds) <= 2.628e6 and not(s.created_at_in_seconds in seconds) :
                    if temp_score > top_score:
                        top_score = temp_score
                        top_tweet['score'] = temp_score
                        top_tweet['date'] = s.created_at
                        top_tweet['seconds'] = s.created_at_in_seconds
                        top_tweet['text'] = s.text
            timestamp = s.created_at_in_seconds
            n += 1
        top_tweets.append(top_tweet)
        seconds.append(top_tweet['seconds'])
    print ("Top " + str(k) + " Scores: ")
    for top_tweet in top_tweets:
        print (top_tweet)

topFAndRT()
topRT()
topF()
topKRT()
topKF()
topScore()
topKScore()
