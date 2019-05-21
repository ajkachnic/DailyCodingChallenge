def addtok(k, array):
  returned = False
  for _ in range(len(array)):
    for i in range(len(array) -1):
      if array[_] + array[i] == k:
        returned =  True
  return returned
