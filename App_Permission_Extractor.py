import re
import os

dir = "C:\\Users\\<user-name>\Desktop\\Machine-learning\\project\\Data-set\\drebin\\drebin-0\\drebin-0"
change_to = "C:\\Users\\<use-name>\Desktop\\Machine-learning\\project\\Data-set\\drebin\\drebin-0\\drebin-0\\"

root, dirs, files = os.walk(dir).__next__()
out = open("App_uses_permission.txt",'w')
for folder in dirs:
	new_Dir = change_to+folder
	app_Hash_Key = folder.strip(".zip.out")
	out.write(app_Hash_Key)
	print(app_Hash_Key)
	try:
		file = open(new_Dir + "\\AndroidManifest.xml",'r',encoding="utf8") # utf8 because we had some chinese text in Manifest.XML
	except (FileNotFoundError,IOError):
		continue	
	pattern = re.compile('<uses-permission')
	line_list = []
	for line in file:
		return_True = pattern.search(line)
		if return_True:
			line_list.append(line)
			
	for line in line_list:
		feature_Word = line.strip().split(".",)
		feature_Word = feature_Word[len(feature_Word)-1].strip("\"/>")
		out.write(" ")
		out.write(feature_Word)
	out.write('\n')
		
