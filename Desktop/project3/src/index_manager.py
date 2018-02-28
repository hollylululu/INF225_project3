from __future__ import division
import argparse
import multiprocessing as mp
from math import ceil
import time



from file_processor import file_processor


class index_manager(object):
	def __init__ (self, numWorkers):
		self.numWorkers = numWorkers
		self.output_dir = None

	def distribute_task (self, inDir, outFile):
		if self.numWorkers == 1:
			inDir = [inDir]
		else:













def main():
	parser = argparse.ArgumentParser(description='Main program for indexing documents.')
	parser.add_argument('-i', '--input_dir', type=str, help='Name of the input document')
	parser.add_argument('-o', '--output_file', type=str, help='Name of output file for the index table')
	parser.add_argument('-n', '--numWorkers', type=int, help='How many splits of the document folders')
	args = parser.parse_args()


	start = time.time()
	idxManager = index_manager(numWorkers = args.numWorkers)
	idxManager.distribute_task(inDir = args.input_dir, outFile = args.output_file)
	end = time.time()
	print "Time to construct index in parallel: " + str(end - start) + 'seconds'



	tester = file_processor(args.input_file)
	body, title = tester.split_body_title()
	tokens = tester.tokenizer(body)
	print tester.computeWordFrequencies(tokens)

if __name__ == "__main__":
    main()