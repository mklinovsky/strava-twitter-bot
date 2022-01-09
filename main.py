import tweepy
import strava
import store

twitter_settings = store.get_twitter_settings()

client = tweepy.Client(
    consumer_key=twitter_settings['api_key'], 
    consumer_secret=twitter_settings['api_secret'], 
    access_token=twitter_settings['access_token'], 
    access_token_secret=twitter_settings['access_token_secret'])

def tweet(event, context):
    try:
        message = strava.get_stats_message()
        print(message)
        client.create_tweet(text=message)
    except tweepy.HTTPException as e:
        print(e.response.json())
