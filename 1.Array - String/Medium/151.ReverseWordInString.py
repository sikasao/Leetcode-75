def reverseWords(s: str) -> str:
        return " ".join(reversed(s.split()))

s = "IceCreAm"

print(reverseWords(s))