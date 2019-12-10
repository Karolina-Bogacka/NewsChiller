from sklearn.model_selection import train_test_split
import time
from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
import pandas as pd
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from nltk import word_tokenize
import pickle
import dill
import re
import numpy as np
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.backend import set_session

#Categories are - in this order
categories = ['POLITICS', 'WELLNESS', 'ENTERTAINMENT', 'TRAVEL',
'STYLE & BEAUTY', 'PARENTING', 'HEALTHY LIVING', 'QUEER VOICES', 'FOOD & DRINK',
'BUSINESS']

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
stop_words_ = set(stopwords.words('english'))
wn = WordNetLemmatizer()

my_sw = ['make', 'amp',  'news','new' ,'time', 'u','s', 'photos',  'get', 'say']
def black_txt(token):
    return  token not in stop_words_ and token not in list(string.punctuation)  and len(token)>2 and token not in my_sw

def to_sequence(tokenizer, preprocessor, index, text):
   words = tokenizer(preprocessor(text))
   indexes = [index[word] for word in words if word in index]
   return indexes

global session
session = tf.Session(graph=tf.Graph())

with session.graph.as_default():
    K.set_session(session)
    model = load_model('model_dir/modelstopic1.h5')

global graph
graph = tf.get_default_graph()

def classify(txt):
    with open('model_dir/vectorizer.pkl', 'rb') as handle:
        vectorizer = dill.load(handle)
    word2idx = {word: idx for idx, word in enumerate(vectorizer.get_feature_names())}
    tokenize = vectorizer.build_tokenizer()
    preprocess = vectorizer.build_preprocessor()
    example = [to_sequence(tokenize, preprocess, word2idx, txt)]
    example = pad_sequences(example, maxlen=42, value=len(vectorizer.get_feature_names()))
    with session.graph.as_default():
        K.set_session(session)
        pred = model.predict(example)
    list = pred[0]
    prediction = np.argmax(list)
    return categories[prediction]
