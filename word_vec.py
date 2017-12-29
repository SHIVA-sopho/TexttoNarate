import numpy as np

class embeddings(object):
	"""Class to deal with pre trained embeddings"""
	def __init__(self,filepath):
		
		self.filepath = filepath
		self.word_to_vec = dict()
		#loading pretrained embeddings
		with open(self.filepath,'r') as fp:
			for line in fp:
				values = line.split(' ')
				word = values[0]
				vector = values[1:]
				self.word_to_vec[word] = vector
		self.embedding_length = len(list(self.word_to_vec.values())[0])

	def get_embedding_matrix(self,word_index):
		print(len(word_index)+1,self.embedding_length)
		embedding_matrix = np.zeros((len(word_index)+1,self.embedding_length))

		for word,i in word_index.items():
			embedding_vector = self.get_word_vector(word)

			if embedding_vector is not None:
				#words not present in word_to_vec are by default vectot of all zeros
				embedding_matrix[i] = embedding_vector

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
			vector = self.word_to_vec.get(word.lower())

		if vector is not None:
			ret_vec = vector

		return ret_vec			