import os
import praw
import visitors

def get_link(submission):
  media = submission.media
  if media['type'] == 'gfycat.com' or media['type'] == 'imgur.com':
    oembed = media['oembed']
    return oembed['thumbnail_url']
  else:
    return None

def get_subreddit():
  reddit = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'], 
                        client_secret=os.environ['REDDIT_CLIENT_SECRET'], 
                        user_agent=os.environ['REDDIT_USER_AGENT'],
                        username=os.environ['REDDIT_USERNAME'],
                        password=os.environ['REDDIT_PASSWORD'])
  return reddit.subreddit('porn_gifs')   

def get_next_link(chat_id):
  subreddit = get_subreddit()
  result = None
  visited = visitors.getVisited(chat_id)
  for submission in subreddit.submissions():
    try:
      link = None
      if submission.id not in visited:
        link = get_link(submission)
    except:
      print("No link")
      link = None    
    if link != None:
      visitors.saveVisited(chat_id, submission.id)
      result = link
      break
  return result

def get_random_gif():
  subreddit = get_subreddit()
  link = None
  while link == None:
    try:
      link = get_link(subreddit.random())
    except:
      print("No link")
      link = None
  return link