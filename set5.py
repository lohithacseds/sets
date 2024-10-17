''''
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''
input_set1 = input()
input_set2 = input()
set1 = set(map(int, input_set1.split()))
set2 = set(map(int, input_set2.split()))
common_values = set1.intersection(set2)
sorted_values = ' '.join(map(str, sorted(common_values)))
print(sorted_values + ' ')
