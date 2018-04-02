import scrapy

class Submission(scrapy.Item):
    '''        List of fields to Extract per submission
                - Id
                - Description
                - Submission_Link
                - Meneame_link
                - Submitter ( User)
                - Content
                - Meneos
                - Clicks
                - Positive_votes
                - Negative_votes
                - Karma
                - Tags (have to take it from inside link)

    '''

    id = scrapy.Field()