from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = "abc"
        #s2 = "lecabee"

        #len(s1) = 3
        # Maintain two frequency counts
        # count1 (characters in s1)
        # count2 the current window in s2

        #count1 = a:1, b:2, c:1
        # "lec" -> count2 = l:1, e:1, c:1
        # ^Not equal -> move the window forward
        # eca -> count2 = e:1, c:1, a:1 count2 != count1
        # "cab" -> count2= c:1, a:1, b:1 cuont2 == count1 -> True

        if len(s1) > len(s2): #Edge case 
            return False

        #build a freqneucy counter for `s1` w/ an array of size 26 (for lower case letters)
        count1 = Counter(s1) # Frequency counter for s1
        window = Counter() #Freqency counter for curr window in s2

        for i, ch in enumerate(s2):
            window[ch] += 1

            # Shrink window if size exceed len(s1)
            if i >= len(s1):
                leftChar = s2[i - len(s1)]
                window[leftChar] -= 1
                if window[leftChar] == 0:
                    del window[leftChar]

            #Compare counters
            if window == count1:
                return True
        return False
        #Fill count 1 w/ freqnencies of s1
        # for ch in s1:
        #     count1[ord(ch) - ord('a')] += 1 # Get index by ASCII Value

        #     # Shrink window if size exceeds len(s1)

        # # Sliding window of size len(s1) over s2 (similar freqnecy counter)
        # for i in range(len(s2)):
        #     count2[ord(s2[i]) - ord('a')] += 1

        #     if i >= len(s1):
        #         count2[ord(s2[i - len(s1)]) - ord('a')] -= 1 # Remove left most element from count

        #     if count1 == count2:
        #         return True
        # return False 
        # For each step, compare counters, if they match return True
        # Return false if there is no match



        