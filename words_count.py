#计算一个文件中每个英文单词出现的次数
filename = "test.txt"
with open(filename) as f_obj:
	lines = f_obj.readlines() 	#按行读
count = {}				
for line in lines:		
	tokens = line.strip().split(' ')	#去掉首位空格换行，再用空格分割
	for token in tokens:				#遍历tokens
		if token not in count:			#token键不在count字典里
			count[token] = 0			#将他的值设为0
		count[token] += 1				#count字典里 给token键-值+1

for word in count:						#遍历count字典，打印键值
	print(word,count[word])