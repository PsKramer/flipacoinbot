import praw, random

TRIGGERS = ['flip a coin', 'coinflip', 'flipacoin', 'heads or tails']
REPLY_TEMP = 'As you requested, I flipped a coin for you, the result was **{}** \n\n --- \n\n ^^For ^^more ^^information/to ^^complain ^^about ^^me, ^^see ^^/r/flipacoinbot'
SIDES = ['Heads', 'Tails']

def main():
	reddit = praw.Reddit(client_id='[id]',
	                     client_secret='[secret]',
	                     user_agent='a coin flipping script',
	                     username='flipacoinbot',
	                     password='hunter2')
	subreddit = reddit.subreddit('all-askreddit-suicidewatch')

	for comment in subreddit.stream.comments():
		proccess(comment)

def proccess(comment):
	normal_comment = comment.body.lower()
	for  call in TRIGGERS:
		if call in normal_comment and comment.author != 'flipacoinbot':
			reply_text = REPLY_TEMP.format(random.choice(SIDES))
			comment.reply(reply_text)

			break


if __name__ == '__main__':
    try:
        main()
    except:
        print(error, restarting)
        main()
