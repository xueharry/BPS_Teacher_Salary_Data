# Script to clean BPS salary data found in 'raw.csv'
# Narrows data down to teachers within 27 BPS high schools only and removes dollar signs from data

import csv, re

# Set containing the names of 27 BPS high schools as they are listed in 'raw.csv'
# (see the readme for further details on how I define 'high school')
# Note: Two high schools, Dearborn and Henderson are not included because raw.csv does not distinguish which of the teachers at
# these schools teach at the high school level.
hs = set(['BPS Another Course To Colleg','BPS Boston Arts Academy','BPS Boston Comm Leadership Ac', 'BPS Boston International HS', 
		'BPS Boston Latin', 'BPS Brighton High', 'BPS Burke High', 'BPS Charlestown High',
		'BPS Community Academy', 'Dorchester Academy', 'BPS East Boston High', 'BPS English High',
		'BPS South Boston HS - Excel', 'BPS Fenway High', 'Kennedy, EM Health Academy', 'Lyon Pilot High 9-12',
		'BPS Madison Park High', 'Margarita Muniz Academy', 'BPS New Mission Pilot', 'BPS Snowden International Hi',
		'Quincy Upper School', 'WREC: Urban Science Academy', 'West Roxbury Academy', 'Green Academy',
		'Tech Boston Academy', 'BPS Latin Academy', "BPS O'Bryant School"

	])

with open('raw.csv', 'rb') as inp, open('BPShighschool.csv', 'wb') as out:
	writer = csv.writer(out)
	for row in csv.reader(inp):
		new_row = []
		# Only write the header row and employees with the title "Teacher" (ignoring substitute teachers etc.)
		if row[1] == 'TITLE' or (row[1] == "Teacher" and row[2] in hs):
			# Remove dollar signs
			for val in row:
				val = re.sub('\$', '', val)
				new_row.append(val)					
			writer.writerow(new_row)