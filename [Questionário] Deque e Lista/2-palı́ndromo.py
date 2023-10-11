def is_palindrome(s):
    return s == s[::-1]

def find_2_palindromes(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+3, len(s)+1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
            if len(palindromes) >= 2:
                return True
    return False

words = input().split()

for word in words:
    if find_2_palindromes(word):
        print(word)
        break
