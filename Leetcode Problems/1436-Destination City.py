class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        initial = []
        final = []
        for i in paths:
            initial.append(i[0])
            final.append(i[1])
        res = list(set(final) - set(initial))
        return res[0]
        
