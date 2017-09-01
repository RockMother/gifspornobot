import os
import praw

def get_link(submission):
  media = submission.media
  oembed = media['oembed']
  return oembed['thumbnail_url']

def get_random_gif():
  reddit = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'], 
                        client_secret=os.environ['REDDIT_CLIENT_SECRET'], 
                        user_agent=os.environ['REDDIT_USER_AGENT'],
                        username=os.environ['REDDIT_USERNAME'],
                        password=os.environ['REDDIT_PASSWORD'])
  subreddit = reddit.subreddit('porn_gifs')   
  link = None
  while link == None:
    try:
      link = get_link(subreddit.random())
    except:
      print("No link")
      link = None
  return link