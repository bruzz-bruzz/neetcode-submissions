class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r,c,g = defaultdict(list),defaultdict(list),defaultdict(list)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] != '.':
                    r[x].append(board[x][y])
                    c[y].append(board[x][y])
                    grid = ((x // 3) * 3) + (y // 3)
                    g[grid].append(board[x][y])
        for x in range(9):
            if len(set(r[x])) != len(r[x]):
                return False
            if len(set(c[x])) != len(c[x]):
                return False
            if len(set(g[x])) != len(g[x]):
                return False
        return True