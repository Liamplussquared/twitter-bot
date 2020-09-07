import sys
import tweepy
import time
import json
import threading

from haiku import Haiku
sys.path.append('../')
from data.secrets import consumer_key, consumer_secret, access_token, access_token_secret


class App:
	def __init__(self):
		# Authenticate to Twitter
		self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(access_token, access_token_secret)

		# Create API object
		self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
		self.haiku = Haiku()

	def listen_mentions(self):
		""" This method assigns a thread to listen for incoming mentions """
		listener_thread = threading.Thread(target=self.get_mentions())
		listener_thread.start()

	def get_mentions(self):
		""" This method sits and waits for any new mentions and replies with a haiku """
		while(True):
			# retrieve recently replied to tweet ids
			with open('../data/recent_mentions.json', 'r') as r:
				recently_replied_to_mentions = json.load(r)["ids"]

			# reply to any tweets not already replied to 
			for tweet in tweepy.Cursor(self.api.mentions_timeline).items():
				if tweet.id not in recently_replied_to_mentions:
					self.reply_to_tweet(tweet.text.lower(), tweet.id)
					recently_replied_to_mentions.append(tweet.id)

			recently_replied_to_mentions.sort()

			# keep removing tweets from stored list until only 20 contained
			while len(recently_replied_to_mentions) > 20:
				recently_replied_to_mentions.pop()

			# update stored list
			with open('../data/recent_mentions.json', 'w') as outfile:
				to_store = {"ids":recently_replied_to_mentions}
				json.dump(to_store, outfile)

			# sleep for 20 seconds
			time.sleep(20)

	def reply_to_tweet(self, message, id):
		""" 
		This method replies to a tweet, reply varies 
		depending on what keywords are found in the message.
		"""
		reply_text = ""
		message = message.replace("@im_a_haiku_bot", "")

		print(message)

		if "what is a haiku" in message:
			reply_text = "A haiku is a short poem containing three phrases following a 5,7,5 syllable pattern."
		elif "haiku" in message:
			reply_text = self.get_haiku()
		else:
			reply_text = "Hello :)"
			
		self.api.update_status(
			status = reply_text,
			in_reply_to_status_id=id
		)

	def get_haiku(self):
		""" This method retrieves a haiku from haiku.py and tweets it. """
		poem = self.haiku.generate_haiku()
		return poem
		
	def post_haiku_status(self, poem):
		""" This method retrieves haiku from get_haiku and tweets it """
		self.api.update_status(status=poem)


def main():
	app = App()
	app.listen_mentions()


if __name__ == '__main__':
	main()

