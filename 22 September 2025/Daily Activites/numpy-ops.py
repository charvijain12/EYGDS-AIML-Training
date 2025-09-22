import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr2)

marks = np.array([80,85,90,75])
print("Max Marks:", marks.max()) #max marks
print("Min marks:", marks.min()) #min marks
print("Average:", marks.mean()) #avg marks

data = np.array([10,20,30,40,50])
print("first 3 elements:", data[:3]) #slicing
print("Reversed:", data[::-1]) #reverse
print("sum:", np.sum(data)) #sum
print("Standard deviation:", np.std(data)) #standard deviation