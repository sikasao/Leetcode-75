def findMaxAverage(nums:int, k: int) -> float:
        total = sum(nums[:k])
        maxAvg = total/k
        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[i+k]
            maxAvg = max(maxAvg, total/k)
        return maxAvg

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k)) # 12.75