import praw, time, random


r = praw.Reddit(user_agent = "User-Agent: Python/urllib:coinflip  (by /u/lizardsrock4)")
print("Logging in")
r.login('flipacoinbot','hunter2')    #Logs In

word_array = ["flip a coin", "flipacoin", "coinflip","coin flip","flipacoinbot"]    #Array of triggers
cache = []    #Empty array that will store comments that have already been replied to

banned_subs = ["MechanicalKeyboards", "AskReddit", "legaladvice", "dota2loungebets", "MLS"]    #Array of subs that have requested for the bot to not post to


def run_bot():
    try:
        print("Starting Stream")
        stream = praw.helpers.comment_stream(r, "all", limit=None, verbosity=3)    #Starts PRAW stream to find comments that want a coin to be flipped
        for comment in stream:
            comment_text = comment.body.lower()
            isMatch = any(string in comment_text for string in word_array)
            notBanned = comment.subreddit.display_name in banned_subs
            if comment.id not in cache and isMatch:    #Checking each comment to see if it is a match and has not already been replied to
                if comment.id is not notBanned:
            
                    #print("Match Found! Comment id:" + comment.id + " Subreddit: " + comment.subreddit.display_name)    #Used for debugging
                    sides = ["Heads", "Tails"]
                    result = random.choice(sides)    #Chooses a side
                    comment.reply("You asked for a coin to be flipped, so I flipped one for you, the result was: **" + result +
                                  "**\n\n ---- \n\n ^This ^bot's ^messages ^aren't ^checked ^often, ^for ^the ^quickest ^response," +
                                  " ^click ^[here](/message/compose?to=/u/lizardsrock4&subject=Bot) ^to ^message ^my ^maker.")    #Replies to the comment with choosen side
                    cache.append(comment.id)    #Adds comment to cache so it won't be replied to again
                else:
                    #print("Match found, but comment was in a banned sub")    #Debugging
                    pass
    except Exception:    #Catches any messups and restarts bot
        print("Error")
        run_bot()

while True:
    run_bot()
