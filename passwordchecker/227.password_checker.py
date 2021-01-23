import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

# def read_res(response):
#     print(response.text)

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    print(response) #Czemu tutaj nie moge dac print response a jak printne w funkcji to mam ciag liczb
    return (response)

pwned_api_check('123')