import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    print(rows)
   
    N = int(rows[0].split()[0])
    print('N :', N)
    
    vertices = []

    for r in range(1, N+1):
        print(rows[r])
        vertices.append(tuple(map(int,rows[r].split())))

    print(vertices)

    tracks = []
    for r in range(N+2, len(rows)):
        tracks.append(tuple(map(int,rows[r].split())))    
    
    print(tracks) 

    # Recreate serie 
    

    # for track in tracks:
    #     if track[0] < track[1]:
    #         l,r = track
    #         while vertices[]


if __name__ == '__main__':
    main()