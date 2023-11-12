import myModule
import random
import datetime
import os

# Ex1

# myModule.myFunction()

# Ex2

# list = []
# for i in range(5):
#     list.append(random.randint(0, 100))
#
# print(list)

# Ex3

# list = []
# for i in range(5):
#     list.append(random.randint(40,70))
#
# print(list)

# Ex4

# myDate = datetime.datetime.now()
# print(myDate.strftime("%A"))

# Ex5

# os.mkdir("myFolder")
# file = open("myFolder\TextFile.txt", "w")
# file.write("Dummy Text1\nDummy Text2")
# file = open("myFolder\TextFile.txt", "r")
# for i in range(2):
#     print(file.readline())
# file = open("myFolder\TextFile.txt", "w")
# file.write("The old content of the file was replaced with this")


#Ex6

# if(os.name == "nt"):
#     print("You are using Windows")
# print(f"Current dir: {os.getcwd()}\nand its subdirs: {os.listdir(os.getcwd())}")

#Ex7

# data = datetime.datetime.now()
# data = data.strftime("%x")
# data = data.split("/")
# data[1] = str(int(data[1])-10)
# tobePrinted=""
# for el in data:
#     tobePrinted += el + "/"
# print(tobePrinted[:-1])

