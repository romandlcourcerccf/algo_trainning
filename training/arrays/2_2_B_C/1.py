import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "3.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    word = rows[0]

    if len(word) == 1:
        print(0)
        return

    counter = 0
    if len(word) % 2  == 0:
        pos1 = len(word) // 2-1
        pos2 = len(word) // 2 
        if word[pos1] != word[pos2]:
            counter +=1
        
        while pos1 > 0:

            pos1 -=1
            pos2 +=1

            if word[pos1] != word[pos2]:
                counter +=1

    elif len(word) % 2  != 0:
        pos = len(word) // 2

    
        pos1 = pos-1
        pos2=  pos+1

        if word[pos1] != word[pos2]:
                counter +=1


        # print(' >> ', word[pos1] ,  word[pos2])

        while pos1 > 0:

            print(' >> ', word[pos1] ,  word[pos2])
            if word[pos1] != word[pos2]:
                counter +=1

            pos1 -=1
            pos2 +=1


    print(counter)

    
   
   
    


   

if __name__ == '__main__':
    main()