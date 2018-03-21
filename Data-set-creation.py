file_1 = open("Andriod_324_permission.txt",'r')
file_2 = open("feature.txt",'r')
file_3 = open("Labeled_Data_Point.txt",'r')
file_4 = open("final_data_set.txt",'w')
list = file_1.read().strip().split()
list_2 = []
for temp in file_3:
	x = temp.strip().split(' ')
	list_2.append(x[0])
	list_2.append(x[1])

APK = " "
feat_list = []
# return label 
def Malware_Label(apk):
	ind = 0
	for ap in list_2:
		ind = ind+1
		if apk == ap:
			return list_2[ind]
	return "No Label"
# Mark 1 or 0 against each feature if exits or not
def Mark_0_OR_1(feat):
	check = True
	for per in list:
		for f in feat:
			if f == per:
				file_4.write('1')
				file_4.write(" ")
				check = False
				break
		if check:
			file_4.write('0')
			file_4.write(" ")
		check = True # for next iteration
	
def Create_Data_Set():
	for line in file_2:
		data = line.strip().split(' ')
		APK = data[0]
		data = data[1::]
		
		Mark_0_OR_1(data)
		Label = Malware_Label(APK)
		file_4.write(Label)
		file_4.write('\n')
Create_Data_Set()
file.close()
file_1.close()
file_2.close()
file_3.close()
file_4.close()
