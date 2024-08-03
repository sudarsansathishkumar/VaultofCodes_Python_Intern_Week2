# 2. Palindrome Checker
# Write a program that checks if a given word is a palindrome

def check_palindrome(text):
    if text == text[-1::-1]:
        return True
    else:
        return False

inp = input("Enter the text here: ")
if check_palindrome(inp.lower()):
    print(f"\"{inp}\", is a palindrome.")
else:
    print(f"\"{inp}\", is not a palindrome.")


# Enter the text here: asdfdsa
# "asdfdsa", is a palindrome.

# Enter the text here: palindrome
# "palindrome", is not a palindrome.