from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = defaultdict(list)
        i = 0
        while i < len(strs):
            counter = Counter(strs[i])
            unique_id = counter_to_unique(counter)
            mymap[unique_id].append(strs[i])
            i += 1
        ans = map_to_list(mymap)
        return ans
        
def counter_to_unique(counter: Counter) -> str:
    ans = ""
    keys = list(counter.keys())
    keys.sort()
    for key in keys:
        count = counter[key]
        ans += count * key
    return ans 

def map_to_list(mymap: Dict[str, List[str]]) -> List[List[str]]:
    ans = []
    for group in mymap.values():
        ans.append(group)
    return ans