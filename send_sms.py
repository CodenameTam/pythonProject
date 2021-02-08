# Download the helper library from https://www.twilio.com/docs/python/install
import random
import schedule
import time
from twilio.rest import Client

in_the_bag_quotes = [
    "Everything you want and need, you already have. Now get in the bag",
    "Just reminding you, that you are the very best. Now seize the day.",
    "God is Love, Love is God. Don't waste the day God has given you.",
    "Erase your worries; now accept only the good today.",
    "Enjoy your luxurious day. Manage your 6+ figures wisely",
    "Birds chirping, dogs barking, and being used to the finer things.",
    "Good morning, Lead with Love again today.",
    "Good morning, get everything today can give.",
    "Make a money opportunity today",
    "Good morning, only you can catch the blessings you want. Get the glove!",
    "Good morning Bestest. Continue to make a greater ROI of everything.",
    "Good morning Amazing Planner. Everything has been right on time.",
    "Good morning, get up in 10sec if you know you have 100k+!",
    "Good morning Tamara! Your Volvo needs to be cleaned again, there might be a spec on it.",
    "Your Top #10 Sticker Shop is waiting on you. Do what it takes for the bag.",
    "Good morning Frontend Developer, continue to be amazing.",
    "Good morning Amazing Mother, save for Giselle and Juel's straight A celebrations!",
    "Good morning Ms. Neutral. Get out of your Mind and get in your Bag.",
    "Good morning Family Woman, give them Love again today."
]

def send_message(quotes_list=in_the_bag_quotes):
    account_sid = 'ACe1eb7ad13f36b117c7d73153954a1f68'
    auth_token = 'cec40077b8bacf3ed75ebc2b8644c8ef'
    client = Client(account_sid, auth_token)
    quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

    client.messages.create(
                     body=quote,
                     from_='+17273085703',
                     to='+13366025704',
                    )


schedule.every().day.at("11:22").do(send_message, in_the_bag_quotes)


while True:
    schedule.run_pending()
    time.sleep(1)