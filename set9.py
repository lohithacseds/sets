''''
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
num_values = int(input())
values_list = []
for i in range(num_values):
    value = int(input())
    values_list.append(value)
duplicate_count = len(values_list) - len(set(values_list))
print(f"Duplicate Values: {duplicate_count}")
unique_values = list(set(values_list))
unique_values.sort()
print(' '.join(map(str, unique_values)))
