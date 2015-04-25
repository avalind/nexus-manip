#!/usr/bin/env python
import sys
import pandas as pd

def load(filename):
	"""
		Loads the exported table from Nexus CNV 7.5 stored in filename
		into a Pandas DataFrame.
	"""
	df = pd.read_table(filename, sep="\t")
	return df

def separate_location(df):
	"""
		Nexus exports the location of the CNV as a UCSC/Ensembl "coordinate string",
		we split them up and add separate columns for chromosome and start and end for
		each segment.
	"""
	def split_location_string(loc):
		parts = loc.split(":")
		coords = parts[1].split("-")

		return (parts[0], \
				int(coords[0].replace(",","")), \
				int(coords[1].replcae(",","")))

		
	column_name = "Chromosome Region"

	

def main():
	print load(sys.argv[1])

if __name__ == "__main__":
	main()
