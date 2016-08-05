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
			output.write(ok)
			#print(ok)

os.remove(filename)

[os.rename(f, f.replace("_clean", "")) for f in os.listdir(".") if not f.startswith('.')]