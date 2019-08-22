import json
from urllib.parse import parse_qs

import requests


class QQOauth(object):
    def __init__(self):
        self.appid = '101772638'
        self.client_secret = '0f138d861e33982754deb1882880133a'
        self.redirect_uri = 'https://ishuangsheng.cn/qq/bind'
        # self.redirect_uri = 'http://127.0.0.1:8080/#/qq/bind'

    def get_auth_url(self):
        qq_auth_url = 'https://graph.qq.com/oauth2.0/authorize'
        auth_url = qq_auth_url + '?response_type=code&client_id={}&redirect_uri={}&state=mlws' \
            .format(self.appid, self.redirect_uri)
        return auth_url

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

    def get_open_id(self, access_token):
        open_id_url = 'https://graph.qq.com/oauth2.0/me'
        payload = {
            'access_token': access_token
        }
        response = requests.get(url=open_id_url, params=payload)
        temp = response.text.replace('callback', '').replace('(', '').replace(')', '').replace(';', '').strip()
        openid = json.loads(temp)['openid']
        return openid

    def get_user_info(self, access_token, openid):
        info_url = 'https://graph.qq.com/user/get_user_info'
        payload = {
            'access_token': access_token,
            'oauth_consumer_key': self.appid,
            'openid': openid
        }
        response = requests.get(url=info_url, params=payload)
        # print(response.text)
        return response.text


if __name__ == '__main__':
    QQOauth().get_user_info('657C692EC74583AF1C44EBF88E230B82', 'D1383F8B7FB0919CC31AFAD58D440CB1')
    # QQOauth().get_open_id('657C692EC74583AF1C44EBF88E230B82')
