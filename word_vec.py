import numpy as np
from keras.preprocessing.sequence import pad_sequences
class embeddings(object):
	"""Class to deal with pre trained embeddings"""
	def __init__(self,filepath,word_index=None):
		
		self.filepath = filepath
		self.word_to_vec = dict()
		self.word_index = word_index
		self.char_index = None
		#loading pretrained embeddings
		with open(self.filepath,'r') as fp:
			for line in fp:
				values = line.split(' ')
				word = values[0]
				vector = values[1:]
				vector[-1] = vector[-1][:-1]
				self.word_to_vec[word] = vector
		self.embedding_length = len(list(self.word_to_vec.values())[0])

	def get_embedding_matrix(self,word_index,char_index=None,char_level=False):
		#if char_level is true then creating char based embedding matrix
		self.char_index = char_index
		if char_level == True:
			if char_index is None:
				print('char_index required')
				return None
			try:
				return self.get_char_embedding_matrix(char_index=char_index,word_index=word_index)
			except Exception as e:
				print(str(e))
				raise e
				return None
		#creating pretrained word vector based embeeding matrix		
		else:	
			try:
				return self.get_pretrained_embedding_matrix(word_index)
			except Exception as e:
				print(str(e))
				raise e
				return None

	def get_pretrained_embedding_matrix(self,word_index):
		print(len(word_index)+1,self.embedding_length)
		embedding_matrix = np.zeros((len(word_index)+1,self.embedding_length))

		for word,i in word_index.items():
			embedding_vector = self.get_word_vector(word)

			if embedding_vector is not None:
				#words not present in word_to_vec are by default vectot of all zeros
				embedding_matrix[i] = embedding_vector

		return embedding_matrix

	def get_char_embedding_matrix(self,char_index=None,word_index=None):
		#if char_index and word_index not provided using default values from main class
		if char_index is None:
			char_index = self.char_index
		if word_index is None:
			word_index = self.word_index
					
		embedding_length = len(max(word_index,key=len))
		embedding_matrix = []

		for word in word_index.keys():
			embedding_vector = self.get_char_vector(word)
			embedding_matrix.append(embedding_vector)

		embedding_matrix = pad_sequences(np.array(embedding_matrix),padding='post',value=0)	
		return embedding_matrix	

	def get_sentence_vectors(self,sentence):
		"""Return the word vectors for a coomplete sentence as python list """
		ret_sent = []
		for word in sentence.split(' '):
			ret_sent.append(self.get_word_vector(word))
		return ret_sent	
	
	def get_word_vector(self,word):
		"""return vector for a giiven word"""
		ret_vec = np.zeros(self.embedding_length)	
		vector = self.word_to_vec.get(word)

		if vector is None:
			vector = self.word_to_vec.get(str(word).lower())

		if vector is not None:
			ret_vec = vector

		return ret_vec			

	def get_char_vector(self,word,char_index=None):
		if char_index is None:
			char_index = self.char_index
		ret_vec = [char_index.get(c) for c in str(word)]
		return ret_vec



		
			


								