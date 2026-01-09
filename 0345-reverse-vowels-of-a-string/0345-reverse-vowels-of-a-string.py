class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) -1
        vowels = ['a','e','i','o','u']
        a = list(s)

        while left < right:
            if  a[right].lower()  not in vowels:
                right -=1
            elif  a[left].lower() not in vowels:
                left += 1
            else:
                a[left],a[right] = a[right],a[left]
                left += 1
                right -= 1
        return ''.join(a)

        