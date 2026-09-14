 


# Python Operatores

 # Arithmatic opeartors
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)



# Assignment operators
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x >>= 3
print(x)

x = 5
x <<= 3
print(x)







# The Ternary Operator
# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

num = 8
x = 'weekend' if num > 7 else 'Workday'
print(x)

# Instead of Elif:
# The ternary operator can be used instead of elif in longer if statements:

num = 6
if num == 2:
    print('Monday')
elif num == 4:
    print('Wednesday')
else:
    print('Sunday, it\'s off day')

# instead of this we use ternary operatores
num = 6
print('Monday' if num == 2 else 'Wednesday' if num == 4 else 'Sunday' )





# comparison operators
x = 3
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# chain comparison operators
x = 5
print(1 < x < 10)

print(1 < x & x < 10)


# logical operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)


# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x is not y)
print(x == y)




# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)






# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

# not in 
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

# Membership in Strings
# The membership operators also work with strings:

name = 'usman'
print('u' in 'usman')
print('man' in 'usman')
print('k' in 'usman')
print('s' not in 'usman')






# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

a = 4
b = 5
print(bin(a))
print(bin(b))
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)















