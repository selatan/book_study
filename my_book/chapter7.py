#!/usr/bin/python
# -*- coding: UTF-8 -*-

#用户输入和while循环

# #input()函数  ——让程序暂停运行，等待用户输入一些文本，获取用户输入后，Python将起存储在一个变量中。
# #程序等待用户输入，并在用户按回车键后继续运行。
# message = input('Tell me something ,and I will repeat it back to you : ')
# print(message)
#
# name = input("Please enter your name :")
# print("Hello , "+name+ " !")
#
# prompt = "If you tell us who you are , we can personalize the message you see ."
# prompt += "\nWhat is you first name ? "
# name = input(prompt)
# print("Hello ,"+name)
#
# #使用int()来获取数值输入
# age = input("How old are you ?")        #使用函数input（），Python将用户输入默认解读为字符串
# print(age)         #此时age是个字符串
# age = int(age)     #将字符串age转换为数值
# print(age<10)      #两个int型的值进行比较


#求模运算符“%”，它将两个数相处并返回余数
# print(4%3)
# print(15%8)
# print(12%2)
#
# #输入一个数字并判断是奇数还是偶数
# num=input("Enter a number, and I'll tell you if it's even or odd:")
# num = int(num)
# if num%2 ==0:
#     print("\nThe number "+ str(num)+ " is even .")
# else:
#     print("\nThe number "+ str(num)+ " is odd .")

# #7-1
# car = input("What's car would you want ?")
# print("Let me see if I can find you a "+car+" .")

# #7-2
# num1 = input("How many people will eat lunch ?")
# num1 = int(num1)
# if num1>8:
#     print("Soryy, there is no desk .")
# else:
#     print("We have desks .")
#
# #7-3
# num2 = input("Please print a number: ")
# num2 = int(num2)
# if num2%10==0:
#     print(str(num2) +"是10的倍数。")
# else:
#     print(str(num2)+"不是10的倍数。")


# #while循环
# #让用户选择何时退出-定义一个值，只要用户输入的不是这个值，程序就接着运行、
# input1 = "\nTell me something ,and I'll repeat it back to you : "
# input1 +="\nEnter 'quit' to end the program."
# mesaage = ""
# while mesaage !='quit':
#     mesaage = input(input1)
#     print(mesaage)

#使用break退出循环，即终止整个循环
#使用continue继续下一次循环（停止本次循环）


#7-4
pizaa_peiliao = "请输入披萨配料 ："
while pizaa_peiliao !='quit':
    pizaa_peiliao = input(pizaa_peiliao)
    print("我们会在披萨中添加配料："+pizaa_peiliao)

#7-5
age ="Please tell us your age :"
if age <3:
    print()