def lcs(nums):
    hashSet=set()
    n=len(nums)
    max_len=0
    for i in nums:
        hashSet.add(i)
    for i in range(n):
        if nums[i]-1 not in hashSet:
            j=nums[i]
            while j in hashSet:
                j+=1
            max_len=max(max_len,j-nums[i])
    return max_len
print(lcs([0,3,7,2,5,8,4,6,0,1]))