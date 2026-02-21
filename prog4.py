import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.subplot(1,2,1)
plt.plot(x,y)

subjects = ["maths", "physics", "AI"]
marks = [45,65,95]
plt.subplot(1,2,2)
plt.bar(subjects,marks)
plt.show()
#subplot(rows,columns,position)