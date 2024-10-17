'''
Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
input_values = input()
values_list = list(map(int, input_values.split()))
max_value = max(values_list)
min_value = min(values_list)
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
