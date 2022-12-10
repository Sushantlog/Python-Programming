#10/12/2022
fruit = "Mango"             
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])    #always start from 0
print(fruit[0:-3])      #len(fruit)=5-3=2  (2-1)=>1 ie. Ma

# 0 1 2 3 4
# M a n g o
print(fruit[:len(fruit)-3])
print("------------------")
print(fruit[-1:len(fruit) - 3])
print("------------------")
#(5-1)=>2   (5-3)=>2  no any relation not print
print(fruit[-3:-1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])

