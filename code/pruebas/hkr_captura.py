import imgkit
import tweepy
from twittercredentials import TwitterCredentials as tw


# personal details
twi = tw()
consumer_key=twi.consumer_key
consumer_secret=twi.consumer_secret
access_token=twi.access_token
access_token_secret=twi.access_token_secret

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

imgkit.from_url('http://www.hkr.es/', 'hkr.jpg')

api.update_with_media('hkr.jpg', status="Hello World !")
