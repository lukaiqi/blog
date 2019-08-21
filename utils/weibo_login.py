import requests
import re


class WeiBoOauth():
    def __init__(self):
        self.client_id = '4253417427'
        # self.redirect_url = 'http://lkqblog.cn:8080/user/oauth'
        self.redirect_url = 'http://vue.lkqblog.cn/user/oauth?type=weibo'

    def get_auth_url(self):
        weibo_auth_url = 'https://api.weibo.com/oauth2/authorize'
        auth_url = weibo_auth_url + '?client_id={}&redirect_uri={}'.format(self.client_id, self.redirect_url)
        return auth_url

    def get_access_token(self, code):
        access_token_url = 'https://api.weibo.com/oauth2/access_token'
        payload = {
            'client_id': self.client_id,
            'client_secret': '7be8d23b22773083a7c495a5189b7e52',
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_url
        }
        return requests.post(access_token_url, data=payload).text

    def get_user_info(self, access_token, uid):
        user_url = 'https://api.weibo.com/2/users/show.json'
        access_token = access_token
        uid = uid
        url = user_url + '?access_token=' + access_token + '&uid=' + uid
        response = requests.get(url=url)
        return response.text


if __name__ == '__main__':
    qq = WeiBoOauth()
    qq.get_auth_url()
