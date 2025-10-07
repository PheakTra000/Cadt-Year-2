# Exercise 1

# def sum(a, b):
#     return a + b

# def difference(a, b):
#     return a - b

# def product(a, b):
#     return a * b

# def quotient(a, b):
#     return a / b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(sum(num1, num2))
# print(difference(num1, num2))
# print(product(num1, num2))
# print(quotient(num1, num2))


# Exercise 2

# def compare(a, b):
#     if a > b:
#         return a
#     else: return b

# def large_num(a, b, c):
#     return compare(compare(a, b), c)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# print(large_num(num1, num2, num3))



# Exercise 3

# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else: 
#         print(i)

# Exercise 4

# def factorial(a):
#     saveNum = a
#     fac = 1
#     while saveNum > 0:
#         fac = fac * saveNum
#         saveNum -= 1
#     return fac
    

# num = int(input("Enter number: "))

# print(factorial(num))

# Exercise 5

# def palindrome(word, word_len, half_word_len):
#     for i in range(half_word_len):
#         if (word[i] != word[word_len - i - 1]):
#             return False
#     return True

# word = input("Enter your word: ").lower()
# word_len = len(word)
# half_word_len = int(word_len / 2)

# if palindrome(word, word_len, half_word_len):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")
    

# Bonus

def long_length_pswd(pswd_len):
    if pswd_len < 8:
        return False
    else: return True

def upper_special_case(pswd, pswd_len):
    for i in range(pswd_len):
        if pswd[i] == {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')'}:
            return True
    


    









