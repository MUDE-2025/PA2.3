# The code below is supposed to find the maximum even number in a list and return its square

# Correct version:
numbers = [3, 7, 2, 8, 5, 10, 6]

def max_even_square(nums):
    max_num = None
    for n in nums:
        if n % 2 == 0:          
            if max_num is None or n > max_num:
                max_num = n

    square = max_num ** 2      
    return square

print("The max even number squared is:", max_even_square(numbers))