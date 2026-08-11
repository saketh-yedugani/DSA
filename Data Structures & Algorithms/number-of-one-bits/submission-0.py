class Solution:
    def hammingWeight(self, n: int) -> int:
        K = bin(n).count("1")
        return K