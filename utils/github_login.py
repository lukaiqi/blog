import requests
import re


class GitHubOauth():
    def __init__(self):
        self.client_id = 'd7f1ea44a2cd23821505'
        self.client_secret = '55098244dbb207221f6962e5d50e8dc829ce2cef'

    def get_auth_url(self):
        weibo_auth_url = 'https://github.com/login/oauth/authorize'
        auth_url = weibo_auth_url + '?client_id={}'.format(self.client_id)
        return auth_url

    def get_access_token(self, code):
        access_token_url = 'https://github.com/login/oauth/access_token'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Accept': 'application/json'
        }
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code

        }
        response = requests.post(access_token_url, headers=headers, data=payload)
        return response.text

    def get_user_info(self, access_token):
        user_url = 'https://api.github.com/user'
        access_token = access_token
        url = user_url + '?access_token=' + access_token
        response = requests.get(url=url)
        return response.text


if __name__ == '__main__':
    github = GitHubOauth()
    github.get_user_info('8375df8121a1fedd187472bce99085549fb995ef')
    # github.get_access_token('b84e17c56a53fe48054b')
