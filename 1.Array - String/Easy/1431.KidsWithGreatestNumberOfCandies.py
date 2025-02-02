
def kidsWithCandies(candies:int, extraCandies:int) -> bool:
        mx = max(candies)
        return [candy + extraCandies >= mx for candy in candies]

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))