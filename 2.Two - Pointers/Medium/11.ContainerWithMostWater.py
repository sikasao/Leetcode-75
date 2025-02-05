def maxArea(height:int) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            t = min(height[l], height[r]) * (r - l)
            ans = max(ans, t)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

s = [1,8,6,2,5,4,8,3,7]
print(maxArea(s)) # 49