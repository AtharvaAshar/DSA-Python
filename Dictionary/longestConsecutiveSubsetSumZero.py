def longestZeroSubset(nums):
    d={}
    sum_value=0
    subset_len=0
    for i in range(len(nums)):
        sum_value+=nums[i]
        if sum_value==0:
            subset_len=i+1
        if sum_value not in d:
            d[sum_value]=i
        else:
            subset_len=max(subset_len,i-d[sum_value])
    return subset_len


print(longestZeroSubset([6,3,-1,2,-4,3,1,-2,20]))
print(longestZeroSubset([95, -97, -387, -435, -5, -70, 897, 127, 23, 284]))
# l = ['95', '-97', '-387', '-435', '-5', '-70', '897', '127', '23', '284']
# a=[int(x) for x in l]
# print(a)