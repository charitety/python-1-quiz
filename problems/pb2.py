def max_values(nums):
    maxNumbers = []
    maxValue = float("inf")
    for num in nums:
        if num == maxValue:
            maxNumbers.append(num)
        if num > maxValue:
            maxValue = []
            maxNumbers.append[num]
    return maxNumbers


print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
print(max_values([-5, -2, -1, -11])) # -> [1, 2]