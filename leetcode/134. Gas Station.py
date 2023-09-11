class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        dif = []

        for i in range(len(gas)):
            dif.append(gas[i] - cost[i])
        
        max_val = float('-inf')
        max_idx = 0

        for i in range(len(dif)):
            if dif[i] > max_val:
                max_val = dif[i]
                max_idx = i

        print('dif :', dif)

        cur_gas = gas[max_idx]
        cur_pos = max_idx
        counter = 0
        while counter < len(gas):
            
            next_pos = cur_pos+1 if cur_pos < len(gas)-1 else 0
            cur_gas = cur_gas - cost[cur_pos] + gas[next_pos] 

            cur_pos = next_pos

            if cur_gas < 0:
                return -1
            
            counter +=1

        return max_idx