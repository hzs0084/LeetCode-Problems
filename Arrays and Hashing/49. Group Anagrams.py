class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) # The reason I use deafult dict because when you try to access or a modify a key that's not present in deafult dict, a default value is used, in this case it's a list

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count [ord(c) - ord("a")] += 1
            res [tuple(count)].append(s)
        return res.values()