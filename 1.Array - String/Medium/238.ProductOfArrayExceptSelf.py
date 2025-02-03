def productExceptSelf(nums:int) -> int:
        n = len(nums)
        ans = [0] * n
        left = right = 1
        for i, x in enumerate(nums):
            ans[i] = left
            left *= x
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans

nums = [1,2,3,4]
print(productExceptSelf(nums)) #Expected output is [24,12,8,6]