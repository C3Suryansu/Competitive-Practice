class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sol = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in sol:
                sol[groupSizes[i]] = [i]
            else:
                sol[groupSizes[i]].append(i)
        res = []
        for key in sol:
            val = sol[key]
            temp = []
            for i in range(len(val)):
                temp.append(val[i])
                if (i + 1) % key == 0:
                    res.append(temp)
                    temp = []
        return res
        
