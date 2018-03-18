# tested for windows 10
import os
import subprocess
dir = "<your path to data-set folder>"
cmd = "apktool d "
root, dirs, files = os.walk(dir).__next__()
print(files)
for file in files:
	temp = cmd
	temp += file
	subprocess.call(temp, shell=True) 
	
