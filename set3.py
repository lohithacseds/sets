''''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
''''
input_set1 = input()
input_set2 = input()
set1 = set(map(int, input_set1.split()))
set2 = set(map(int, input_set2.split()))
different_values = set1.symmetric_difference(set2)
sorted_values = ' '.join(map(str, sorted(different_values)))
print(sorted_values + ' ')
