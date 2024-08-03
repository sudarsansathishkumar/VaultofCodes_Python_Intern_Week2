# 1. Write a program to count word frequencies in a given text

def count_word_frequency(text):
    words = list(text.split(" "))
    freq = {}
    for word in words:
        word = word.strip(";:'\"()[]{}.,?").lower()
        if word:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    return freq

inp = input("Enter the text here: ")
freq = count_word_frequency(inp)
print("The frequency of words are listed below:")
for key, val in sorted(freq.items(), key=lambda item : item[1], reverse=True):
    print(key, "\t=> ", val)

# Enter the text here: This is a (sample) test case, to ;  text this prog.
# The frequency of words are listed below:
# this    =>  2
# is      =>  1
# a       =>  1
# sample  =>  1
# test    =>  1
# case    =>  1
# to      =>  1
# text    =>  1
# prog    =>  1