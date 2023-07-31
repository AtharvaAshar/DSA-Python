def kDiffPairs(nums):
    d={}
    count = 0
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if i+3 in d:
            count+=d[i]*d[i+3]
            
    return count

print(kDiffPairs([2,-1,3,5,6,0,-1,2,6]))