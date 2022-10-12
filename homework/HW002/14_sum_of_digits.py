# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример: 6782 -> 23 0,56 -> 11

def calc_digits(real_num):
    list_char = list(real_num)
    list_int = []
#    print(list_char) # check string of chars
    if '.' in list_char:        # check and delete dote
        list_char.remove('.')
    elif ',' in list_char:      # check and delete comma (only 1 dote OR 1 comma must be deleted)
        list_char.remove(',')
    if '-' in list_char:    
        list_char.remove('-')   # check and delete minus sign (minus must be deleted anyway)
    for i in range(0,len(list_char)):
        try:
            list_int.append(int(list_char[i]))  # fill in new list of integers
        except:
            print('Your input was incorrect')   # if there are unexpected symbols (chars, etc.)
            return
    print(sum(list_int))

string2 = input('input number\n').replace('-','')
calc_digits(string2)
