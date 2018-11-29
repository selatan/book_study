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


