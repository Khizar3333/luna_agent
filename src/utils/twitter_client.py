import os
import tweepy

from config import bearer_token, api_key, api_secret, access_token, access_token_secret

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)