import tweepy
import BeautifulSoup
import pprint
import random

pp = pprint.PrettyPrinter(indent=4)

a = tweepy.models.ResultSet
b = tweepy.models.Status


CONSUMER_KEY = 'P9npViwfoDDj8NY0rJNDX5xYD'
CONSUMER_SECRET = 'KyBbmRI1uAyQZgOVDTznd138xkDXO8dspWhkpTsmDlZRivMaba'
ACCESS_KEY = '840999689294106624-I9F78QJOhha9qTxQglR3twqdWbt1kzj'
ACCESS_SECRET = 'oAP1LacIK5NCdTfKgDJdncHmNxLSE7VsZFnixi9p6REoJ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

mentions_id_cache = set()
replies = set()


def reply():
    mentions = api.mentions_timeline() # type: tweepy.models.ResultSet
    for mention in mentions: # type: tweepy.models.Status
        # check if already replied to
        if mention.id in mentions_id_cache:
            break
        mentions_id_cache.add(id)

        #pp.pprint(mention.__dict__)

        text = mention.text # type: str
        # strip text of @<user>s
        text = ' '.join(word for word in text.split(' ') if word[0] != '@')

        reply = '@' + mention.user.screen_name + ' ' + parse(text)
        print reply

        try:
            api.update_status(reply, mention.id)
        except tweepy.error.TweepError:
            pass


def parse(text):
    return text + ' replied' + str(random.random())


if __name__ == '__main__':
    reply()