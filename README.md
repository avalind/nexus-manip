# nexus-manip

(Mostly for myself since I tend to export a lot of data segmented in Biodiscoverys
software for downstream analysis in bedtools)

Lets you convert exported tables from Biodiscovery Nexus Copy Number software
to some more useful file formats (.bed and .gff) for downstream processing.

For instance, if table.txt contains segments from three Samples (S1, S2 and S3):

	base.py table.txt

will generate a .bed-file each for the samples with segment size and the type of
abberation.
