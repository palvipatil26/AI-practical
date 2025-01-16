def TowerofHanoi(n, source, destination, auxiliary):
  if n==1:
    print("Move disk 1 from source",source,"to destination",destination)
    return
  TowerofHanoi(n-1, source, auxiliary, destination)
  print("Move disk",n,"from source",source,"to destination",destination)
  TowerofHanoi(n-1, auxiliary, destination, source)

#number of rings
n=4
TowerofHanoi(n,'A','B','C')  #A, B, C are the name of roots
