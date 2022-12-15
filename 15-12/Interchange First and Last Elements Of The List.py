# Interchange First and Last Elements Of The List

list=[1,2,3,4,5]

temp=list[0]
list[0]=list[-1]
list[-1]=temp
print(list)