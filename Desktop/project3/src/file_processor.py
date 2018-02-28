
class file_processor:

	def __init__ (self, filePath):
		self.pos_inverted_index = {}
		self.docID = filePath.split('/')[-2] + '/' + filePath.split('/')[-1]
		self.filePath = filePath
		self.title = ''
		self.body = ''
		self.filePath = filePath


	def split_body_title (self):
		res_str = ''
		with open(self.filePath, 'rt') as fin:
			res_str = fin.read()

		#some documents missing <body> tags. 
		if '<body>' in res_str:
			split_list = res_str.split('<body>')
			self.title = split_list[0]
			self.body = split_list[1].replace('</body>', '')
			
		else:
			self.title = ''
			self.body = res_str

		return self.title, self.body

#return list of tuples: [(pos, word1), (pos, word2), (pos, word1), (pos, word3).....]
#one word may appear multiple times - pass it to aggregate_pos_list to handle

	def tokenizer(self, inStr):
		import nltk
		import string
		from tokenize import tokenize
		from nltk.tokenize import WhitespaceTokenizer
		#import collections
		#from collections import OrderedDict
		#from collections import Counter

		res_tokens = []
		freq_dict = {}
		translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

		outStr = inStr.replace("'","")
		outStr = outStr.translate(translator).lower()
		tempStr = outStr.split()

		word_pos_list = list(enumerate(tempStr))
		#tokens = nltk.word_tokenize(outStr)
		#freq_dict = dict(collections.Counter(tokens))
		return word_pos_list


#return dictonary: {term1: {docID: [pos1, pos2]}, term2: {docID: [pos1, pos2, pos3, ..., posN]} .... termN: {docID: [pos1, pos2... posN]} }
#docIDs will be the same. This is for the ease of merging with other docs.

	def aggregate_pos_list (self, counter_list):
		for tup in counter_list:
			doc_dict = {}
			if tup[1] not in self.pos_inverted_index:
				doc_dict[self.docID] = [tup[0]]
				self.pos_inverted_index[tup[1]] = doc_dict
			else:
				self.pos_inverted_index[tup[1]][self.docID].append(tup[0])
		return self.pos_inverted_index


		




import argparse

def main():
	parser = argparse.ArgumentParser(description='Main program for indexing documents.')
	parser.add_argument('-i', '--input_file', type=str, help='Name of the input document')
	parser.add_argument('-o', '--output_file', type=str, help='Name of output file for the index table')
	args = parser.parse_args()

	tester = file_processor(args.input_file)
	title, body = tester.split_body_title()
	tokens = tester.tokenizer(body)
	#print tokens
	#print tester.computeWordFrequencies(tokens)

	print tester.aggregate_pos_list(tokens)

if __name__ == "__main__":
    main()



