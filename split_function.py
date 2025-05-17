# readingvalues
# program for reading list of values dynamically from Keyboard
print("Enter the elements dynamically from KBD seperated by space:")
lst=[int(x) for x in input().split()]                                 # List comrehension
print("Content of list=",lst)
print("="*60)
print("Enter the elements dynamically from KBD seperated by comma:")
lst1=[float(x) for x in input().split(",")]                          # List comrehension
print("Content of list=",lst1)

print("Enter the elements dynamically from KBD seperated by #:")
lst2=[int(x) for x in input().split("#")]                             # List comrehension
print("Content of list=",lst2)