from datetime import date
from GoogleNews import GoogleNews
news = GoogleNews()
news.set_lang('en')
date_today = date.today()
news.set_time_range('01/11/2020',date_today)
news.set_encode('utf-8')
topic = input("Topic : ")
news.search(topic)
news.get_page(2)
#headlines with links WORLD NEWS
for i in range(6):
    print(news.results()[i]["title"])
    print(news.results()[i]["link"])
