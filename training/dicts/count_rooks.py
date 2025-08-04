def count_rooks(coords):

    def add_rook(rowcol, key):
        rowcol[key] +=1
    
    def pairs_count(rowcol):
        pairs = 0 
        for k in rowcol:
            