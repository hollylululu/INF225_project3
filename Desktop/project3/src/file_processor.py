
class file_processor:

	def __init__ (self, filePath):
		self.term_freq = {}
		self.filePath = filePath
		self.title = ''
		self.body = ''


	def split_body_title (self):
		res_str = ''
		with open(self.filePath, 'rt') as fin:
			res_str = fin.read()
		split_list = res_str.split('<body>')
		self.title = split_list[0]
		self.body = split_list[1].replace('</body>', '')
		return self.title, self.body



	def tokenizer(self, str):
		import nltk
		import string
		from tokenize import tokenize
		res_tokens = []
		translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

		with open (self.filePath, 'r') as fin:
			for line in fin:
				line = line.replace("'","")
				line = line.translate(translator).lower()
				tokens = nltk.word_tokenize (line)
				res_tokens.extend(tokens)
		return res_tokens

	def computeWordFrequencies(self, tokens):
		import collections
		from collections import OrderedDict
		from collections import Counter
		return dict(collections.Counter(tokens))

import argparse

def main():
	parser = argparse.ArgumentParser(description='Main program for indexing documents.')
	parser.add_argument('-i', '--input_file', type=str, help='Name of the input document')
	parser.add_argument('-o', '--output_file', type=str, help='Name of output file for the index table')
	args = parser.parse_args()

	tester = file_processor(args.input_file)
	body, title = tester.split_body_title()
	tokens = tester.tokenizer(body)
	print tester.computeWordFrequencies(tokens)

if __name__ == "__main__":
    main()



