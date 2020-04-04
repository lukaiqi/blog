import json

import requests


class MPOauth(object):
    def __init__(self):
        self.appid = 'wx8aa6946ab2be69ca'
        self.secret = '1104788f58dcc6059dba150047c1ecdf'
        self.grant_type = 'authorization_code'

    def get_openid(self, code):
        url = 'https://api.weixin.qq.com/sns/jscode2session'
        payload = {
            'appid': self.appid,
            'secret': self.secret,
            'grant_type': 'authorization_code',
            'js_code': code,
        }
        response = requests.get(url, payload)
        result = json.loads(response.text)
        openid = result['openid']
        return openid


if __name__ == '__main__':
    mp = MPOauth()
    mp.get_openid('043je5vC1RKWH50z03vC1qMZuC1je5vo')
