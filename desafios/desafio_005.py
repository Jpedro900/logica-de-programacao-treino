#Palindromo Basico

def is_palindrome(s: str):
    r_str = ""
    for i in range(len(s)-1, -1, -1):
        r_str+=s[i]
    if s == r_str:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(is_palindrome("ana"))   # esperado True
    print(is_palindrome("abc"))   # esperado False
    print(is_palindrome(""))      # esperado True
    print(is_palindrome("a"))     # esperado True
    print(is_palindrome("radar")) # esperado True
    print(is_palindrome("python"))# esperado False