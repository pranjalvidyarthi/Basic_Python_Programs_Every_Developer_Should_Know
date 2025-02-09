# Find the Most Frequent Element in a List
from collections import Counter
num = list(map(int, input('enter the numbers separated by spaces: ').split()))
most_common = Counter(num).most_common(1)[0]
print(f'Most frequent number: {most_common[0]} (appeared {most_common[1]} times)')