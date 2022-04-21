import random

def partition(lst, pivot):
  gr = []
  eq = []
  less = []
  
  for num in lst:
    if num > pivot:
      gr.append(num)
    elif num == pivot:
      eq.append(num)
    else:
      less.append(num)
      
  return less, eq, gr
  

def quickSort(lst):
  n = len(lst)
  
  if n <= 1:
    return lst
    
  pivotIn = random.randint(0, n -1)
  pivot = lst[pivotIn]
  
  less, equal, great = partition(lst, pivot)
  
