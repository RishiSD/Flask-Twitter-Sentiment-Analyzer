from flask import Blueprint, request, render_template

from TwitApp.data import TwitterMain
from TwitApp.forms import TweetForm

tweet = Blueprint('tweet', __name__)

title = 'Twitter Sentiment Analyser'


@tweet.route('/')
def my_form():
    form = TweetForm(request.form)
    return render_template('index.html', title=title, form=form)


@tweet.route('/', methods=['POST'])
def my_form_post():
    text = request.form['search_key']
    count = int(request.form['tweet_count'])
    twit_main = TwitterMain()
    tweets, rand_id = twit_main.get_trends(text, count)
    return render_template('disp.html', title=title,
                           search_key=text, rand_id=rand_id,
                           render_list=tweets)


@tweet.route('/analysis/<key>/<int:rand_id>')
def analysis(key, rand_id):
    data = TwitterMain.get_analysis_data(key, rand_id)
    return render_template('analysis.html', title=title,
                           search_key=key, data=data)
