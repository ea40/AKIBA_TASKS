word = input("Enter a word or phrase: ")    
    
if word == word[::-1]:
    result = "is a palindrome"
else:
    result = "is not a palindrome"

print(f"{word} {result}")