# Given a string as a parameter to a function, return True if the string is a palindrome and False if not

string1 = "Dad"
string2 = "add"


def is_palindrome(string):
    if string.lower() == string.lower()[::-1]:
        return True
    else:
        return False

is_palindrome(string1)
is_palindrome(string2)
