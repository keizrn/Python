# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def find_prime_numbers(num_5: int):
    list_5 = []
    for i5 in range(2, round((num_5+1)/2)):
        if num_5 % i5 == 0:
            check_5 = True
            for i5_a in range(2, i5):
                check_5 = True
                if i5 % i5_a == 0:
                    check_5 = False
                if check_5 == False:
                    break
            #print(i5, check_5)
            if check_5:
                list_5.append(i5)
    if list_5 == []:
        print('No prime multipliers found for this number.')
    else:
        print(list_5)

try:
    num_0 = int(input('This program will show you all prime multipliers of your number N. If you are lucky...\n'))
    find_prime_numbers(num_0)
except:
    print('Your input was incorrect')



#find_prime_numbers(27999510)

