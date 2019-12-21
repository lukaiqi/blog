import json
from urllib.parse import parse_qs

import requests


class QQOauth(object):
    def __init__(self):
        self.appid = '101772638'
        self.client_secret = '0f138d861e33982754deb1882880133a'
        self.redirect_uri = 'https://ishuangsheng.cn/user/login?from=qq'
        self.info_url = 'https://graph.qq.com/user/get_user_info'
        self.open_id_url = 'https://graph.qq.com/oauth2.0/me'

    def get_access_token(self, code):
        access_token_url = 'https://graph.qq.com/oauth2.0/token'
        payload = {
            'client_id': self.appid,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        response = requests.get(url=access_token_url, params=payload)
        result = response.text
        print(result)
        access_token = parse_qs(result)['access_token'][0]
        # print(access_token)
        return access_token

    def get_openid(self, access_token):
        payload = {
            'access_token': access_token
        }
        response = requests.get(url=self.open_id_url, params=payload)
        temp = response.text.replace('callback', '').replace('(', '').replace(')', '').replace(';', '').strip()
        openid = json.loads(temp)['openid']
        return openid

    def get_userinfo(self, access_token, openid):
        payload = {
            'access_token': access_token,
            'oauth_consumer_key': self.appid,
            'openid': openid
        }
        response = requests.get(url=self.info_url, params=payload)
        return response.text
