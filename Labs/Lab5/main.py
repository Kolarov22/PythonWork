import re
import pandas as pd


#Ex1

# def ex1(s):
#     if(len(s) == 0):
#         return "String doesn't belong to language"
#     for i in range(len(s)):
#         if s[i] != '1':
#             return "String doesn't belong to language"
#     return "String belongs to language"
#
# print(ex1("1111111112"))

#Ex2


def startA(x):
        if(x == '0'):
            dfa = 1
        else:
            dfa = -1
        return dfa
def stateB(x):
        if(x=='0'):
            dfa = 2
        else:
            dfa = -1
        return dfa
def stateC(x):
        if(x=='0'):
            dfa = 3
        elif (x=='1'):
            dfa = 5
        else:
            dfa = -1
        return dfa
def stateD(x):
        if (x=='0'):
            dfa = 4
        else:
            dfa = -1
        return dfa
def stateF(x):
        if(x=='0'):
            dfa = 3
        elif(x=='1'):
            dfa = 5
        else:
            dfa = -1
        return dfa
def stateE(x):
        if(x=='1'):
            dfa = 6
        else:
            dfa = -1
        return dfa
def stateG(x):
        if(x=='1'):
            dfa = 6
        else:
            dfa = -1
        return dfa

def ex2(s):
    l = len(s)
    dfa = 0
    for i in range(l):
        if(dfa == 0):
            dfa = startA(s[i])
        elif(dfa == 1):
            dfa = stateB(s[i])
        elif(dfa == 2):
            dfa = stateC(s[i])
        elif(dfa == 3):
            dfa = stateD(s[i])
        elif(dfa == 4):
            dfa = stateF(s[i])
        elif(dfa == 5):
            dfa = stateE(s[i])
        elif (dfa == 6):
            dfa = stateG(s[i])

        else:
            return "Doesn't belong"
    if(dfa == 6):
        return "The string belongs to the language"
    else:
        return "Doesn't belong"

s1 = "001111"
s2 = "0001111"
s3 = "00001111"

print(s1, ex2(s1), "\n")
print(s2, ex2(s2), "\n")
print(s3, ex2(s3), "\n")

#Ex3

# def ex3(s):
#     if len(s)<3:
#         return "String doesn't belong"
#
#     x = s[0]
#
#     for i in range(1, len(s)-1):
#         if s[i] != x:
#          continue
#     if s[-1] == x:
#         return "String does belong"
#     else:
#         return "String doesn't belong"
#
# myString="a42289274972fdhfuhdfha"
# otherString ="a934394389438948bbbb"
# print(ex3(myString), "\n")
# print(ex3(otherString), "\n")





