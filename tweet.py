import tweepy
import pprint
import random
import crawl
import time

pp = pprint.PrettyPrinter(indent=4)

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

mentions_id_cache = set()
replies = set()

db = crawl.FlyCircuitDB()

TWITTER_MAX_LENGTH = 140

fields = ['Name', 'Author', 'Gender/Age', 'Putative birth time', 'Soma Coordinate', 'Driver', 'Lineage', 'Putative neurotransmitter', 'Stock']

def tweetNeuron(neuron, mention):
    tag = '@' + mention.user.screen_name + '\n'
    fieldTexts = ['\n' + field + ': ' + neuron[field] for field in fields]
    i = 0
    tweet = tag
    while i < len(fieldTexts):
        fieldText = fieldTexts[i]
        if len(tweet) + len(fieldText) < TWITTER_MAX_LENGTH:
            tweet += fieldText
            i += 1
        else:
            api.update_status(tweet, mention.id)
            tweet = tag
    api.update_status(tweet, mention.id)

def reply():
    mentions = api.mentions_timeline() # type: tweepy.models.ResultSet
    for mention in mentions: # type: tweepy.models.Status
        # check if already replied to
        if mention.id in mentions_id_cache:
            break
        mentions_id_cache.add(mention.id)

        #pp.pprint(mention.__dict__)

        text = mention.text # type: str
        # strip text of @<user>s
        text = ' '.join(word for word in text.split(' ') if word[0] != '@')

        try:
            tweetNeuron(parse(text), mention)
        except ValueError as e: # type: ValueError
            api.update_status('@' + mention.user.screen_name + ' ' + str(e) + str(random.random()))
        except tweepy.error.TweepError as e:
            print(str(e))
            pass



def parse(text):
    neuron = 'Cha-F-800070'
    #text = neuron
    try:
        print 'neuron: ' + text
        return db.parse_neuron(text)
    except ValueError as e:
        raise ValueError('Please tweet us the name of a fruit fly neuron')
    pp.pprint(ret)

if __name__ == '__main__':
    while True:
        reply()
        time.sleep(30)
