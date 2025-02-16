#  Find the Mode (Most Frequent Element)
from collections import Counter
numbers = [1,2,2,3,3,3,4]
mode = Counter(numbers).most_common(1)[0][0]
print('Mode: ', mode)
