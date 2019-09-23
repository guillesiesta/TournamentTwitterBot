from yattag import Doc
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

f = open("tests/web.html", "w")

doc, tag, text, line = Doc(
    defaults = {'ingredient': ['chocolate', 'coffee']}
).ttl()

with tag('h1'):
    text('Hello world!')
    text('Hello world! caca y pedo')

with tag('h2'):
    text('Caca pedo y culo')


with tag('form', action = ""):
    line('label', 'Select one or more ingredients')
    with doc.select(name = 'ingredient', multiple = "multiple"):
        for value, description in (
            ("chocolate", "Dark Chocolate"),
            ("almonds", "Roasted almonds"),
            ("honey", "Acacia honey"),
            ("coffee", "Ethiopian coffee")
        ):
            with doc.option(value = value):
                text(description)
    doc.stag('input', type = "submit", value = "Validate")

f.write(doc.getvalue())

f.close()

imgkit.from_file('tests/web.html','tests/out.jpg')

# update the status
#api.update_status(status ="Hello Everyone !")

api.update_with_media('tests/out.jpg', status="Hello World !")
