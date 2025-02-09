def largestAltitude(gain:int) -> int:
        maxAltitude = 0
        currentAltitude = 0
        
        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)
        
        return maxAltitude

input = [-5,1,5,0,-7]
print(largestAltitude(input)) # 1