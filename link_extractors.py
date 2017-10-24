""" Module contains extractors for links """
class RedditLinkExtractor():
    """ Class for extract link from reddit entities """
    @staticmethod
    def extract(submission):
        """ Extract link from submission """
        media = submission.media
        if media:
            media_type = media['type']
            if media_type == 'gfycat.com' or media_type == 'imgur.com':
                oembed = media['oembed']
                return oembed['thumbnail_url']
        return None
