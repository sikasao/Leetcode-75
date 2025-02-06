from collections import Counter

def maxOperations(nums:int, k: int) -> int:
        cnt = Counter()
        ans = 0
        for x in nums:
            if cnt[k - x]:
                ans += 1
                cnt[k - x] -= 1
            else:
                cnt[x] += 1
        return ans

nums = [1,2,3,4]
k = 5
print(maxOperations(nums,k)) # 2