import requests
import json

url = 'https://spreadsheets.google.com/feeds/list/1zBeYVkoyLavJIIBKJ9aG8ID_ZtLe-UHeKK72hk_ZKfE/1/public/values?alt=json'


response = requests.get(url)
jobs = json.loads(response)