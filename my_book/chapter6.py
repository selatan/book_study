#!/usr/bin/python
# -*- coding: UTF-8 -*-

#字典


#一个简单的字典
alien_0 = {'color':'green','point':5}
print(alien_0['color'])
print(alien_0['point'])


#使用字典
#在Python中字典是一些列键-值对，每个键都与一个值相关联。可以使用键来访问与之关联的值
#在Python中字典使用花括号中的一些列键-值对表示，键和值之间用冒号分离。


#访问字典中的值
alien_1 = {'color':'green','point':7}
new_points = alien_1['point']
print("Your just earned " +str(new_points)+" points!")           #str(new_points)将整数转换为字符串

#添加键值对,字典是一种动态结构，可以随时在其中添加键值对。python不关心排列顺序，值关系键与值之间的关联关系
alien_1['x_poition'] = 0
alien_1['y_positon'] = 49
print(alien_1)

#创建空字典,再添加键值对
alien_2 ={}
alien_2 ={'color':'yello','point':8}
print(alien_2)

#修改字典中的值
alien_2['color'] = 'blue'
print(alien_2)

alien_3 = {'x':0,'y':25,'speed':'medium'}
print('Original x: '+str(alien_3['x']))
if alien_3['speed']=='slow':
    x_increment=1
elif alien_3['speed']=='medium':
    x_increment =2
else:
    x_increment =3
alien_3['x']=alien_3['x']+x_increment
print('New x :'+ str(alien_3['x']))


#删除键值对
#使用del语句删除键值对，必须指定字典名和要删除的键
alien_4 = {'color':'green','point':5}
print(alien_4)
del alien_4['point']
print(alien_4)


#p87
#6-1
friends = {
    'first_name':'zhang',
    'last_name':'zan',
    'age':1,
    'city':'chengdu',
}
print(friends['first_name'])
print(friends['last_name'])
print(friends['age'])
print(friends['city'])

#6-2
favorite_nums = {
    'Amy':88,
    'Tom':25,
    'Lily':99,
    'Join':100,
    'Bob':1,
}
print("Amy like number : "+str(favorite_nums['Amy'])+'.')
print("Tom like number : "+str(favorite_nums['Tom']))
print("Join like number :"+str(favorite_nums['Join']))

#遍历字典
user_0 ={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi,'
}
for k ,v in user_0.items():         #items（）方法，以列表形式返回可遍历的(键, 值) 元组数组
    print("\nkey :"+k)
    print('value :'+v)


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_languages.items():
    print('\n'+name.title() + "'s favorite language is :"+language.title()+'.')

#python中字典函数values（）、kesys（）、items（）的用法与区别
dict = {
    'name':'HLJ',
    'age':30,
    'weight':55,
    'high':158
}
print(dict.keys())
print(dict.values())
print(dict.items())

#遍历字典中的所有键  keys（）——遍历字典中所有键，并以列表方式返回
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for people_name in favorite_languages.keys():
    print(people_name.title())            #title()方法将每个字符串的首字母变为大写字母

for people_name in favorite_languages:    #输出结果与上面的for循环一样
    print(people_name.title())


#按条件遍历
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
friend = ['phil','sarah']
for people_name in favorite_languages.keys():
    print(people_name.title())
    if people_name in friend:
        print("Hi "+people_name.title() + " ,I see you favorite language is :"+favorite_languages[people_name]+'.')

if 'mhuang' not in favorite_languages.keys():    #判断“mhuang”是否在字典的key中
    print("mhuang , please take our poll!")

#按顺序遍历字典中的所有键
