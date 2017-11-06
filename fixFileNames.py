import sys
import os

directory = "./" if len(sys.argv) < 2 else sys.argv[1]
os.chdir(directory)

# helper to sort files by creation time
def sortFiles(directory):
    a = [s for s in os.listdir(directory)
         if os.path.isfile(os.path.join(directory, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(directory, s)))
    return a 

for index,filename in enumerate(sortFiles("./")):
	if filename.endswith(".pdf"): 
		# remove spaces in name
		noSpaces = filename.replace(" ","_")
		# adds file number if not already present
		withNumber = noSpaces if noSpaces[0].isdigit() else str(index+1) + "." + noSpaces
		os.rename(filename, withNumber)

