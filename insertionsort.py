1def insertionsort(1, arr1):
2	   for index in range(1,len(arr1)):
3	
4	     currentvalue = arr1[index]
5	     position = index
6	
7	     while position>0 and arr1[position-1]>currentvalue:
8	         arr1[position]=arr1[position-1]
9	         position = position-1
10	
11	     arr1[position]=currentvalue
12	
13	arr1 = [14,46,43,27,57,41,45,21,70]
14	insertionSort(arr1)
15	print(arr1)
