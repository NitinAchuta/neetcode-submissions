class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        anagramList = []

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in hash:
                hash[sortedWord] = len(hash)
                anagramList.append([word])
            else:
                anagramList[hash[sortedWord]].append(word)
        
        return anagramList


        
        



        