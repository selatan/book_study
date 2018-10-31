#!/usr/bin/python
# -*- coding: UTF-8 -*-

#if 语句

cars = ['audi','bmw','toyota','fort']
for car in cars:
    if car =='bmw':
        print(car.upper())     # 'bmw'以大写字母展示
    else:
        print(car.title())       #首字母以大写字母展示

#检查特定值是否包含在列表中
cars = ['audi','bmw','toyota','fort']
if 'benz' in cars:
    print("benz in cars")
else:
    print("benz is not in cars")

if 'bmw' not in cars:
    print('bmw is not in cars')
else:
    print('bmw in cars')


#if~elif~else---------4岁以下免费，4~18岁收费5美元，18岁（含）以上收费10美元
age = 12
if age <4:
    print('Yout admissionh cost is $0')
elif age <18:
    print('Your admission cost is $5')          #可以使用多个elif语句
else:
    print('Your admission cost is $10')


#使用多个elif代码块  ------4岁以下免费，4~18岁收费5美元，18岁（含）以上收费10美元，65岁以上收费5美元
age = 12
if age < 4:
    print('Yout admissionh cost is $0')
elif age < 18:
    print('Your admission cost is $5')
elif age <65:
    print('Your admission cost is $10')
else:
    print('You admission cost is $5')


