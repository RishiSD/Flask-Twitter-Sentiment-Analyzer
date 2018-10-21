from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from TwitApp import db


class Tweet(db.Model):

    __tablename__ = 'Tweets'

    id = db.Column(db.Integer, primary_key=True)
    rand_id = db.Column(db.Integer)
    tag = db.Column(db.String())
    tweet_id = db.Column(db.String())
    lang = db.Column(db.String())
    text = db.Column(db.String())
    sentiment = db.Column(db.Float)
    datetime = db.Column(db.String())

    def __init__(self, rand_id, tag, tweet_id, lang, text):
        self.rand_id = rand_id
        self.tag = tag
        self.tweet_id = tweet_id
        self.lang = lang
        self.text = text
        self.sentiment = SentimentIntensityAnalyzer().polarity_scores(text)['compound']
        self.datetime = str(datetime.now())

    @classmethod
    def save_all_to_db(cls, tweet_list):
        if tweet_list:
            db.session.add_all(tweet_list)
            db.session.commit()

    @classmethod
    def del_all_by_key(cls, tag, rand_id):
        cls.query.filter_by(tag=tag, rand_id=rand_id).delete()
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
