import string
import sys
import os
import glob


filename = sys.argv[1]
outfile = filename.split('.')[0] + '_clean' + '.csv'

with open(filename,'r+') as input:
	with open(outfile, 'wb') as output:
		for line in input:
			ok = line.replace("\"", "")
			ok = ok.split(',')
			out = ''
			for x in range(0,6):
				out+=ok[x]
				if x is not 5:
					out+=','
				else:
					out+='\n'
			output.write(out)
			#print(out)

os.remove(filename)

[os.rename(f, f.replace("_clean", "")) for f in os.listdir(".") if not f.startswith('.')]