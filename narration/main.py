import pandas as pd 
import numpy as np

from train_process import SentenceGetter 
import matplotlib.pyplot as plt
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from word_vec import embeddings
from predicter import extract
import os
#from imagedownloader import downloader as Downloader
cwd = os.getcwd()
embeds = embeddings('narration/datasets/glove.6B.50d.txt')
model2 = load_model('narration/saved_model/model.h5')
model2._make_predict_function()


def imager(text):
    #print('imager started')
    keywords = np.array(extract(model2 , text , embeds))
    indexes = np.unique(keywords, return_index=True)[1]
    keywords = [keywords[index] for index in sorted(indexes)]
    print(keywords)
    #downloader1  = Downloader()
    #names = []
    #u = 1
    #for i in keywords:
    #    _Title = Title + str(u)
    #    names.append(downloader1.download(i, _Title))
    #    u += 1
    #print('imager over in main')
    return keywords