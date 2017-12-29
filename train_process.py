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
			 




				


		