# 3. List Manipulation
# Create a list of numbers, then write a program that prints the square of each number in the list

def sq_num_list(nums):
    print("The square values of each numbers are:")
    for i in nums:
        print(f"{i} ^ 2 = {i ** 2}")

print("Enter the list of numbers here (separate by space):")
nums = list(map(int, input().split(" ")))
sq_num_list(nums)

# Enter the list of numbers here (separate by space):
# 1 2 3 4 5 6 7 8 9 10
# The square values of each numbers are:
# 1 ^ 2 = 1
# 2 ^ 2 = 4
# 3 ^ 2 = 9
# 4 ^ 2 = 16
# 5 ^ 2 = 25
# 6 ^ 2 = 36
# 7 ^ 2 = 49
# 8 ^ 2 = 64
# 9 ^ 2 = 81
# 10 ^ 2 = 100