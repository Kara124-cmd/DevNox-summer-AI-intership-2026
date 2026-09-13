

'''Recursion 
when a function calls itself repeatedly '''

# write a recursive function to print the number from any 1 to 10
def print_num(n = 1):
    if (n == 11):   # base case
        return 
    print(n)
    print_num(n + 1)    # recursive case

print_num()


# write a recursive function to calculate the factorial

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)

print(fact(4))



# a simple recursive function that count from 5
def countdown(n):
    if n <= 0:           # base case
      print('done')
    else:               # recursive case
      print(n)
      countdown(n - 1)

countdown(6)


# calculate the sum of first n natural number
def cal_num(n):
    if n == 0:
        return 0
    return cal_num(n - 1) + n


sum = cal_num(5)
print(sum)


# print factorial using recursion
def fact(n):
   if n == 0 or n == 1:
      return 1
   else:
      return n * fact(n - 1)

print(fact(5))



# print fabonacci series
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))



# recursion with list
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))
