
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
    account = 'TWILIO_ACCOUNT_SID'
    token = 'TWILIO_AUTH_TOKEN'
    client = Client(account.token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to='+13366025704',
                           from_='+17273085703',
                           body=quote
                           )


schedule.every().day.at("11:22").do(send_message, in_the_bag_quotes)


while True:
    schedule.run_pending()
    time.sleep(1)