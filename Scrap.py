from bs4 import BeautifulSoup
import requests


r = requests.post('http://httpbin.org/post', data = {'UserId':'12345', 'Status':'On'})
if r.status_code == 200:
    print('Good')
else:
    print("ERROR", r.status_code)


response = requests.get('https://yandex.ru/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html5lib")

span_list = soup.find_all('span',
                          {'class': 'desk-notif-card__covid-histogram-desc-count'})


print(span_list)