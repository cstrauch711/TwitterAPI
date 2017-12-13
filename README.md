# TwitterAPI
TwitterAPI accesses the twitter API and uses it to access number of retweets and favorites from tweets within the last month to use later on. The file uses the Twitter module to pull information from Twitter.'/n'
The consumer_key, consumer_secret, access_token_key, and access_token_secret must be added in lines 6-9 for the program to function.
A User_ID of the account wanting to be analyzed must be added in line 13 for the program to work correctly. I used http://gettwitterid.com/ to gain the Account's ID number.
The code contains a variety of methods for accessing information from Twitter using a Twitter account ID number in the past month. The different functions available are:
1. topFAndRT()  This function pulls and prints the top retweeted tweet and most favorited tweet of the account in the last month.
2. topRT()  This function pulls and prints the top retweeted tweet of the account in the last month.
3. topF()   This function pulls and prints the most favorited tweet of the account in the last month.
4. topKRT() This function pulls and prints the top 'k' number of most retweeted tweets in the last month from the specified account.
5. topKF()  This funciton pulls and prints the top 'k' number of most favorited tweets in the last month from the specified account.
6. topScore()  This funciton pulls and prints the tweet in the last month from the specified user with the highest 'score'. 'score' is a number calculated by adding an integer multiplied by a tweet's number of retweets and an integer multiplied by a tweet's number of favorites. The integer is currently set at 1 for favorites and 2 for retweets, but it can be changed in line 178.
7. topKScore()  This function is similar to topScore(), but it pulls and prints a 'k' number of top scored tweets from the specified user within the last month.
