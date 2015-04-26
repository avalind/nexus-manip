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
				coords[0].translate(None, ''.join(",")), \
				coords[1].translate(None, ''.join(",")))

		
	column_name = "Chromosome Region"
	location_parts = df[column_name].apply(lambda x: pd.Series(split_location_string(x)))
	location_parts.columns = ['Chromosome', 'Start', 'Stop']

	df['Chromosome'] = location_parts['Chromosome']
	df['Start'] = location_parts['Start']
	df['Stop'] = location_parts['Stop']

	return df

def split_by_sample(dataset):
	per_sample = dataset.groupby(['Sample'])
	return per_sample

def to_simple_bed(dataset, filehandle):
	"""
		writes a .bed file to filehandle
		containing the segments present in dataset.
	"""
	def to_bedrow(r):
		return r['Chromosome']+"\t"+ \
			   r['Start']+"\t"+ \
			   r['Stop']+"\t"+ \
			   r['Event']

	for index, row in dataset.iterrows():
		filehandle.write(to_bedrow(row)+"\n")

def to_gff(dataset):
	""" 
		Generates a gff file containing all columns
		present in dataset.
	"""
	pass

def main():
	dataset = load(sys.argv[1])
	dataset = separate_location(dataset)
	to_simple_bed(dataset, sys.stdout)

	
if __name__ == "__main__":
	main()
