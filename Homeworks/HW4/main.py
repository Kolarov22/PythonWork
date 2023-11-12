from datetime import datetime
import re

#Ex1

# def identifySeq(string):
#     pattern = re.compile("^[a-z0-9*]+$")
#     if pattern.match(string):
#         print("Sequence is valid")
#     else:
#         print("invalid sequence")
#
# identifySeq("24pppp*")
# identifySeq("HA3020")

#Ex2

# def upper_lower(string):
#     pattern = re.compile("^[A-Z]+_+[a-z]+$")
#     if pattern.match(string):
#         print("Valid pattern")
#     else:
#         print("Invalid pattern")
#
# upper_lower("FILS_student")
# upper_lower("student")

#Ex3

# hw4 = "rectangle square sphere triangle cone cube cylinder"
# hw4 = hw4.split()
# pattern = re.compile('(re|le)$')
# matching_strings = [word for word in hw4 if pattern.search(word)]
# print(matching_strings)

#Ex4
# sentence = "The dealership has on sale 3 BMW, 4 AUDI, 8 MERC"
# pattern = re.compile("([0-9])+.([A-Z]{3,4})+")
# print(pattern.findall(sentence))
# for i in pattern.finditer(sentence):
#     print(i.group(1))
#     print(i.group(2))

#Ex5
# date = "21-12-01"
# pattern = r"(\d{2})-(\d{2})-(\d{2})"
# new_date = re.sub(pattern, r"\3-\2-\1", date)
# new_date = datetime.strptime(new_date, "%d-%m-%y")
# print(new_date.strftime("%d-%B-%y"))

#Ex6

# def ex6(string):
#     pattern = re.compile("^m.{3}n+$")
#     if(pattern.match(string)):
#         print("Valid")
#     else:
#         print("Invalid")
#
# ex6("mardn")
# ex6("madasiis")

#Ex7

# def ex7(string):
#     pattern = re.compile("^h*i{2,3}$")
#     if (pattern.match(string)):
#         print("Valid")
#     else:
#         print("Invalid")
#
# ex7("hiii")
# ex7("hei")

#Ex8

# def ex8(string):
#     pattern = re.compile("\Bq\B")
#     if (pattern.search(string)):
#         print("Valid")
#     else:
#         print("Invalid")
#
# ex8("maquis")
# ex8("quentin")

#Ex9
# def ex9(string):
#     new_string = string.replace("a","u")
#     new_string = new_string.replace("i", "e")
#     return new_string
# print(ex9("I made this for testing the function"))