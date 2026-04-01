class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            (found, j) = binary_search(i, numbers[(i + 1):], target - numbers[i])
            if found:
                return [i + 1, j + 1]
            i += 1
        return []

def binary_search(i: int, remains: List[int], remain: int) -> Tuple[bool, int]:
    ng = -1
    ok = len(remains)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if remains[mid] >= remain:
            ok = mid
        else:
            ng = mid
    if ok == len(remains):
        return (False, -1)
    elif remains[ok] != remain:
        return (False, -1)
    else:
        return (True, i + ok + 1)