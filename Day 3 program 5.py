arr=[1,2,3,4]
k=2
missing_cout=0
current =1
index=0
n=len(arr)
while missing_cout<k:
    if index<n and arr[index]==current:
        index+=1
    else:
        missing_cout+=1
        if missing_cout==k:
            result=current
            break
    current+=1
print(result)
