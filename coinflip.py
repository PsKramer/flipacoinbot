import praw, time, random, os
#import truerandom.py


r = praw.Reddit(user_agent = "User-Agent: Python/urllib:coinflip  (by /u/lizardsrock4)")
print("Logging in")
r.login()

word_array = ["flip a coin", "flipacoin", "coinflip", "flip a coin", "coin flip", "!flipacoin", "flipacoinbot", "/u/flipacoinbot"]
cache = []

banned_subs = ["MechanicalKeyboards", "AskReddit", "legaladvice", "dota2loungebets", "MLS"]


def run_bot():
    try:
        print("Starting Stream")
        stream = praw.helpers.comment_stream(r, "all", limit=None, verbosity=3)
        for comment in stream:
            comment_text = comment.body.lower()
            isMatch = any(string in comment_text for string in word_array)
            notBanned = comment.subreddit.display_name in banned_subs
            if comment.id not in cache and isMatch:
                if comment.id is not notBanned:
            
                    #print("Match Found! Comment id:" + comment.id + " Subreddit: " + comment.subreddit.display_name)
                    randInt = random.randint(0, 1)
                    if randInt == 1:
                        comment.reply("You asked for a coin to be flipped, so I flipped one for you, the result was: **Tails**\n\n ---- \n\n ^This ^bot's ^messages ^aren't ^checked ^often, ^for ^the ^quickest ^response, ^click ^[here](/message/compose?to=lizardsrock4&subject=CoinBot) ^to ^message ^my ^maker \n\n ^Check ^out ^my ^[source](http://github.com/lizardsrock4)")
                        #print("Tails!")
                        cache.append(comment.id)
                    elif randInt == 0:
                        comment.reply("You asked for a coin to be flipped,so I flipped one for you, the result was: **Heads**\n\n ---- \n\n  ^This ^bot's ^messages ^aren't ^checked ^often, ^for ^the ^quickest ^response, ^click ^[here](/message/compose?to=lizardsrock4&subject=CoinBot) ^to ^message ^my ^maker \n\n ^Check ^out ^my ^[source](http://github.com/lizardsrock4)")
                        #print("Heads!")
                        cache.append(comment.id)
                else:
                    #print("Match found, but comment was in a banned sub")
                    pass
    except Exception:
        print("Error")
        run_bot()
def cls():
    os.system('cls')

while True:
    run_bot()
