def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1  # Start pointers at the beginning and end.

    while left < right:
        print('====')
        print(left)
        print(right)
        if s[left] != s[right]:
            return False  # If characters don't match, it's not a palindrome.
        left += 1
        right -= 1

    return True


# Practice
print(isPalindrome("racecar"))  # Should print True
print(isPalindrome("hello"))  # Should print False


