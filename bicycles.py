#2019/3/22 
'''简单的列表表示，一个列表包含几种自行车'''
bicycles = ['trek','cannondale','redline','specialized']
# print(bicycles)

'''从列表bicycles中提取第一款自行车： '''
#print(bicycles[0])

'''使用方法title()让元素格式更整洁： '''
#print(bicycles[0].title())

'''索引从0开始而不是1
	访问第二个元素和第四个元素'''
# print(bicycles[1])
# print(bicycles[3])
'''访问最后一个元素，索引为-1'''
# print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title()
print(message)

