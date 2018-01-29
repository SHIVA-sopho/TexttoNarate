from keras.preprocessing.sequence import pad_sequences
import numpy as np

class SentenceGetter(object):
	"""takes input data and gives out sentences"""
	def __init__(self, data):
		
		self.n_sent = 1
		self.data = data

		agg_func = lambda s:[(w,p,t) for w,p,t in zip(s['Word'].values.tolist(),
													  s['POS'].values.tolist(),
													  s['Tag'].values.tolist())]
		self.grouped = self.data.groupby('Sentence').apply(agg_func)
		self.sentences = self.grouped.tolist()

	def get_next(self):

		try:
			sent = self.grouped['Sentence: {}'.format(self.n_sent)]
			self.n_sent += 1
			return sent
		except Exception as e:
			return None
			
			 
			
class TestProcessor(object):
					""" Class for handling Test data"""
					def __init__(self, data, embeds):
						print('inside constructor')
						self.sentences = data.split('. ')
						self.embeds = embeds
						self.pad_len = 0
						print(self.sentences)
						for i, sent in enumerate(self.sentences):
							self.sentences[i] = sent.split(' ')
							#if len(self.sentences[i]) > self.pad_len:
							#	self.pad_len = len(self.sentences[i])
						#self.sentences = np.array(self.sentences)
						self.pad_sequences(self.sentences,value='ghansham')
						self.raw_sentences = self.sentences
						for i,sent in enumerate(self.sentences):
							self.sentences[i] =  self.get_sentence_vectors(sent)
						self.sentences = np.array(self.sentences)

					def get_sentence_vectors(self,sent):
						rt_sent = []
						for word in sent:
							rt_sent.append(self.embeds.get_word_vector(word))

						return rt_sent	

									
										
					def pad_sequences(self,sequences,value,max_len = 104):
						for i,sent in enumerate(sequences):
							for j in range(0,104-len(sent)):
								sequences[i] += [value]


		