
class file_processor:

	def __init__ (self, filePath, docID, outFile):
		self.pos_inverted_index = {}
		self.docID = docID
		self.filePath = filePath
		self.title = ''
		self.body = ''
		self.filePath = filePath
		self.outFile = outFile

	def split_body_title (self):
		import io
		res_str = ''
		with open(self.filePath, 'r') as fin:
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
		from nltk.corpus import stopwords
		#from nltk.stem.porter import *

		stop_words = set(stopwords.words('english')) 
		#stemmer = PorterStemmer()
		#import collections
		#from collections import OrderedDict
		#from collections import Counter

		res_tokens = []
		freq_dict = {}
		translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

		outStr = inStr.replace("'","")
		outStr = outStr.translate(translator).lower()
		tempStr = outStr.split()
		#tempStr = [w for w in tempStr if not w in stop_words]

		#tempStr = [stemmer.stem(plural) for plural in tempStr]


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

	def write_dict (self, index_dict):
		with open(self.outFile, 'w') as fout:
			for key in index_dict:
				fout.write(key + ': ')
				fout.write(str(index_dict[key]))
				fout.write('\n') 

import argparse

def main():
	parser = argparse.ArgumentParser(description='Main program for indexing documents.')
	parser.add_argument('-i', '--input_file', type=str, help='Name of the input document')
	parser.add_argument('-o', '--output_file', type=str, help='Name of output file for the index table')
	args = parser.parse_args()

	tester = file_processor(args.input_file, '0/6', args.output_file)
	title, body = tester.split_body_title()
	tokens = tester.tokenizer(body)
	index_dict = tester.aggregate_pos_list(tokens)
	tester.write_dict(index_dict)

	#print tokens
	#print tester.computeWordFrequencies(tokens)

	#print tester.aggregate_pos_list(tokens)

if __name__ == "__main__":
    main()



