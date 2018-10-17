#!/usr/bin/python
# -*- coding: UTF-8 -*-

#列表简介
#列表是用方括号[] 来表示的有序集合
#打印、访问列表，添加、修改、删除列表中的值，升序、降序排列列表，




#列表
bicycles = ['ofo','mobike','CCbike','bluebike']

#打印列表
print(bicycles)

#访问列表元素
print(bicycles[0])   #第一个元素
print(bicycles[1])   #第二个元素
print(bicycles[3].title())   #第四个元素

print(bicycles[-1])   #访问最后一个（倒数第一个）元素
print(bicycles[-2])   #访问倒数第二个元素，以此类推

#使用列表中的值
message = "My first bicycle is " + bicycles[0].title()+'!'
print(message)

#修改列表元素
motocycles = ['honda','yamaha','suzuki']
print(motocycles)
motocycles[0] = 'beite'
print(motocycles)

#在列表末尾添加元素
motocycles.append('ducati')      #使用append()方法将元素“ducati”添加到列表末尾
print(motocycles)

#在列表中添加元素
motocycles.insert(1,'yadi')   #使用insert()方法将'yadi'添加到列表第二个位置，后面的元素依次后移一位
print(motocycles)

#从列表中删除元素
del motocycles[0]     #使用del语句删除列表中的元素
print(motocycles)

#pop()方法可以删除（弹出）列表中任意位置的元素，并接着使用它的值（如将他生成一个新的列表）
#例如列表中的书籍是按购买时间存储的，需要指出最后购买的是哪本书
book1 = ['JAVA','C++','PHP','Python']
print(book1)
last_owned = book1.pop()    #使用pop()方法删除（弹出）列表中最后一个元素
print(book1)
print(last_owned)
second_owned = book1.pop(1) #使用pop()方法删除（弹出）列表中第二个元素
print(second_owned)
print(book1)


#根据值删除列表中的元素（不需要知道值所处的位置）(如果该值在列表中出现多次，remove()只删除列表中第一个出现的指定值，使用循环可以删除所有的值）
book2 = ['JAVA','C++','PHP','Python']
book2.remove('PHP')       #使用remove()方法从列表中删除值’PHP‘
print(book2)
#使用remove()删除元素时使用该元素
too_hard = 'JAVA'
book2.remove(too_hard)
print(book2)
print(too_hard + " is so hard for me ! ")




#p38页练习
invite_name = ['Edison','Buffett','mayun','Bill Gates']
print("Would you like eat lunch with me "+str(invite_name)+ "?")

del_guest = invite_name.pop(1)   #'Buffett'无法赴宴
print(del_guest + " can't eat lunch with me.")
print(invite_name)
invite_name.insert(1,'wangjunkai')   #'wangjunkai'来赴宴
print("Would you like eat lunch with me "+str(invite_name) + '?')

print("I find a big table !!!!")
invite_name.insert(0,'zhaoliying')   #将’zhaoliying‘添加到邀请名单开头位置
print(invite_name)
invite_name.insert(2,'Newton')   #添加一个“Newton”到第三位
print(invite_name)
invite_name.append('Einstein')      #将'Einstein'添加到名单末尾
print(invite_name)

for i in invite_name:
    print("I want to invite " + i + " eat lunch with me.")

print("Sorry,only two person can eat lunch with me.")

del_guest1 = invite_name.pop()
print("Sorry," + del_guest1+",I can't invite you eat lunch with me.")
print(invite_name)
del_guest2 = invite_name.pop()
print("Sorry," + del_guest2+",I can't invite you eat lunch with me.")
print(invite_name)
del_guest3 = invite_name.pop()
print("Sorry," + del_guest3+",I can't invite you eat lunch with me.")
print(invite_name)
del_guest4 = invite_name.pop()
print("Sorry," + del_guest4+",I can't invite you eat lunch with me.")
print(invite_name)
del_guest5 = invite_name.pop()
print("Sorry," + del_guest5+",I can't invite you eat lunch with me.")
print(invite_name)

for i in invite_name:
    print("I always want to invite " + i + " eat lunch with me.")

del invite_name[1]
del invite_name[0]
print("最后的邀请名单为："+str((invite_name)))






#使用sort()方法对列表进行永久性排序(再也无法恢复到原来的排序）
cars1 = ['bmw','audi','toyota','subaru']   #元素全是小写字母
cars1.sort() #永久-默认升级排序
print(cars1)     #或直接写成print(cars.sorted())
cars1.sort(reverse=True)   #永久-将列表元素进行降序排列
print(cars1)

#使用sorted()函数对列表进行临时排序（不影响他们在列表中原始排列顺序）
cars2 = ['bmw','audi','toyota','subaru']
print(sorted(cars2))   #对列表进行临时性升级排序
print(cars2)          #原列表元素位置不变
print(sorted(cars2,reverse=True))    #对列表进行临时性降序排序

#注意：上面sort（）是方法method-类里面定义的叫方法，而sorted（）是函数function-类外面定义的是函数


#倒着打印列表（反转列表元素的排列顺序）使用方法reverse()
cars3 = ['bmw','audi','toyota','subaru','Fort']
cars3.reverse()
print(cars3)
#reserve()对列表进行永久性修改排列顺序，但再次调用resever()即可恢复原来的排列顺序



#使用函数len（）获取列表长度
cars4 = ['bmw','audi','toyota','subaru','Fort','benz']
print(len(cars4))




#p41练习
L = ['xinduqiao','dali','jiuzaigou','ouzhou','xinjiang']
print(L)
print(sorted(L))    #临时升序排列
print(L)
print(sorted(L,reverse=True))    #临时倒序排列
print(L)

L.reverse()   #对列表进行倒序排列
print(L)
L.reverse()   #再次对列表进行倒序（恢复原来的顺序）
print(L)

L.sort()  #对列表进行永久性升序排列
print(L)
L.sort(reverse=True)   #对列表进行永久性降序
print(L)

print(len(L))

print(L[4])



#————over——————
