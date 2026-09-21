class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3, 4, 5, 6, 1, 2], target = 1
        # binary search modified to handle the rotation
        #L, R = 0, 5
        # mid = (0 + 5) // 2 = 2 -> nums[mid] = 5
        # nums[left] = 3, nums[mid] = 5
            # This tells me the left half is sorted
        # Target is 1 so discard left half bc not btwn 3 and 5
        #Mid (3 + 5) // 2 = 4 -> nums[mid] = 1
        # nums[mid] == target
            # Return mid -> 4
            
        # Use binary search w/ two pointers, `l`, `r`
        l, r = 0, len(nums) - 1

        # [3, 5, 6, 0, 1, 2], target = 4
        while l <= r:
        #@ each step, compute `mid` mid = (l + r) // 2
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # check right half
                else:
                    r = mid - 1 # check left half
        return -1
            # Check which half (left to mid or right to mid is sorted)
            # If the target lies with the sorted half
                # Move the other pointer inwards to search that half
            # Otherwise
                # Discard, search the unsorted half
        
        