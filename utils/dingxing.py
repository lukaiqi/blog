import json
import requests


class DingXing(object):
    def __init__(self, app_code):
        self.app_code = app_code
        self.host = 'http://dingxin.market.alicloudapi.com/dx/sendSms'

    def send_sms(self, mobile, code):
        payload = {
            'mobile': mobile,
            'param': 'code:' + code,
            'tpl_id': 'TP1712202'
        }
        headers = {
            'Authorization': 'APPCODE ' + self.app_code
        }
        # print(headers,payload)
        response = requests.post(url=self.host, data=payload, headers=headers)
        re_dict = json.loads(response.text)
        return re_dict
