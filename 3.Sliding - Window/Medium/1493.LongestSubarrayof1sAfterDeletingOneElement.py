def longestSubarray(nums:int) -> int:
        n = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans
    
input = [1,1,0,0,1,1,1,0,1]
print(longestSubarray(input)) # 4
    