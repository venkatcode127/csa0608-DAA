def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
random_array=[5,2,9,1,5,6]
print("original Array (Random):",random_array)
selection_sort(random_array)
print("sorted array (Random):",random_array)
print()

reverse_sorted_array=[10,89,6,4,2]
print("original Array (Reverse sorted):",reverse_sorted_array)
selection_sort(reverse_sorted_array)
print("sorted Array(Reverse sorted):",reverse_sorted_array)
print()

sorted_array=[1,2,3,4,5]
print("original Array(Already sorted):",sorted_array)
selection_sort(sorted_array)
print("sorted Array (already sorted):",sorted_array)
