import tweepy
import urllib.request

CONSUMER_KEY = "******************"
CONSUMER_SECRET = "*****************"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = "*****************"
ACCESS_SECRET = "******************"
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

if __name__ == '__main__':
    for status in api.home_timeline(count=200)[::-1]:
        if status.favorited == True:
            try:
                j = 0
                for i in status.extended_entities['media']:
                    print (i['media_url'])
                    j = j + 1
            except:
                print ("No pictures")
