import os
import sys
from collections import defaultdict
import math

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '7.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [tuple(map(int,r.split())) for r in rows]
        
    return rows

rows = get_rows()
