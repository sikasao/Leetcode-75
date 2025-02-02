def gcdOfStrings(str1: str, str2: str) -> str:
        def check(a, b):
            c = ""
            while len(c) < len(b):
                c += a
            return c == b

        for i in range(min(len(str1), len(str2)), 0, -1):
            t = str1[:i]
            if check(t, str1) and check(t, str2):
                return t
        return ''

str1 = "ABCABC"
str2 = "ABC"

print(gcdOfStrings(str1, str2))