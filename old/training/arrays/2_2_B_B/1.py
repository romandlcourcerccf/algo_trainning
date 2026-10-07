import os

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    nums = list(map(int, rows[0].split()))
    
    print(nums)

    left_max_array = [0] * len(nums)
    left_max = 0
    for i in range(len(nums)):
        if nums[i] == 2:
            left_max = 0
        elif nums[i] == 1:
            left_max_array[i] = left_max
        
        left_max +=1
    
    print(left_max_array)
   
    right_max_array = [0] * len(nums)
    right_max = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 2:
            right_max = 0
        elif nums[i] == 1:
            right_max_array[i] = right_max
        
        right_max +=1

    print(right_max_array)
    
    max_array = [0] * len(nums)

    for i in range(len(nums)):
        if nums[i] == 1:
            max_array[i] = min(right_max_array[i], left_max_array[i])

    print(max(max_array))

if __name__ == '__main__':
    main()