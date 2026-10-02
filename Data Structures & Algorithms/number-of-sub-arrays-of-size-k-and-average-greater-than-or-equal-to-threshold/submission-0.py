class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # Two pointer

        # L, R start at 0, 0
        # R - L + 1 == k

        # Increment R, increase by arr[R], sub my arr[L], L += 1
            # if currSum > thresh, total += 1

        currSum = 0
        total = 0
        L = 0

        for R in range(len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1
            currSum += arr[R]
            # print(currSum) # 11, 24, 41, 53, 69, 83, 67, 43, 14, 10
            if currSum / k >= threshold and R - L + 1 == k:
                # print("INCREASING TOTAL")
                total += 1
        
        return total
        