import os
import tweepy


def twit_auth_handler():
    cons_tok = 'lbCYp2p5I70uplUK5WxzcjprM'
    cons_sec = 'gPlctghseUCy6ooTsEBSF95MTajmdHs6xINU5F4cL2sC7DGJVf'
    app_tok = '2898362052-nn71389b4DWYtvXjdE22Vu1AHni6Yt5VRXRcDzY'
    app_sec = 'lOKf4e01uCcY2BpW6DYTSLyzUGFir1NSND1cLcZxX1JzL'
 #   cons_tok = os.environ.get('CONS_TOK')
 #   cons_sec = os.environ.get('CONS_SEC')
 #   app_tok = os.environ.get('APP_TOK')
 #   app_sec = os.environ.get('APP_SEC')

    auth = tweepy.OAuthHandler(cons_tok, cons_sec)
    auth.set_access_token(app_tok, app_sec)

    return tweepy.API(auth)
