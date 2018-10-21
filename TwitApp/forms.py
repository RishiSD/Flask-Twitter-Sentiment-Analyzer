from wtforms import Form, StringField, IntegerField, validators


class TweetForm(Form):
    search_key = StringField('search_key',
                             validators=[validators.InputRequired()])
    tweet_count = IntegerField('tweet_count',
                               validators=[validators.InputRequired()])
