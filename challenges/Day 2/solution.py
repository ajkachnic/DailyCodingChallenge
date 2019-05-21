def arrayTimes(array):
  newarray = []
  newvalue = 1
  for _ in range(0, len(array)):
    for i in range (0, len(array)):
      if i != _:
        newvalue *= array[i]
      
    newarray.append(newvalue)
    newvalue = 1
  return newarray
  
