import requests


class WBOauth(object):
    def __init__(self):
        self.client_id = '4253417427'
        self.redirect_url = 'https://shuangsheng.cn/user/login?from=weibo'
        self.info_url = 'https://api.weibo.com/2/users/show.json'
        self.access_token_url = 'https://api.weibo.com/oauth2/access_token'

    def get_access_token(self, code):
        payload = {
            'client_id': self.client_id,
            'client_secret': '7be8d23b22773083a7c495a5189b7e52',
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_url
        }
        response = requests.post(self.access_token_url, payload).text
        print(response)
        return response

    def get_userinfo(self, access_token, uid):
        response = requests.get('{0}?access_token={1}&uid={2}'.format(self.info_url, access_token, uid))
        print(response.text)
        return response.text
