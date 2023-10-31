a=[]
print("**************Bubble Sort****************")
size=int(input("Enter the size of array:"))

print(f"\nEnter {size} elements:")
for i in range(size):
  ele=int(input())
  a.append(ele)
  
print("\n**list before sorted:**\n")
for i in range(size):
  print(" ",a[i],end=" ")
  
for i in range(size):
  flag=0
  for j in range(size-1-i):
    if(a[j]>a[j+1]):  
      flag=1
      temp=a[j]
      a[j]=a[j+1]
      a[j+1]=temp
  if flag==0:
    break
    
print("\n**After sorted list is:**\n")
for i in range(size):
  print(" ",a[i],end=" ")
