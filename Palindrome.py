def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    # Check if the word is the same forwards and backwards
    return normalized_word == normalized_word[::-1]


print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("hello"))     # Output: False
print(is_palindrome("Madam"))     # Output: True
print(is_palindrome("sir"))       # Output: False
