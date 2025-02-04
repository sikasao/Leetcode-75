def moveZeroes(nums:int) -> list:
        k = 0
        for i, x in enumerate(nums):
            if x:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return nums

s = [0,1,0,3,12]
print(moveZeroes(s))