class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        h1, h2 = {}, {}

        for n in nums1:
            if n not in h1:
                h1[n]=1
            else:
                h1[n]+=1
        
        for n in nums2:
            if n not in h2:
                h2[n]=1
            else:
                h2[n]+=1

        res = []
        
        used = set()

        for n in nums1:
            if n in h1 and n in h2 and n not in used:
                used.add(n)
                for i in range(min(h1[n], h2[n])):
                    res.append(n)
        
        print(used)

        for n in nums2:
            if n in h1 and n in h2 and n not in used:
                used.add(n)
                for i in range(min(h1[n], h2[n])):
                    print('>> ', n)
                    res.append(n)

        return res