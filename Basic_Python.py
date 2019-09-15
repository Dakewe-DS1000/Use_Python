#coding:utf-8

# 简明Python
# 简单的Python用法

#Print函数的用法
#Python中，Print的默认输出是换行的
print("Hello, World")
print("This is Python")

#以下代码在Python3中使用
#在Print函数中使用“end”，表示这个输出不换行
print("Hello", end=' ')
print("You")

#以下代码仍然会输出文字在同一行
print("Hello", "World")

#变量
#每个变量在内存中创建，都包括变量的标识，名称和数据这些信息
#每个变量在使用前都必须赋值，赋值号是“=”
#Python在定义变量的时候，是不需要声明变量类型的
#小技巧：按shift+Enter，执行当前行并在终端输出结果
int_a = 5
float_b = 6.3
str_c = "hello"
print(int_a, float_b, str_c)
print(int_a, type(int_a))
print(float_b, type(float_b))
print(str_c, type(str_c))

#标识符
#在Python里，标识符由字母、数字、下划线组成
#但是不能以数字开头
#Python中，大小写是敏感的，也就是大小写不同表示不同的变量
x_6 = 7 #这样写是可以的
###
#6_x = 8 #这样写是不可以的
###
X_6 = 8
#python中还支持中文的变量名，但是建议不要使用中文，因为这样做局限性会比较大，代码不会国际化
变量1 = 9
print(x_6, X_6, 变量1)

#Numbers(数字)的数据类型
#数字数据类型用于存储数值，默认十进制数据，还可以表示二进制，八进制和十六进制
#还支持科学计数法
#还支持复数complex
#整型的表示：
var1 = 0b10 # output : 2
var2 = 0o10 # output : 8
var3 = 0x10 # output : 16
print(var1, var2, var3)
#Python支持非常长的整数
var1 = 1234567890123456789012345678901234567890
print(var1, type(var1)) # 并不损失任何精确度
#浮点型的表示
var1 = 1e-5; var2 = 6.7e15; var3 = 6.7e16; var4 = -1.8
print(var1, var2, var3, var4)
print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))
#复数的表示
var1 = 3 + 5.3j
var2 = complex(3.4e5, 7.8)
print(var1, type(var1))
print(var2, type(var2))
#布尔类型
#bool : True and False
i_love_you = True
you_love_me = False
print(i_love_you, type(i_love_you))
print(you_love_me, type(you_love_me))

#Python中的注释
#当行注释使用“#”
#多行注释使用'''或者"""
print("这句可以被输出")
#print("这句可以被输出")
"""
这里被注释，不输出
print("这句可以被输出")
这里是多行注释的部分
"""
'''
这里被注释，不输出
print("这句可以被输出")
也可以这样写多行注释
'''

#Python中的基本运算
#算术运算
#+ - * / %(求模，也就是取余数) **(求幂) //(取整数)
a = 10 + 3.5
print(a, type(a)) #系统中直接默认的是将整型向浮点型转换
b = 10 - 3.5
print(b, type(b))
c = a * b
d = c / a
e = c // a
f = c % a
g = c ** a
print(c, d, e, f, g)
#结果符号和除数相同
c = -10 % 3 # output +
d = 10 % -3  # output -
print(c, d)
#幂运算
c = 10 ** 3
print(c)
c = 10 ** 3.0
print(c)

#Python中的比较运算
#==, !=(不等于), <>(不等于), >, <, >=, <=
print(10<3)
print(10>3)
print(10>=3)
print(10<=3)
print(1==1)
print(1!=1)
print(3==3.0)   #output : True
print(3.0==3)   #output : True
print(3=="3")   #output : False
print(10+3==13) #output : True，这里先做+的算术运算，再去做比较运算
print(13==10+3) #output : True
#在Python中算术运算的优先级比关系运算的优先级要高

#Python中的赋值运算
#=, +=, -=, *=, /=, %=, **=, //=
#赋值运算中的左边必须是一个变量
a = 10.1
b = 2.5
a += 3
b *= 2
print(a, b)
a //= b
print(a, b)
