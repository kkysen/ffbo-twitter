import tweepy

CONSUMER_KEY = 'P9npViwfoDDj8NY0rJNDX5xYD'
CONSUMER_SECRET = 'KyBbmRI1uAyQZgOVDTznd138xkDXO8dspWhkpTsmDlZRivMaba'
ACCESS_KEY = '840999689294106624-I9F78QJOhha9qTxQglR3twqdWbt1kzj'
ACCESS_SECRET = 'oAP1LacIK5NCdTfKgDJdncHmNxLSE7VsZFnixi9p6REoJ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

for k in tweepy.API.__dict__:
    print k