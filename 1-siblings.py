'''
Find a number in an array of numbers by adding K th elemment with K th element and return the K th largest number.

Note:

    1. The K th largest number must an absolute number.
    2. If the sum is already present in the array then add the number to K th value
    3. Negative values will also be passed as input.
    
Example: [4, 1, 2, 12, 7, 3],2

Root element is 1(minimum),
Here K=2 (It was the index value)

The number K th i.e (2-1)th largest number: (2-1 is the index and 2 is the position in array)
1+1 = 2
2 is already present so let's add 2+1=3
3 is already present so let's add 3+1=4
4 is already present so let's add 4+1=5

Hence, the answer is 5

Input Format

Computer generated input of array A[i] and position K (Getting using map)

Constraints

0 ≤ k ≤ 100

Output Format:

    Absolute number  (important point)

Sample Input 0

-4 -1 -2 -12 -7 -3 4 1 2 12 7 3
2
Sample Output 0

5
Sample Input 1

3 2 1 4 5 6
1
Sample Output 1

9
'''
class Solution():
    def sibling(self):
        #getting the single line input with space seperated values and changing to list
        arr = list(map(int, input().split()))
        #getting the index value
        k = int(input())
        #picking the arr value ofor the particular index for further use
        k_val = arr[k-1]
        #adding the k_val 2 times for the k_lar value
        k_lar = k_val+k_val
        '''
            if k_val in the arr again we need to add the k_val for next k_lar value
            else we can end the loop and we return the value
        '''
        while k_lar in arr:
            k_lar = k_lar + k_val
        return(abs(k_lar))

#main
if __name__ == '__main__':
    #creating the class
    sol = Solution()
    #calling the function and printing he result
    print(sol.sibling())
    