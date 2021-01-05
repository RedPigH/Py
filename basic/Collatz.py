# Collatz

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


print('Enter number :')
try:
    num = input();
    while num != 1:
        num = collatz(int(num))
        print(int(num))
except:
    print('input Type is Integer type!')



