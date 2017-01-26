"""
Calculate Euclidean Distance in 2-Dimensional Space
"""

import math
from itertools import combinations

list1 = [(4, 10), (5, 9), (8, 7), (9, 6), (8, 3), (6, 15)]


[(math.sqrt((y1-x1)**2 + (y2-x2)**2)) for (x1, x2), (y1, y2) in combinations(list, 2)]

