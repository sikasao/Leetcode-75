def increasingTriplet(nums:int) -> bool:
        mi, mid = inf, inf
        for num in nums:
            if num > mid:
                return True
            if num <= mi:
                mi = num
            else:
                mid = num
        return False

input = [1,2,3,4,5]
print(increasingTriplet(input)) #Expected output is True