""" Module contains extractors for links """
class RedditLinkExtractor():
    """ Class for extract link from reddit entities """
    @staticmethod
    def extract(submission):
        """ Extract link from submission """
        media = submission.media
        if media['type'] == 'gfycat.com' or media['type'] == 'imgur.com':
            oembed = media['oembed']
            return oembed['thumbnail_url']
        else:
            return None
