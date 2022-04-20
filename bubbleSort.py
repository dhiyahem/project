#sorting by sending the largest to back
def bubbleSort(lst):
  for i in range(len(lst)-1, 0, -1):
    for j in range(0, i):
      if lst[j] > lst[j+1]:
        temp = lst[j]
        lst[j] = lst[j+1]
        lst[j+1] = temp

  return lst
  
lst = [8, 4, 10, -2, 5]
print(lst)
print(bubbleSort(lst))
