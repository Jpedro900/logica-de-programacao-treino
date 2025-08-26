#Reverter String

def reverse_str(s: str):
    r_str = ""

    for i in range(len(s)-1, -1, -1):
        r_str+=s[i]

    return r_str

if __name__ == "__main__":
    print(reverse_str("abc"))  # esperado "cba"
    print(reverse_str("a"))    # esperado "a"
    print(reverse_str(""))     # esperado ""
