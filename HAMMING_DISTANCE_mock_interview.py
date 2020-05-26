'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff_bits = x^y
        #print(diff_bits)
        num_1s = bin(diff_bits).count('1')
        #print(num_1s)
        return num_1s
         