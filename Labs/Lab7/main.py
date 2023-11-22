import matplotlib.pyplot as plt
import numpy as np

#1

# list1 = [1.4, 5.9, 2.6, 7.3, 8.5, 9.3, 6.1]
# arr1 = np.array(list1)
# print(arr1)

#2

# list2 = [a for a in np.arange(70,91) if a%2 == 0]
# arr2 = np.array(list2)
# print(arr2)

#3

# mat3 = np.array([[np.zeros(3)], [np.zeros(3)], [np.zeros(3)]])
# mat3= np.diag([3, 7, 11])
# print(mat3)

#4

# mat4 = np.arange(10,16).reshape(2,3)
# print(mat4)


#5

ex5=np.array([[10, 50, 70, 20, 40],
             [5,45, 95, 35, 65]])
# def filter_numbers_2d(arr, threshold):
#     smaller_than_threshold = arr[arr < threshold]
#     greater_than_threshold = arr[arr > threshold]
#     return smaller_than_threshold, greater_than_threshold
#
#
# smaller_numbers_2d, greater_numbers_2d = filter_numbers_2d(ex5, 43)
#
# print("\nNumbers strictly smaller than", 43, ":", smaller_numbers_2d)
# print("\nNumbers strictly greater than", 43, ":", greater_numbers_2d)


#6

# np.savetxt("output.txt", ex5)
# arr5 = np.loadtxt("output.txt")
# print(arr5)

#7

x1 = np.array([0,1,2])
y1 = np.array([3,4,5])

plt.figure(1)
plt.title("Title1")
plt.plot(x1,y1,'-o', c = 'blue', mfc = 'blue', mec = 'red')

x1 = np.array([6, 8])
y1 = np.array([9, 11])

plt.figure(2)
plt.title("Title2")
plt.plot(x1,y1,'--', c = 'green')
plt.grid()

plt.figure(3)
plt.title("Title3")
plt.bar(x1,y1, color = 'green', width = 1.75)

plt.figure(4)
plt.title("Title4")
colors = np.random.randint(7,size=(20))
scatterX1 = np.random.randint(20,size=(20))
scatterY1 = np.random.randint(20,size=(20))
plt.scatter(scatterX1,scatterY1,c = colors)

plt.figure(5)
plt.title("Title5")
x2 = np.array([35,40,45])
y2 = np.array([5,10,20])

plt.plot(x1,y1, '--o', c = 'blue')
plt.plot(x2,y2, '--', c = 'yellow', linewidth = 3)

plt.figure(6)
plt.title("Title6")
plt.barh(x2,y2, color = "purple", height=1.75)


plt.figure(7)
plt.title("Title7")
x3 = np.array([5,6,7])
y3 = np.array([1,2,3])

x4 = np.array([4,6,8])
y4 = np.array([0.5, 2 , 3.5])

plt.plot(x3,y3,'--', c='red', linewidth = 2)
plt.plot(x4,y4,'-o', c='blue')


plt.figure(8)
plt.title("Title8")
pieValues = ([20,25,15,10,30])
mylabels = ["A","B","C","D","E"]
mycolors = ["red","blue","yellow","orange","green"]
plt.pie(pieValues,labels = mylabels, colors = mycolors)
plt.show()
