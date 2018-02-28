import os
from file_processor import file_processor


class dir_processor:

	def __init__ (self, inDir, outFile):
		self.inDir = inDir
		self.inDir_inverted_index = {}
		self.dirID = self.inDir.split('/')[-2]
		self.outFile = outFile

	def dir_walker (self):
		for root, dirs, files in os.walk(self.inDir):
			fileList = files
		for file in fileList:
			docID = ('/').join([self.dirID, file])
			fileProcessor = file_processor(root + file, docID)
			title, body = fileProcessor.split_body_title()
			tokens = fileProcessor.tokenizer(body)
			#self.inDir_inverted_index.update
			doc_dict = fileProcessor.aggregate_pos_list(tokens)
			for term in doc_dict:
				if term not in self.inDir_inverted_index:
					self.inDir_inverted_index[term] = doc_dict[term]
				else:
					self.inDir_inverted_index.update(doc_dict[term]) 



		return self.inDir_inverted_index


	def write_to_file (self, index_dict):
		with open(self.outFile, 'w') as fout:
			for key in index_dict:
				fout.write(key + ': ')
				fout.write(str(index_dict[key]))
				fout.write('\n') 






import argparse
def main():
	parser = argparse.ArgumentParser(description='Main program for indexing documents.')
	parser.add_argument('-i', '--input_dir', type=str, help='Name of the input directory')
	parser.add_argument('-o', '--output_file', type=str, help='Name of output file for the index table')
	args = parser.parse_args()

	dirProcessor = dir_processor(args.input_dir, args.output_file)
	index_dict = dirProcessor.dir_walker()
	dirProcessor.write_to_file(index_dict)


if __name__ == "__main__":
    main()