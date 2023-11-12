import re

#Ex1
#
# words =["rectangle", "square", "sphere", "triangle", "cone", "cube", "cylinder"]
#
# pattern = re.compile(r'^(c|s).*e$')
#
# matching_strings = [word for word in words if pattern.match(word)]
#
# for string in matching_strings:
#     print(string)


#Ex2
# words = ["car", "cat", "dog", "pool", "bath", "cone", "cube", "ring", "int"]
#
# pattern = re.compile("\w{4}")
#
# match = [word for word in words if pattern.match(word)]
#
# for string in match:
#     print(string)

#Ex3

# words = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexogon",
#          "rectangle", "parallelogram", "trapezoid"]
#
# for word in words:
#     x = re.findall("re$", word)
#     if x:
#         print(word)


#Ex4

# geo = "A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6." \
#       "While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides."
#
#
# words = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexogon",
#           "rectangle", "parallelogram", "trapezoid"]
#
# for word in words:
#     x = re.findall(word, geo)
#
#     if x:
#         print (word)
# d = re.findall("\d", geo)
# print(d)
# l = re.findall("\D", geo)
# print(l)


#Ex5

# link ="https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-thewar-for-gloria-read-until-you-understand-and-the-end-of-bias"
#
# date = re.findall("\d{1,4}\/\d{1,2}\/\d{2,4}", link)
# print(date)

#Ex6

input_date = "2021-11-02"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
formatted_date = re.sub(pattern, r"\3-\2-\1", input_date)
print(formatted_date)

#Ex7

# def startswithDigit(string):
#     pattern = re.compile("^[0-9]")
#
#     if(pattern.match(string)):
#         print("The string starts with a digit")
#     else:
#         print("The string doesn't start with a digit")
#
# startswithDigit("3cai")
# startswithDigit("faradigit")

#Ex8

# def endswithDigit(string):
#     pattern = re.findall("[0-9]$", string)
#
#     if(pattern):
#         print("Ends with digit")
#     else:
#         print("Doesn't end with digit")
#
# endswithDigit("boss0")
# endswithDigit("faradigit")


#Ex9

# def containsDigit(string):
#     pattern = re.findall("\d", string)
#
#     if(pattern):
#         print("Contains digit")
#     else:
#         print("Doesn't contain digit")
# containsDigit("an420")
# containsDigit("dsdsdsd")









