from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l = len(rooms)
        if l < 2:
            return True
        ans = [False] * l
        def dfs(n):
            ans[n] = True
            for i in rooms[n]:
                if not ans[i]:
                    dfs(i)
        dfs(0)
        return all(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))