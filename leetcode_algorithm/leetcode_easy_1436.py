# 20200928
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for pair in paths:
            d[pair[0]] = pair[1]
        for k in d.keys():
            if d[k] not in d:
                return d[k]

# 20230930
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        origin = set([p[0] for p in paths])
        for p in paths:
            if p[1] not in origin:
                return p[1]

# 20231007
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        origins = set(p[0] for p in paths)
        for p in paths:
            if p[1] not in origins:
                return p[1]
