import praw

# CREDENTIALS
client_id = "JUnxYbGENv-953eLxccLww"
client_secret = "rPJsCwuUusGoye5lIIgVICNSjOa9tw"
user_agent = "personal use script"
username = "Emotional-Zebra5359"
password = "thepsworld"

reddit_client = praw.Reddit(
  client_id=client_id,
  client_secret=client_secret,
  user_agent=user_agent,
  username=username,
  password=password,
)

sub = "AskWomen"

sub_resp = reddit_client.subreddit(sub)
comments = sub_resp.comments(limit = 10)
user_tags = []

for c in comments:
  print(c.body)
  try:
      user_tags.append(c.author_flair_text)
  except AttributeError:
      pass

print(user_tags)

