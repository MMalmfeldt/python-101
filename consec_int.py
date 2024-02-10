my_int = input('Please enter an integer greater than 0: ')

my_op = input('Enter "s" to compute the sum, or "p" to compute the product. ')

sum_or_prod = 1

for num in range(1, (int(my_int) + 1)):
    if my_op == 's':
        sum_or_prod += (int(num) - 1)
    elif my_op == 'p':
        sum_or_prod *= int(num)
    
if my_op == 's':
    print(f'The sum of the integers between 1 and {my_int} is {sum_or_prod}.')
else:
    print(f'The product of the integers between 1 and {my_int} is {sum_or_prod}.')

