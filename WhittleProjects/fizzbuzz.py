# 1st project: FizzBuzz
for num in range(1, 101):
    if num % 15 == 0:
        print('fizzbuzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)


# Write a python file called fizzbuzz.py that does the following:
# - Prints the numbers 1-100
# - if the number is divisible by 3, print 'fizz'
# - if the number is divisible by 5, print 'buzz'
# - If the number is divisible by 15, print 'fizzbuzz'
