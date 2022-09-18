## Add code below with answer clearly stated
# A simple method to calculate the factorial of number, as python can support longer numbers
def nFactorial(number):
    # Inially factorial is set to 1
    factorial = 1
    # A loop starting from 1 to the number
    for i in range(1, number+1):
        # Multiply the ith number with the previously calculated factorial
        factorial = factorial*i
    # Initial Sum
    sum = 0
    # A loop to get all the digits from factorial
    while factorial > 0:
        # Get a single digit and add that to sum
        sum += factorial % 10
        # Remove that digit from the factorial
        factorial = factorial // 10
    # Return the result
    return sum
print(nFactorial(100))


# ## The following code is from the old school technique, where a language cannot support a longer number
# ## This is an helper method, which accepts a bigger number as a list, and multiple a number to the list.
# def helper(list, x):
#     # Initially a carry which is set to 0
#     carry = 0
#     # Get the size of list
#     size = len(list)
#     # A loop to the end of list
#     for i in range(len(list)):
#         # Get the result with the carry.
#         result = carry + list[i] * x
#         # Trim the result to get the last digit from result
#         list[i] = result % 10
#         # Add the carry to carry variable
#         carry = result // 10
#     # If we have a carry, which is not zero
#     while (carry != 0):
#         # Add that carry to the list
#         list.append(carry % 10)
#         # Remove the last digit from carry
#         carry //= 10
#     # Return the list
#     return list

# # Final Method
# def sumOfDigits(number):
#     # Initially add 1 to the list
#     list = [1]
#     # From 1 to the number, multiple each number with the list using helper method
#     for i in range(1, number+1):
#         list = helper(list, i)
#     # Return the sum of all digits from list
#     return sum(list)

# print(sumOfDigits(100))
