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
print(dict.keys())         #以列表的形式返回所有键
print(dict.values())       #以列表的形式返回所有值
print(dict.items())        #以列表的形式返回所有键值对

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
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in sorted(favorite_languages.keys()):                    #对方法favorite_languages.keys()的结果调用函数sorted（）
    print(name.title()+ ", thank you for taking the poll")


#遍历字典中所有值
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for language in favorite_languages.values():
    print(language.title())

#遍历字典中的所有值并去重
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for language in set(favorite_languages.values()):
    print(language.title()+'.')


#P92
#6-5
rivers = {
    'changjiang':'china',
    'henghe':'india',
    'nile':'egypt',
}
for river,country in rivers.items():
    print("The "+river.title() + " runs through "+ country.title())

for r in rivers.keys():
    print(r.title())

for c in rivers.values():
    print(c.title())

#6-6
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
names = ['bob','jen','tom']
for name in names:
    if name in favorite_languages.keys():
        print(name.title()+" , thank you for taking poll.")
    else:
        print(name.title() +" , please take our poll!")

#嵌套-字典中存储列表、列表中存储字典、字典中存储字典，都称为嵌套
#在列表中存储字典
alien_4 = {'color':'green','point':5}
alien_5 = {'color':'yellow','point':10}
alien_6 = {'color':'red','point':15}
aliens = [alien_4,alien_5,alien_6]
for alien in aliens:
    print(alien)

aliens = []   #创建一个用于存储外星人的空列表
for alien_num in range(30):            #创建30个绿色的外星人（循环30次）
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:    #显示出前5个外星人
    print(alien)

print("Total number of aliens: "+str(len(aliens)))   #显示创建了多少个外星人

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='mediu'
        alien['point']=10
for alien in aliens[0:5]:
    print(alien)


#在字典中存储列表
pizza ={
    'crust':'thick',
    'topping':['mushrooms','extra chees'],
}
print("You ordered a "+ pizza['crust']+"-curst pizza "+ "with the following toppings :")
for topping in pizza['topping']:
    print(topping)



favorite_languages={
    'jen':['python','c'],
    'sarah':['c'],
    'edward':['ruby','java'],
    'phil':['python'],
}
for name,languages in favorite_languages.items():
    print('\n'+name.title()+",s favorite language are :")
    for language in languages:
        print(language.title())

#在字典中存储字典
users ={
    'huanglj':{
        'age':25,
        'city':'shanghai',
        'weight':50,
    },
    'zhangfb':{
        'age':26,
        'city':'beijing',
        'weight':60,
    }
}
for username,user_info in users.items():
    print(username.title()+" is "+str(user_info['age']) + " years old .")
    print(username.title()+" is at "+user_info['city'])



#p99
#6-8    列表中存储字典
pet1 = {'name':'dog','admin':'tom'}
pet2 = {'name':'cat','admin':'join'}
pet3 = {'name':'panda','admin':'lucy'}
pets =[pet1,pet2,pet3]
for pet in pets:
    print(pet['name'].title()+ "'s admin is "+pet['admin'].title())

#6-9  字典中存储列表
favorite_places ={
    'huanglg':['beijing','japan','dali'],
    'zhangfb':['india','china'],
    'zhangz':['home']
    }
for name ,favorite_place in favorite_places.items():
    print(name.title() + " favorite places is : " )
    for place in favorite_place:
        print(place.title())

#6-11 字典中存储字典
cities ={
    'chengdu':{
        'country':'china',
        'population':5000,
        'fact':'panda',
    },
    'toyoko':{
        'country':'japan',
        'population':4002,
        'fact':'fushishan',
    },
    'beijing':{
        'coutry':'china',
        'population':8225,
        'fact':'The Great Wall',
    }
}

for city,info in cities.items():
    print(city + " is in "+info['country'])
    print(city.title()+ "'s popilation is "+str(info['population']) +'.')
