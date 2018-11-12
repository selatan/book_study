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
age = 3
if age < 4:
    print('Yout admissionh cost is $0')
elif age < 18:
    print('Your admission cost is $5')
elif age <65:
    print('Your admission cost is $10')
else:
    print('You admission cost is $5')

#省略else代码块——python并不要求if-elif结构后面必须有else代码块
age = 60
if age < 4:
    print('Yout admissionh cost is $0')
elif age < 18:
    print('Your admission cost is $5')
elif age <65:
    print('Your admission cost is $10')
elif age >=65:
    print('You admission cost is $5')


#p75页练习
#5-3
alien_color1 = 'yellow'
if alien_color1=='green':
    print("玩家获得5个点")

alien_color2 = 'green'
if alien_color2 =='green':
    print("玩家获得5个点")

#5-4
alien_color3 = 'yellow'
if alien_color3 =='green':
    print('玩家因射杀该外星人获得了5个点')
else:
    print('玩家获得了10个点')

#5-5
alien_color4 ='red'
if alien_color4=='green':
    print('玩家获得了5个点')
elif alien_color4 =='yellow':
    print('玩家获得了10个点')
else:
    print('玩家获得了15个点')

#5-6
age= 4
if age < 2:
    print('他是婴儿')
elif age <4:
    print('他正蹒跚学步')
elif age <13:
    print('他是儿童')
elif age <20:
    print('他是青少年')
elif age < 65:
    print('他是成年人')
else:
    print('他是老年人')

#5-7
fruit = ['apple','banana','watermelon']
if 'banana' in fruit:
    print("Your really like banana！")
if 'pear' in fruit:
    print('Your really like pear！')
if 'watermelon'in fruit:
    print('Your really like watermelon！')

#检查特殊元素
pens = ['铅笔','圆珠笔','钢笔','彩笔']
for pen in pens:
    if pen=='彩笔':
        print('彩笔用完了，要买了')
    else:
        print('这支笔还可以用:'+ pen)



#确定列表不是空的
requested_toppings=[]
if requested_toppings:           #列表不为空时返回true
    for requested_topping in requested_toppings:
        print("Adding"+requested_topping+".")
    print("\n Finished making your pizza!")
else:                            #列表为空时返回false
    print("Are you sure you want a plain pizza?")


#使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppingss = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppingss:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping+'.')
else:
    print("we don't have"+requested_topping+'.')
print("Finished making your pizza.")



#p79
#5-8
users=['ada','admin','lily','tom','yamy']
for user in users:
    if user =='admin':
        print("Hello "+user+','+"would you like to see a status reports?")
    else:
        print("Hello "+user+','+"thank you for logging in again.")

#5-9
users1=[]
if users1:
    for user in users1:
        if user == 'admin':
            print("-Hello " + user + ',' + "would you like to see a status reports?")
        else:
            print("-Hello " + user + ',' + "thank you for logging in again.")
else:
    print("We need to find some users")

#5-10
current_users=['Bob','amy','vivian','emma','aha']
new_users = ['amada','lucy','emma','bob','kiven']
for new_user in new_users:
    if new_user in current_users:
        print("用户名:"+new_user+" 已被占用，请输入其他的用户名")
    else:
        print("这个用户名:"+new_user+" 未被占用")

#怎么把一个列表中的所有元素转为大写

