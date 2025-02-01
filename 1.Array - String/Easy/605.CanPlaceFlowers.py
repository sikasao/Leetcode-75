def canPlaceFlowers(flowerbed, n):
    if flowerbed is None or len(flowerbed) == 0:
        return False
    
    count = 0
    for i in range(len(flowerbed)):
        # Check if the current plot is empty and the plots before and after are either empty or out of bounds
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
            if count >= n:
                return True
    return count >= n


flowerbed = [1,0,0,0,1]
n = 1

print(canPlaceFlowers(flowerbed, n))