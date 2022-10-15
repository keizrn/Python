sum = 0
num = 12.3456

while num % 1 > 0:
    num *= 10
    print(num)

while num%10 > 0:
    sum += int(num%10)
    num = num//10
print(sum)