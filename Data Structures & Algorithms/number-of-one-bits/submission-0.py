class Solution:
    def hammingWeight(self, n: int) -> int:

        nBinary = str(bin(n)[2:])

        acc = 0
        for n in nBinary:
            if n == "1":
                acc += 1
        return acc

        