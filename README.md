# Twitter Haiku Bot

This bot was created using the Python `tweepy` package. The bot is capable of replying to mentions, and has specific behaviours based on what keywords are contained in the mention. The bot creates three different types of haikus, two of which are formatted after famous haikus and another I formatted myself.

A list of recent mentions is maintained in `recent_mentions.json` to ensure that the bot only replies to a mention once. A maximum of 20 recent mentions is maintained. 

The `data.json` file contains a json object of words that are used by the haiku generator. 

`haiku.py` manages the creation of haikus and is called by `app.py`. `app.py` is the actual bot code, and must be run for the bot to work.  


## Steps to run the bot

1. Apply for a Twitter developer account and enter credentials into `secrets.py`.
2. Ensure that all depenencies are installed (check `requirements.txt`)
3. From command line, `cd` in the `bot` directory and execute `python app.py`.
4. Once the program is running, any mentions made to the bot account (while the bot is logged in) will be replied to!