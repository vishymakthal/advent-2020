
nums = []

with open('nums.txt','r') as f:
    n = f.readline()
    while(n):
        nums.append(int(n))
        n = f.readline()

target = 2020

def two_sum():

    m = {}
    for n in nums:
        if n in m:
            return (n,m[n])
        m[target - n ] = n 

def three_sum():

    nums.sort()
    
    for i in range(len(nums)-2):
        right = len(nums) - 1
        left = i + 1
        while left <= right:
            n = sum((nums[i], nums[left],nums[right]))
            if n == target:
                print(nums[i],nums[left],nums[right])
                print(nums[i]*nums[left]*nums[right])
                return

            if n < target:
                left += 1
            if n > target:
                right -= 1
            
three_sum()