from collections import deque


def is_palindrome(s):
    new_s = ''.join(s.split()).lower()

    char_deque = deque(new_s)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
        
        return True
    
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Hello world!"))
