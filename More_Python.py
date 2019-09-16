#coding:utf-8
# 简明Python
# 进阶的Python用法

##字符串
var1 = "Use Python"
var2 = 'Life is Hard'
print(var1, type(var1))
print(var2, type(var2))

###如何输出: He said "Hello"
#- 转义字符是"\"
var1 = "He said \"Hello\""
print(var1, type(var1))
#- 另外一种书写形式：单引号与双引号的混合使用
var1 = 'He said "Hello"'
print(var1, type(var1))
#- 如果你不想让反斜杠发生转义，可以在字符串前面添加一个"r"，表示原始字符串
var1 = r"This is a \"String\""
print(var1)

###如何输出多行的大段文字
print("1st line\n2nd line\n3rd line\n4th line\n")
####如果按照以上写法，非常麻烦
var1 = """1st line
2nd line
3rd line
4th line"""
print(var1)

###字符串的运算
var1 = "Hello" + "World"
print(var1)
var1 = "Hello" * 20
print(var1)
#- 不支持以下写法
#var1 = "5" + 4
#print(var1)

##列表
list1 = [1, 2, 3, 4, 5]
print(list1)
list1 = [1, 2, 3, "Hello", "World", [5, 6, 7, 8]]
print(list1)
for i in range(6):
    print(i, " : ", list1[i])
#- 注意：以下代码的输出不包含第三个数据
print(list1[0:3])
###以2步长为间隔，输出列表数据
print(list1[::2])

list2 = [1, 2, 3, "Hello", "World", [5, 6, 7, 8]]
print(list2[-1][1:])

###字符串可以被看作特殊的列表
str1 = "Hello, World"
print(str1[2:5])
print(str1[-1])

##元组
###元组是只读的：
###元组中的元素一旦被定义，就不能修改操作
#### -1 表示元组中最后一个数据
tuple1 = (1, 2, 3, 4, 5, 6, "Hello Python", [7, 8, 9, 0])
print(tuple1, type(tuple1))
print(tuple1[0])
print(tuple1[-1])
print(tuple1[6:-1])
print(tuple1[-1][-1])

#### 元组与列表的区别是：元组是()，列表是[]

##集合
###集合是一个无序、且不含重复元素的序列，集合主要用来进行成员关系测试和删除重复元素
###使用大括号{}或者set()函数，创造集合
set1 = {1, 3, 5, 5, 3, 1}
print(set1)
print(5 in set1)
print(8 in set1)

###集合的逻辑操作
set1 = {1, 2, 3}
set2 = {2, 4, 5}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

##字典
dict1 = {"name":"google", "height":176, "weight":72}
print(dict1["height"])
dict1["height"] = 77
print(dict1["height"])
####其他字典的写法
dict2 = dict([("name", "google"), ("height", 176)])
print(dict2)
dict3 = dict(name="google", weight=72)
print(dict3)
####字典中的一些内置函数
print(dict2.keys())
print(dict2.values())
dict2.clear()
print(dict2)