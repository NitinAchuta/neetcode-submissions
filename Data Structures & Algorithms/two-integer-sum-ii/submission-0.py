class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        val = numbers[l] + numbers[r]
        while val != target:
            if val > target:
                r -= 1
            if val < target:
                l += 1
            val = numbers[l] + numbers[r]

        return [l+1, r+1]
            
        