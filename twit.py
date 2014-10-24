import tweepy
import json
import time
#create a twitter app to get these. https://dev.twitter.com
consumer_key='' 
consumer_secret=''
access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        tweet_id = decoded['id']
        api.create_favorite(tweet_id)
        print "Favorited a new tweet!"
        time.sleep(65)
        return True

    def on_error(self, status):
        if(status == 420):
        	print "Twitter is limiting this account."
    	else:
    		print "Error Status "+ str(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Favoriting new tweets from Houston, TX."

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(locations=[-95.788087,29.523624,-95.014496,30.110732])
    #http://boundingbox.klokantech.com/ -- select 'CSV' from the dropdown. WORKS LIKE A CHARM!!!! TOOK ME FOREVER TO FIND THAT SOB.
