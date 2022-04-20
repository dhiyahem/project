import random

def selectionSort(lst):
  toReturn = []
  while len(lst) > 0:
    minNumber = lst[0]
    for i in range(len(lst)):
      if minNumber > lst[i]:
        minNumber = lst[i]
    toReturn.append(minNumber)
    lst.remove(minNumber)
  return toReturn
  
l = [random.randint(1,100) for i in range(10)]

print(l)

print(selectionSort(l))

#O(1) space compplexity, because we just modify the original list
def selectionSort2(lst):
  for i in range(len(lst)):
    minItem = lst[i]
    minItemIndex = i 
    
    for j in range(i, len(lst)):
      if lst[j] < minItem 
      minItem = lst[j]
      minItemIndex = j 
      
    temp = lst[i]
    lst[i] = minItem 
    lst[minItemIndex] = temp
    
  return lst
  
    
