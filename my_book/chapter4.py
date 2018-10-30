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



#p54页练习
#使用一个for循环打印数字1~20
for t in range(1,21):
    print(t)

#创建一个列表包含1~20中的奇数
s=[]
for r in range(1,21,2):
    s.append(r)
print(s)

#创建一个列表,包含3~30中能被3整除的数字
s1 = []
for d in range(3,31,3):
    s1.append(d)
print(s1)

#创建一个列表,包含1~10的三次方
s2 = []
for e in range(1,11):
    s2.append(e**3)
print(s2)

#使用列表解析生成一个列表,其中包含前15个数字的立方
s3 = [v**3 for v in range(1,16)]
print(s3)


#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])   #打印出前三名队员
print(players[1:4])    #打印出第2~4名队员
print(players[:2])     #如果没有指定第一个索引,默认从列表开头开始
print(players[2:])     #不指定终止索引,默认终止于末尾
print(players[-2:])    #无论列表多长,取出末尾的2个元素

#遍历切片-如果要遍历列表的部分元素,可在for循环中使用切片
#遍历前三名队员,并打印他们的名字
for p in players[0:3]:
    print(p.title())

#复制列表
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]
print("My friend's favorite foods are :")
print(friend_food)
