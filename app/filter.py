from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import pickle

# load model
global model
loaded_model = load_model('model_dir/models819.h5')
global graph
graph = tf.compat.v1.get_default_graph
max_len = 42

with open('model_dir/tokenizer819.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

set_filter = 0

def classify(txt):
    seq= loaded_tokenizer.texts_to_sequences([txt])
    padded = pad_sequences(seq, maxlen=max_len)
    global graph
    with graph.as_default():
        pred = loaded_model.predict(padded)
    if round(pred[0][0])==1:
        distress = 1
    elif round(pred[0][1])==1:
        distress = -1
    elif round(pred[0][2])==1:
        distress = 0
    distress
