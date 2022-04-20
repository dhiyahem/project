# main.py
#make a new list to return. write downt he big O 
#htin: don't forget o remove from the original list
def insertSort1(lst):
  toReturn = []
  for i in range(len(lst)):
    itemToInsert = lst[i]
    toReturn.append(itemToInsert)
    indexToInsert = i
    
    while itemToInsert < toReturn[indexToInsert - 1] and indexToInsert != 0:
      toSwap = toReturn[indexToInsert - 1]
  
      toReturn[indexToInsert - 1] = itemToInsert
      toReturn[indexToInsert] = toSwap
      
      indexToInsert -= 1
      
  return toReturn
  
lst = [5, 2, 0,7,4,6,27,0,1]
      
      

      
    
def insertSort2(lst):
  for i in range(len(lst)):
    item = lst[i]
    indexOfItem = i
    while indexOfItem != 0 and item < lst[indexOfItem - 1]:
      temp = lst[indexOfItem - 1]
      indexOfTemp = indexOfItem - 1
      lst[indexOfTemp] = item
      lst[indexOfItem] = temp
      
      indexOfItem -= 1
      
  return lst
    
    
print(insertSort2(lst))
    
    



