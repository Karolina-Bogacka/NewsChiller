from simpletransformers.classification import ClassificationModel

model_bert_binary = ClassificationModel('roberta', 'filter_dir/model_dir/binary_outputs2/', use_cuda=False)

def classify_bert(txt):
    pred = model_bert_binary.predict(txt)
    distress = pred[0][0]
    return distress
