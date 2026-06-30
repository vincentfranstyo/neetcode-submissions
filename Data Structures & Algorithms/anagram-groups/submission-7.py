class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for word in strs:
            wordArr = [0] * 26

            for c in word:
                wordArr[ord(c) - ord('a')] += 1
            
            key = tuple(wordArr)
            strMap[key].append(word)
        
        res = []
        for val in strMap.values():
            res.append(val)
        
        # print(strMap.values())
        # print(type(strMap.values()))
        # print(type([strMap.values()]))
        
        return res