
def compress(chars:str) -> int:
        i, k, n = 0, 0, len(chars)
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[k] = chars[i]
            k += 1
            if j - i > 1:
                cnt = str(j - i)
                for c in cnt:
                    chars[k] = c
                    k += 1
            i = j
        return k

chars = ["a","a","b","b","c","c","c"]
print(compress(chars)) #Expected output is 6