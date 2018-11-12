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