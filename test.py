def singleNumber(nums):
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic.keys():
        if dic[i] == 1:
            return i

nums = [4,1,2,1,2]
print(singleNumber(nums))