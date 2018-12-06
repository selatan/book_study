#!/usr/bin/python
# -*- coding: UTF-8 -*-

#函数


#定义一个简单的函数
def greet_user():   #定义一个函数
    print("Hello!")         #函数体
greet_user()    #调用该函数

#向函数传递参数
def greet_user(username):       #username是形参
    print("Hello, "+username+".")
greet_user('HuangLJ')          #HuangLJ是实参

#8-1
def display_message():
    print("本章所学习的是函数相关的知识。")
display_message()

#8-2
def favorite_book(title):
    print("One of my favorite book is "+ title+' .')
favorite_book('Python')


#位置实参-调用函数时，Python将函数调用中的每个实参都关联到函数定义中的一个形参，这种关联方式成为位置实参
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+'.')
    print('My '+animal_type +"'s name is "+pet_name+'.')
describe_pet('cat','Batu')

#关键字实参-关键字实参是传递给函数的名称-值对，直接在实参中将名称和值关联起来，因此向函数传递实参时不会混淆
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+'.')
    print('My '+animal_type +"'s name is "+pet_name+'.')
describe_pet(animal_type='dog',pet_name='Willion')

#默认值-定义函数时，给每个形参指定默认值。在调用函数时若给形参提供了实参，Python将使用指定的实参，否则，将使用形参的默认值
#在给形参指定默认值后，可在调用函数时省略相应的实参
#定义函数时，带有默认值的形参，需要放在没有默认值的形参后面
def describe_pet(pet_name,animal_type='pig'):
    print("\nI have a "+animal_type+'.')
    print('My '+animal_type +"'s name is "+pet_name+'.')
describe_pet(pet_name='Peiqi')  #不传animal_type,使用默认值
describe_pet('Joni','rabbit')  #传递animal_type，使用实参值

#8-3
def make_shirt(size,message):
    print("\nThis T-shirt's size is: "+size+",and message is: "+message+'.')
make_shirt('155','Monday')
make_shirt(message='Tuesday',size='175')

#8-4
def make_shirt(size,message='I love Python'):
    print("\nThis T-shirt's size is: "+size+",and message is: "+message+'.')
make_shirt('L')
make_shirt('M')
make_shirt('L',message='Sunday')

#8-5
def describe_city(city,country='China'):
    print("\n"+city+" is in "+country+'.')
describe_city('BeiJing')
describe_city('Tokyo',country='Japan')
describe_city(country='America',city='Los Angeles')


#返回值
def get_formatted_name(first_name,last_name):
    full_name =first_name +' '+last_name
    return full_name.title()
musician = get_formatted_name('zhang','zan')   #将get_formatted_name()函数的返回值存储在变量musician中
print(musician)


#让实参变成可选的
#假设需要提供中间名，但不是所有人都有中间名，让中间的参数变成可选的，可以给实参middle_name指定一个默认值-空字符串
def get_name(first_name,last_name,middle_name=''):         #python将非空字符串解读为True，此时middle_name默认是False
    if middle_name:            #如果middle_name非空，为true
        full_name = first_name+' '+middle_name+' '+last_name
    else:                      #middle_name为false时
        full_name =first_name+' '+last_name
    return full_name.title()
name1 = get_name('zhang','zan')   #没有中间名
print(name1)
name2 = get_name('huang','juan','li')         #有中间名
print(name2)


#返回字典-函数可以返回任何类型的值，包括列表和字典等较复杂的数据结构
def build_person(first_name,last_name):
    person ={'first':first_name,'last':last_name}
    return person
name3 = build_person('zhang','zan')
print(name3)


#返回字典-参数中带有可变参数
def build_people(first_name,last_name,age =''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
name4 = build_people('huang','jie')
print(name4)
name5 = build_people('zhang','zan',2)
print(name5)


# #结合while循环-请用户输入姓和名，并打印出问候语
# def get_full_name(first_name,last_name):
#     full_name =first_name +' '+last_name
#     return full_name.title()
# while True:
#     print("\nTell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name : ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name : ")
#     if l_name =='q':
#         break
#     name6 = get_full_name(f_name,l_name)
#     print("\nHello,"+name6+"!")


# #8-6
# def city_country(city_name,country):
#     city_info = '"'+city_name+","+country+'"'
#     return city_info
# city1 = city_country('Beijing','China')
# print(city1)
#
# #8-7
# def make_album(singer_name,song_name,songs_num=''):
#     album = {'singer':singer_name,'song':song_name}
#     if songs_num:
#         album['num']=songs_num
#     return album
# album1 = make_album("ESON","L.O.V.E")
# print(album1)
# album2 = make_album("JONGHYUN",'SO GOODBY')
# print(album2)
# album3 = make_album('JAY','J III(EP',6)
# print(album3)

# #8-8
# def make_album(singer_name,album_name):
#     album = {'singer':singer_name,'song':album_name}
#     return album
# while True:
#     s_name = input("Please input songer name : ")
#     print("(enter 'q' at any time to quit)")
#     if s_name =='q':
#         break
#     a_name = input("Please input album name : ")
#     if a_name=='q':
#         break
#     info = make_album(s_name,a_name)
#     print(info)


# #传递列表
# #假设有一个用户列表，我们要问候其中的每位用户
# def greet_users(names):
#     for name in names:
#         msg = "Hello, "+name+"!"
#         print(msg)
# usernames = ['Ada','Bob','Emma']
# greet_users(usernames)

#在函数中修改列表
#查看p127-128


# #8-9
# def show_magicians(names):
#     for name in names:
#         print("Hi "+name+"!")
# magician_names = ['Maryy','Ella','Allen','Helln']
# show_magicians(magician_names)

#8-10
def show_magicians(name1s):
    for name in name1s:
        print("Hi "+name+"!")
def make_great(name2s,completed_name1s):
    while name2s:
        current_name = name2s.pop()
        completed_name1s.append(current_name+", The great")
names =["hehe",'haha']
completed_name2s = []
make_great(names,completed_name2s)
show_magicians(completed_name2s)

#8-11-后面有时间研究

#传递任意数量的实参
def make_pizza1(*toppings):    #星号让Python创建一个名为toppings的空元组，并将收到的所有值都装到这个元组中
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)
make_pizza1('pepperoni')
make_pizza1('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量实参   -Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中（即先放确定的，再放不确定的）
def make_pizza2(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza2(16,'pepperoni')
make_pizza2(12,'mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参、
#你知道你将收到有关用户的信息，但不确定是什么样的信息，在下面的实例中，函数接受用户的姓名，同时还接受任意数量的关键字实参
def build_profile(name,**user_info):
    profile={}
    profile['user_name']=name
    for key,value in user_info.items():        #遍历user_info字典的键值对
        profile[key]=value           #将user_info的键值对加入profile字典中
    return profile
user_profile = build_profile('HuangLJ',age =31,location='chengdu')
print(user_profile)


#8-12
def make_pizza3(*toppings):
    print("\nThis is your pizza's toppings:")
    for topping in toppings:
        print("-- "+topping)
make_pizza3('miki','beer','mushrooms')


#8-14
def car_profile(manufacturer,model,**car_info):
    profile={}
    profile['manufacturer']=manufacturer
    profile['model']=model
    for key,value in car_info.items():
        profile[key]=value
    return profile
car = car_profile('subaru','outback',color='blue',tow_package=True)
print(car)


#将函数存储在模块中
#有两个py文件A.py,B.py
#B.py中# 导入整个模块：import A；B.py中调用A.py中的函数时：A.function_A()
#B.py中# 导入特定的函数:from A import function_A；B.py中调用A.py中的函数时:function_A()
#使用as给函数指定别名
#B.py中# 导入特定的函数:from A import function_A as f_A，B.py中调用时：f_A()
#使用as给模块指定别名
#B.py中# 导入模块A:import A as AA，B.py中调用A.py中的函数时：AA.funcitin_A()
#导入模块中的所有函数
#B.py中# 导入模块A中的所有函数：from A import *  ；B.py中调用A.py中的函数时：function_A()






