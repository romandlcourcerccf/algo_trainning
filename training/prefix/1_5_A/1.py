import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row_1 = list(map(int, rows[1].split()))
    row_2 = list(map(int, rows[3].split()))


    pos_1 = pos_2 = 0
    min_dist = float('inf')
    min_pos_1 = min_pos_2 =  0

    while pos_1 <= len(row_1)-1 and  pos_2 <= len(row_2)-1:

        if abs(row_1[pos_1] - row_2[pos_2]) <=  min_dist:
            min_dist = abs(row_1[pos_1] - row_2[pos_2])
            min_pos_1 , min_pos_2 = pos_1, pos_2


        if row_1[pos_1] == row_2[pos_2]:
            print(row_1[pos_1],' ', row_2[pos_2])
            return
        elif row_1[pos_1] < row_2[pos_2]:
            if pos_1 == len(row_1)-1:
                break

            pos_1 +=1
        else:
            if pos_2 == len(row_2)-1:
                break
            pos_2 +=1

    print(row_1[min_pos_1],' ', row_2[min_pos_2])
        


if __name__ == '__main__':
    main()