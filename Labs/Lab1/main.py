#Ex1

# for i in range(40,70):
#     if (i%3==0):
#         print(i)

#Ex2

# names = input("Input your full name: \n")
# names = names.split(" ")
# reversed=""
# while(names):
#     reversed+=(f'{names.pop()} ')
#
# print(reversed)

#Ex3
"""
limit = int(input("Enter the number: \n"))
sum = 0
for i in range(1, limit+1):
    sum += i
print(sum)
"""

#Ex4
"""
i = 5
count = 0

while(1):
    print(i)
    if(count == 9):
        print("Success!")
        break
    i+=1
    count+=1
"""

#Ex5
"""
sentence = "Welcome to the lab!"
for char in "mlcae":
    print(sentence.count(char))
"""

#Ex6
"""
limit = int(input("Enter the number \n"))
result = 1
for i in range(1, limit+1):
    result*=i
print(result)
"""

#Ex7
"""
number = int(input("Type the number: \n"))
if number>100:
    number/=2
    number+=20
    print(number)
elif number<100:
    number*=3
    number-=200
    print(number)

"""

#Ex8
"""
seq = input("Type sequence \n").split(",")
print(seq)
print(tuple(seq))
"""
#Ex9
"""
def square(no):
    for i in range(1, no+1):
        print(i*i)

square(5)
"""