from simpletransformers.classification import MultiLabelClassificationModel

model_bert = MultiLabelClassificationModel('roberta', 'filter_dir/model_dir/second_outputs/', use_cuda=False)

def classify_bert(txt):
    pred = model_bert.predict([txt])
    print(pred[0][0][0])
    if pred[0][0][0]==1:
        distress = 1
    elif pred[0][0][1]==1:
        distress = -1
    elif pred[0][0][2]==1:
        distress = 0
    return distress
