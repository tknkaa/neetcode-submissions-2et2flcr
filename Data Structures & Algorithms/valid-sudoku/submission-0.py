from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        columns = [[] for _ in range(n)]
        rows = [[] for _ in range(n)]
        squares = [[] for _ in range((n//3)**2)]
        for i in range(0, n):
            for j in range(0, n):
                columns[j].append(board[i][j])
                rows[i].append(board[i][j])
                squares[(i // 3) * (n // 3) + (j // 3)].append(board[i][j])
        check_list = columns + rows + squares
        for target_list in check_list:
            if not check(target_list):
                return False
        return True

def check(target_list: List[str]) -> bool:
    count = defaultdict(int)
    for target in target_list:
        if target == '.':
            continue
        else:
            count[target] += 1
            if count[target] == 2:
                return False
    return True

        

        