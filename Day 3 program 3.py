arrays=[
    [64, 25, 12, 22, 11],
    [29, 10, 14, 37, 13],
    [3, 5, 2, 1, 4],
    [5, 4, 3, 2, 1]
]
for arr in arrays:
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    print(arr)
