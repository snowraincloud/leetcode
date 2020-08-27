from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        ticket_map = defaultdict(list)
        for ticket in tickets:
            ticket_map[ticket[0]].append([ticket[1], True])
        for _, to in ticket_map.items():
            to.sort()
        ans = []
        l = len(tickets)
        ans.append("JFK")
        def backtrack(i) -> bool:
            if i == l:
                return True
            if ticket_map[ans[-1]]:
                for to in ticket_map[ans[-1]]:
                    if to[1]:
                        ans.append(to[0])
                        to[1] = False
                        if backtrack(i+1):
                            return True
                        ans.pop()
                        to[1] = True
            return False
        backtrack(0)
        return ans 
    # 这种「一笔画」问题与欧拉图或者半欧拉图有着紧密的联系，下面给出定义：

    # 通过图中所有边恰好一次且行遍所有顶点的通路称为欧拉通路。

    # 通过图中所有边恰好一次且行遍所有顶点的回路称为欧拉回路。

    # 具有欧拉回路的无向图称为欧拉图。

    # 具有欧拉通路但不具有欧拉回路的无向图称为半欧拉图。

    # 因为本题保证至少存在一种合理的路径，也就告诉了我们，这张图是一个欧拉图或者半欧拉图。我们只需要输出这条欧拉通路的路径即可。

    # 如果没有保证至少存在一种合理的路径，我们需要判别这张图是否是欧拉图或者半欧拉图，具体地：

    # 对于无向图 GG，GG 是欧拉图当且仅当 GG 是连通的且没有奇度顶点。

    # 对于无向图 GG，GG 是半欧拉图当且仅当 GG 是连通的且 GG 中恰有 22 个奇度顶点。

    # 对于有向图 GG，GG 是欧拉图当且仅当 GG 的所有顶点属于同一个强连通分量且每个顶点的入度和出度相同。

    # 对于有向图 GG，GG 是半欧拉图当且仅当 GG 的所有顶点属于同一个强连通分量且

    # 恰有一个顶点的出度与入度差为 11；

    # 恰有一个顶点的入度与出度差为 11；

    # 所有其他顶点的入度和出度相同。

    # Hierholzer 算法用于在连通图中寻找欧拉路径，其流程如下：

    # 从起点出发，进行深度优先搜索。

    # 每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。

    # 如果没有可移动的路径，则将所在节点加入到栈中，并返回。

    # 当我们顺序地考虑该问题时，我们也许很难解决该问题，因为我们无法判断当前节点的哪一个分支是「死胡同」分支。

    # 不妨倒过来思考。我们注意到只有那个入度与出度差为 11 的节点会导致死胡同。而该节点必然是最后一个遍历到的节点。我们可以改变入栈的规则，当我们遍历完一个节点所连的所有节点后，我们才将该节点入栈（即逆序入栈）。

    # 对于当前节点而言，从它的每一个非「死胡同」分支出发进行深度优先搜索，都将会搜回到当前节点。而从它的「死胡同」分支出发进行深度优先搜索将不会搜回到当前节点。也就是说当前节点的死胡同分支将会优先于其他非「死胡同」分支入栈。

    # 这样就能保证我们可以「一笔画」地走完所有边，最终的栈中逆序地保存了「一笔画」的结果。我们只要将栈中的内容反转，即可得到答案

    # 作者：LeetCode-Solution
    # 链接：https://leetcode-cn.com/problems/reconstruct-itinerary/solution/zhong-xin-an-pai-xing-cheng-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def findItineraryBetter(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = list()
        dfs("JFK")
        return stack[::-1]
        

if __name__ == "__main__":
    s = Solution()
    print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))