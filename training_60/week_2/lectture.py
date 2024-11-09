

def pref_sum(l):

    p_s = [0] * (len(l)+1)
    for i in range(1, len(p_s)):
        p_s[i] = p_s[i-1] + l[i-1]
    return p_s

def pref_zeros(nums):
        p_z = [0] * (len(nums)+1)

        for i in range(1, len(p_z)):
            if nums[i-1] == 0:
                p_z[i] = p_z[i-1]+1
            else:
                p_z[i] = p_z[i-1]
        
        return p_z

def ex_1():


    a = [2,3,2,3,4,4,2,4]

    print(f'   a        : {a}')
    pf = pref_sum(a)
    print(pf)
   

# ex_1()

def count_zeros():

    
    def count_zeros(pref_zeros, l ,r):
        return pref_zeros[r] - pref_zeros[l]

    a = [6,0,7,8,0,0,7,0,0,6,8,0,7,6,8]
    pz = pref_zeros(a)

    print(f'   {a}')
    print(pz)

    print(count_zeros(pz, 2 ,7))
    

# count_zeros()

def count_zero_sum():
    nums = [1, 2, -3, 4, -2, 1, -3, 0]

    def count_pref_sum(nums):
        pref_sum = {}
        nowsum = 0
        for n in nums:
            nowsum +=n
            if nowsum not in pref_sum:
                pref_sum[nowsum] = 0
            pref_sum[nowsum] += 1
        return  pref_sum
    

    def count_zero_sum_ranges(pref_sum_dict):
        cnt = 0
        for sm in pref_sum_dict:
            c_sm = pref_sum_dict[sm]
            cnt += c_sm * (c_sm-1)//2
        return cnt

    pref_sum_dict = count_pref_sum(nums)
    zero_range_sum = count_zero_sum_ranges(pref_sum_dict)
    print(zero_range_sum)


# count_zero_sum()

def sum_of_pair():
    nums = [1,3,3,4, 5, 6]

    def solution(nums, k):
        pairs_count = 0
        last = 0
        for first in range(len(nums)):
            while last < len(nums) and nums[last] - nums[first] <= k:
                last +=1
            pairs_count += len(nums) - last
        
        return pairs_count
    
    
    print(solution(nums, 2))

# sum_of_pair()

def sum_of_players():
    pass

def merge_sorted_seq():

    def merge(seq1, seq2):
        
        l1, l2 = 0,0
        res = []
        while l1 <= len(seq1)-1 and l2 <= len(seq2)-1:
            if seq1[l1] <= seq1[l2]:
                res.append(seq1[l1])
                l1 +=1
            else:
                res.append(seq2[l2])
                l2 +=1
        
        if l1 <= len(seq1)-1:
            while l1 <= len(seq1)-1:
                res.append(seq1[l1])
                l1+=1
        
        if l2 <= len(seq2)-1:
            while l2 <= len(seq2)-1:
                res.append(seq2[l2])
                l2+=1

        return res
    
    seq1, seq2 = [1,3,5], [2,4,7]

    print(merge(seq1, seq2))

merge_sorted_seq()     





    







