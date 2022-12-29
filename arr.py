#find the elements which give sum as 9
#(3+6=9 and 4+5=9)

arr=[1,2,3,4,5,6]
sum=9
arr1=[]
n=len(arr)
i=0
while i<n:
    j=i+1
    while j<n:
        if (arr[i]+arr[j]==sum):
            (a,b)=(arr[i],arr[j])
            arr1.append(a)
            arr1.append(b)
        j+=1
    i+=1
    
print(arr1)
