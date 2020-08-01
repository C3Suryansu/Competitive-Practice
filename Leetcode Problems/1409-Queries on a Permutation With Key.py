class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        actual = [i+1 for i in range(m)]
        for i in range(len(queries)):
            val = actual.index(queries[i])
            res.append(val)
            del actual[val]
            actual.insert(0, queries[i])
        return res
