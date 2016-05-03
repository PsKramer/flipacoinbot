import praw, random

UA = "User-Agent: Python/urllib:coinflip  (by /u/lizardsrock4)"
triggers = ["flip a coin", "coinflip", "coin flip", "flipacoinbot", "heads or tails"]
cache = []

def check_condition(c):
    text = c.body.lower()
    if any(string in text for string in triggers):
        if c.id not in cache:
            return True
    return False

def bot_action(c, respond=True):
    sides = ["Heads", "Tails"]
    result = random.choice(sides)

    if respond:
        start = "As you have requested, I have flipped a coin, the result was: **"
        end = "**\n\n ---- \n\n ^This ^bot's ^messages ^aren't ^checked ^often, ^for ^the ^quickest ^response, ^click ^[here](/message/compose?to=/r/flipacoinbot&subject=Bot) ^to ^message ^my ^maker."
        cache.append((c.reply(start + result + end)).id)
        cache.append(c.id)
        

while True:
    r = praw.Reddit(UA)
    r.login('flipacoinbot','hunter2')
    
    for c in praw.helpers.comment_stream(r, 'all'):
        if check_condition(c):
            bot_action(c, respond=True)
