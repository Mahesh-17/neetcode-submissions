class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        # for word in strs:
        #     key = "".join(sorted(word))
        #     groups[key].append(word)
        # return list(groups.values())
        groups = defaultdict(list)
        for word in strs:
            str1 = [0]*26
            for cnt in word:
                str1[ord(cnt)-ord('a')] += 1
            groups[(tuple(str1))].append(word)
        return list(groups.values())

        