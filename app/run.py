from app import app
from db import db
from models import article, source
import routes
import main_feed
import filter
import re
from nltk import word_tokenize
import topicfilter
from threading import Thread
import time
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
stop_words_ = set(stopwords.words('english'))
wn = WordNetLemmatizer()

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

my_sw = ['make', 'amp',  'news','new' ,'time', 'u','s', 'photos',  'get', 'say']
def black_txt(token):
    return  token not in stop_words_ and token not in list(string.punctuation)  and len(token)>2 and token not in my_sw

with app.app_context():
    db.create_all()

def updating_loop():
    while True:
        with app.app_context():
            q = source.Source.query
            for src in q.all():
                try:
                    update_source(src)
                except:
                    continue
        time.sleep(15*60)

def update_source(src):
    parsed = main_feed.parsing_method(src.feed)
    articles = main_feed.articles_get(parsed)
    article.Article.insert_feed(src.id, articles)


print("classify works")
print(filter.distress_classify("text"))
thread = Thread(target=updating_loop)
thread.start()
app.run(use_reloader=False)
