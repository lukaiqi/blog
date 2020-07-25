import os

import requests


class WBOauth(object):
    def __init__(self):
        self.client_id =os.environ['WB_APPID']
        self.redirect_url = 'https://ishuangsheng.cn/web/user_login?from=weibo'
        self.info_url = 'https://api.weibo.com/2/users/show.json'
        self.access_token_url = 'https://api.weibo.com/oauth2/access_token'
        self.client_secret = os.environ['WB_SECRET']

    def get_access_token(self, code):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_url
        }
        response = requests.post(self.access_token_url, payload)
        return response.text

    def get_userinfo(self, access_token, uid):
        response = requests.get('{0}?access_token={1}&uid={2}'.format(self.info_url, access_token, uid))
        return response.text
