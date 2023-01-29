#Chapter 1 Strings/Arrays:

#counting simular elements in string

def count_str(str):
	counts=[]
	tmp=str[0]
	length=len(str)
	for i in range(1,length):
		if str[i] in tmp:
			tmp += str[i]
			continue
		counts.append(len(tmp))
		tmp=str[i]
	counts.append(len(tmp))
	return counts


def str_dict(str):
	counts={}
	for item in str:
		if item in counts:
			counts[item] += 1
		else:
			counts[item] = 1
	return counts


def str_edit(str1, str2):
	if abs(len(str1)-len(str2)) > 2:
		return False 
	else:
		j=k=counter=0
		for i in range(max(len(str1),len(str2))):
			if str1(j) == str2(k):
				continue
			else: str1

def common_str(str1,str2):
	common_str_helper()

def common_str_helper(j=0,i=0):
	if i>len(str1) or j>len(str2):
		return 0
	if str1[i] == str2[j]:
		return 1+common_str_helper(i+1,j+1)
	else:
		return max(common_str_helper(i,j+1),common_str_helper(i+1,j))



