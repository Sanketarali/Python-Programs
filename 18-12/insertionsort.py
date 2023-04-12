a=[12,3,1,15,11]
for i in range(1,len(a)):
    k=a[i]
    j=i-1
    while j>=0 and k<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=k

print("sorted array",a)    