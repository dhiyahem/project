def merge(lst1, lst2):
  result = []
  while len(lst1) > 0 and len(lst2) > 0:
    #why do we need an and instead of an or?
    if lst1[0] >= lst2[0]:
      result.append(lst2.pop(0))
      
    else:
      result.append(lst1.pop(0))
      
  if len(lst1) == 0:
    return result + lst2
    
  else:
    return result + lst1
    

def mergeSort(lst):
  n = len(lst)
  
  if n <= 1:
    return lst
    
    
  firstHalf = mergeSort(lst[:n//2])
  secondHalf = mergeSort(lst[n//2:])
  
  return merge(firstHalf, secondHalf)
  
print(mergeSort([5, 1, 3, 2, 6]))

def mergeSort1(lst):
  n = len(lst)
  
  if n <= 1:
    return lst
    
  firstHalf = mergeSort1(lst[:n//2])
  secondHalf = mergeSort1(lst[n//2:])
    
  result = []
  aIndex = 0
  bIndex = 0
  
  while aIndex < len(firstHalf) and bIndex < len(secondHalf):
    if firstHalf[aIndex] < secondHalf[bIndex]:
      result.append(firstHalf[aIndex])
      aIndex += 1
    else:
      result.append)secondHalf[bIndex])
      bIndex += 1
      
  while aIndex < len(firstHalf):
    result.append(firstHalf[aIndex])
    aIndex += 1
    
  while bIndex < len(secondHalf):
    result.append(secondHalf[bIndex])
    
    
  return result
