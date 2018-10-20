#!/usr/bin/python
# -*- coding: UTF-8 -*-

#操作列表


#遍历整个列表使用for循环
cars = ['bmw','audi','toyota','subaru','Fort','benz']
for car in cars:
    print(car)
    print(car.title() + ' is so expensive!')
print("It's cars, "+ str(cars))



#50页练习
books = ['java','python','PHP','C++']
for book in books:
    print("My son like "+ book +".")
    print("I like pepperoni pizza.")
print("I really like pizza.")

annimals = ['dog','rabbit','cat']
for animal in annimals:
    print(animal)
    print("A " +animal +" would make a great pet.")
print("The animals would make a great pet!")


#range()函数,生成一系列数字,它从第一个数值开始数,并在到达指定的第二个值后停止,因此下面这个循环输出的是1,2,3,4
for value in range(1,5):
    print(value)

#使用range()创建数字列表,可以使用函数list()将range()的结果直接转换为列表
number = list(range(1,6))
print(number)

#使用range()函数还可以指定步长,下面的代码打印1~10内的偶数
num = list(range(2,11,2))
print(num)

#创建一个列表,包含1~10的平方
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)      #也可直接写squares.append(value**2)
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))   #打印列表中最小值
print(max(digits))   #打印列表中最大值
print(sum(digits))   #打印列表所有值得和


#列表解析
#使用列表解析创建1~10的平方
squares1 = [value**2 for value in range(1,11)]
print(squares1)


#P54练习
#使用for（）循环打印1~20（包含）
s=[]
for i in range(1,21):
    s.append(i)
print(s)

#创建一个列表，包含1~20中的奇数，再将这些数字打印出来
s1 = [i for i in range(1,21,2) ]
print(s1)
for x in s1:
    print(x)

#创建一个列表，包含3~30中能被3整除的数字，再将这些数字打印出来
s2 = [m for m in range(3,31,3)]
print(s2)
for n in s2:
    print(n)

#创建一个列表，包含1~10的立方，再将这些数字打印出来
s3 = [v **3 for v in range(1,11)]
print(s3)
for y in s3:
    print(y)

#切片————指定要使用的第一个元素的索引和最后一个元素的索引+1（与range（）类似）
#打印出前三名队员
players = ['charls','martina','michael','florence','eli']
print(players[0:3])




