import os
import tweepy


def twit_auth_handler():
    cons_tok = os.environ.get('CONS_TOK')
    cons_sec = os.environ.get('CONS_SEC')
    app_tok = os.environ.get('APP_TOK')
    app_sec = os.environ.get('APP_SEC')

    auth = tweepy.OAuthHandler(cons_tok, cons_sec)
    auth.set_access_token(app_tok, app_sec)

    return tweepy.API(auth)
