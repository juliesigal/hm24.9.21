#home work targil 1

x = int(input("please enter number: "))
max = x

while x > 0:
    if x > max:
        max = x
    x = int(input("please enter number: "))

print(max)

#home work targil 2

x = int(input("please enter number: "))
mini = x

while x > 0:
    if mini > x:
        mini = x
    x = int(input("please enter number: "))

print(mini)

#home work targil 3

x = int(input("please enter number: "))
digit = x

while x // 10 > 0:
    digit = x // 10
    x = x // 10

print(digit)

#home work targil 4

x = int(input("please enter number: "))
result = 0

while x > 0:
    result = result + (x % 10)
    x = x // 10

print(result)

#home work targil 5

num = int(input("please enter number: "))
result = 1

for i in range(1,num+1):
    result = result * i

print(result)



#home work targil 6 

num = int(input("please enter number: "))

for i in range(1,num+1):
    if num % i == 0:
        print(i)
        
        
#home work targil 7

x = int(input("please enter a number"))
y = int(input("please enter a number"))
max_div = 1
count = 1
if x == y:
    print(x)
else:
    if x < y:
        min_num = x
    else:
        min_num = y
    while count <= min_num:
        if (x % count == 0) and (y % count == 0):
            max_div = count
        count = count + 1

print(max_div)
