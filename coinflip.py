import praw, random

# Start Vars
TRIGGERS = ['flip a coin', 'coinflip', 'flipacoin', 'heads or tails']  #What the bot will look for in comments
REPLY_TEMP = 'As you requested, I flipped a coin for you, the result was **{}** \n\n --- \n\n ^^For ^^more ^^information/to ^^complain ^^about ^^me, ^^see ^^/r/flipacoinbot'  #Reply template, with heads/tails being placed in {}
SIDES = ['Heads', 'Tails']
SUBS = 'all-askreddit-suicidewatch'  #The subreddit(s) that the bot will search in

# Login details
ID = ''
SECRET = ''
AGENT = 'a coinflipping script'
USER = 'flipacoinbot'
PASS = 'hunter2'
# End Vars

def bot():
    try:
        main()
    except:
        print('error, restarting')
        main()  #ignore exceptions by restarting


def main():
	reddit = praw.Reddit(client_id=ID,
	                     client_secret=SECRET',
	                     user_agent=AGENT,
	                     username=USER,
	                     password=PASS)
	subreddit = reddit.subreddit(SUBS)

	for comment in subreddit.stream.comments():
		proccess(comment)

def proccess(comment):
	normal_comment = comment.body.lower()   #make all comments lowercase to make easier proccessing
	for  call in TRIGGERS:
		if call in normal_comment and comment.author != USER:
			reply_text = REPLY_TEMP.format(random.choice(SIDES))
			comment.reply(reply_text)

			break


while True:
    bot()
