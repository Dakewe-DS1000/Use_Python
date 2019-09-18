#coding:utf-8
# 简明Python
# 高级的Python用法

##Print格式化输出
###输出一个字符，即使是数字，也会换成ASCII码进行输出
print("%c" % "A")
print("%c" % 65)
###格式化字符串
print("%s" % "Hello World")
print("%#d" % 10)
####格式化八进制
print("%#o" % 10)
####格式化十六进制
print("%#x" % 10)
print("%#X" % 10)
####格式化浮点数
print("%f" % 3.14)
print("%3.5f" % 3.1)
####格式化右对齐输出
print("%10.6f" % 3.1234)
####格式化做对齐输出
print("%-10.6f" % 3.1234)
####格式化科学计数法输出
print("%e" % 3140000)
####格式化自动输出数值显示方法
print("%g" % 31400000000)
####用*从后面的元组中读取字段宽度或精度
pi = 3.1415926
#- 以下代码是小数点后面保留5位的有效长度
print("pi = %.*f" % (5, pi))

###放置多个%，用来在一行内输出多个变量的值
str1 = "abc"
var1 = 15
print("The 1st word is %s and 2nd is %d" % (str1, var1))
###使用字典来对应填充
dict1 = dict(fruit_name = "orange", weight = 1.5, size = 15)
print("i like %(fruit_name)s and can eat %(weight)-8.2f, the size = %(size)d" % dict1)

##数据类型转化
#- 数据类型的转换，只需要将数据类型作为函数名使用即可，这些函数返回一个新的对象，表示转换的值
x = "6"
y = int(x)
print(x, type(x))
print(y, type(y))

x = 6.5
y = int(x)
print(x, type(x))
print(y, type(y))

x = "6.5"
y = float(x)
print(x, type(x))
print(y, type(y))
####将一个字符转换为相应的ASCII码值
print(ord("A"))
####将一个数值转化为ASCII码值并输出相应的字符
print(chr(65))

####超强的表达式计算
x = 8
calc = "5 * x + 9"
print(eval(calc))

#Python的流程控制
###三种基本结构：顺序、条件、循环
##条件语句
###if 条件表达式: 语句块
print("请输入体重(kg) : ")
#weight = float(input())
weight = 90
if weight>90:
    print("胖子，你该减肥了")
###if 条件表达式:
###     语句块1
###else:
###     语句块2
print("请输入体重(kg) : ")
#weight = float(input())
weight = 90
if weight > 90:
    print("胖子，你该减肥了")
else:
    print("小样，身材保持的不错")
###if 条件表达式1:
###     语句块1
###elif 条件表达式2:
###     语句块2
###else:
###     语句块3
print("请输入体重(kg) : ")
#weight = float(input())
weight = 90
print("请输入身高(m) : ")
#height = float(input())
height = 1.8
BMI = weight / height **2
if BMI < 20:
    print("你的BMI指数是%.2, 太轻了哦" %BMI)
elif BMI > 25:
    print("你的BMI指数是%.2f, 太重了哦" %BMI)
else:
    print("你的BMI指数是%.2f, 非常正常, 请保持!" %BMI)

##循环语句
###While循环
###While 条件表达式: 语句块
####统计6出现在2的100次方中出现的次数
num = 2 ** 100
print(num)

count = 0

while num > 0:
    if num % 10 == 6:
        count = count + 1
    num //= 10
print(count)

###For循环
###for 循环变量 in 序列:
###     语句块
####统计6出现在2的100次方中出现的次数
num = 2 ** 100
print(num)
count = 0
for digit in str(num):
    if digit == "6":
        count += 1
print(count)

####输出从1到10的整数
for i in range(1, 10):
    print(i)
####输出从0到10的整数
for i in range(10):
    print(i)
####以2为步进，输出从0到10的整数
for i in range(0, 10, 2):
    print(i)

###列表推导式
list1 = [1, 2, 3]
list2 = [3, 4, 5]
print([x * y for x in list1 for y in list2])
for x in list1:
    for y in list2:
        print(x * y)
print([x for x in list1 if 4>x>1])

##循环嵌套
for i in range(1, 10):
    for j in range(1, i+1):
        result = j * i
        print("%s x %s = %-5s" % (i, j, result), end=" ")
    print()

##break语句
###如果在嵌套循环中，break语句将停止执行本层的循环
####字符9出现在num数据列中的位置
num = 2 ** 100
pos = 0
for digit in str(num):
    pos += 1
    if digit == "9":
        break
print("2**100 is %d \nthe first position of 9 is Pos. %d" % (num, pos))

##continue语句
###跳过当前循环的剩余语句，然后继续进行下一轮循环
num = 2 ** 100
without9 = ""
for digit in str(num):
    if digit == "9":
        continue
    without9 += digit
print("2**100 is : %d \nwtihout 9 is : %s" % (num, int(without9)))

##pass语句
###空语句，是为了保持程序结构的完整性，一般用作占位语句
num = 2 ** 100
without9 = ""
for digit in str(num):
    if digit == "9":
        pass
    else:
        without9 += digit
print("2**100 is : %d \nwtihout 9 is : %s" % (num, int(without9)))

##函数
####def function_name(parameters):
####    function_suite
####    return [expression]
def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
pass
res = fact(10)
print(res)

def fun_example(listp, intp = 0, stringp = "A Default String"):
    listp.append("A new item")
    intp += 1
    return listp, intp, stringp
pass
fun_example.__doc__
my_list = [1, 2, 3]
a, b, c = fun_example(my_list)
print(a, b, c)

##全局变量和局部变量
