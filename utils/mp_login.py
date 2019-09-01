import json

import requests


class MPOauth(object):
    def __init__(self):
        self.appid = 'wx8aa6946ab2be69ca'
        self.secret = '7c1a0e850447bb6fa1ebd36840914966'
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
        try:
            openid = result['openid']
        except:
            openid = ''
        return openid


if __name__ == '__main__':
    mp = MPOauth()
    mp.get_openid('033Ea2G82QvZkL0gm0H82rV1G82Ea2Ga')
