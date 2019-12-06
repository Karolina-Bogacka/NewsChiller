from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
import pandas as pd
from keras.preprocessing.sequence import pad_sequences
import pickle
from keras import backend as K

set_filter = 0
loaded_model = load_model('model_dir/models819.h5')
#self.loaded_model._make_predict_function()
#self.graph = tf.compat.v1.get_default_graph
with open('model_dir/tokenizer819.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

def classify(txt):
    seq= loaded_tokenizer.texts_to_sequences([txt])
    padded = pad_sequences(seq, maxlen=42)
    with K.get_session().graph.as_default() as graph:
        pred = loaded_model.predict(padded)
    if round(pred[0][0])==1:
        distress = 1
    elif round(pred[0][1])==1:
        distress = -1
    elif round(pred[0][2])==1:
        distress = 0
    print("distressed in classify")
    print(distress)
    distress
