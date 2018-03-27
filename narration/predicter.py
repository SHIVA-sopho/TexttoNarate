from train_process import TestProcessor
import numpy as np
def extract(model2, text, embeds):
    sen = text
    tp = TestProcessor(sen, embeds)
    sent = tp.sentences
    sent = sent.astype('float32')
    try:
        pred = model2.predict(sent)    
    except Exception as e:
        raise e
    predict = np.argmax(pred,axis=-1)
    sent = sen.split(". ")
    for i , s in enumerate(sent):
        sent[i] = s.split(" ")
    raw = sent
    keywords = []
    for i, s in enumerate(raw):
        j = 0
        while(True):
            keyword = ''
            if predict[i][j] != 0:
                keyword = keyword + raw[i][j]
                while(predict[i][j] != 0):
                    if predict[i][j+1] != 0 :
                        keyword = keyword + " "+ raw[i][j+1]
                        j = j+1
                    else:
                        break
            j = j+1
            if keyword != '':
                keywords.append(keyword)
            if j == 102:
                break
    return keywords