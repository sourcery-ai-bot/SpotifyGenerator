'''
P.S.: I could just make the password a random hash, but it being base64 just seems more simple.
'''

import requests, random, string, base64


def random_strings(char_num) -> str:
       return ''.join(random.choices(string.ascii_letters, k=char_num))


class SpotifyGenerator:
    def __init__(self, username) -> None:
           self.username = username
           self.email = f'{self.username}{random_strings(5)}@gmail.com'
           self.password = base64.b64encode(username.encode()).decode()
           self.request_url = 'https://spclient.wg.spotify.com/signup/public/v1/account'
           self.headers = {
               'authority': 'spclient.wg.spotify.com',
               'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
               'sec-ch-ua-platform': '"Windows"',
               'content-type': 'application/x-www-form-urlencoded',
               'accept': '*/*',
               'origin': 'https://www.spotify.com',
               'sec-fetch-site': 'same-site',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://www.spotify.com/',
               'accept-language': 'en-US,en;q=0.9'
           }
           self.data = {
               'birth_day': '01',
               'birth_month': '01',
               'birth_year': '1969',
               'creation_flow': '',
               'creation_point': '"https://www.spotify.com/us/',
               'displayname': self.username,
               'username': self.username,
               'gender': random.choice(['male', 'female', 'neutral']),
               'iagree': '1',
               'key': 'a1e486e2729f46d6bb368d6b2bcda326',
               'platform': 'www',
               'referrer': 'https://www.spotify.com/us/',
               'send-email': '0',
               'thirdpartyemail': '0',
               'email': self.email,
               'password': self.password,
               'password_repeat': self.password
           }
    
    def generate_account(self) -> str:
        r = requests.post(self.request_url, headers=self.headers, data=self.data)
        if 'login_token' in r.text:
            return r.text
        else:
            raise Exception('Failed to create account')



if __name__ == "__main__":
    account_gen = SpotifyGenerator(username=random_strings(10))
    generated_account = account_gen.generate_account()
    print(generated_account)
