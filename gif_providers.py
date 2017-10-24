"""
Gets GIFs from reddit 
"""
import praw
import link_extractors

class GifRedditProvider():
    """ Gets GIFs from specific subreddit"""
    def __init__(self, subredditName, client_id, client_secret, user_agent, username, password):
        self.subredditName = subredditName
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.username = username
        self.password = password


    def get_gif(self, exclude_list):
        """ Gets gif """
        reddit = praw.Reddit(client_id = self.client_id, 
                                client_secret=self.client_secret, 
                                user_agent=self.user_agent,
                                username=self.username,
                                password=self.password)
        subreddit = reddit.subreddit(self.subredditName)          
        result = None
        for submission in subreddit.submissions():
            link = None
            if submission.id not in exclude_list:
                link = link_extractors.RedditLinkExtractor.extract(submission)
                if link != None:
                    result = {'link': link, 'id': submission.id}
                    break
        return result


    