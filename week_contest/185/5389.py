from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        orders = sorted(orders, key=lambda x:int(x[1]))
        foots = set()
        customer = dict()
        for order in orders:
            foots.add(order[2])
            if not customer.get(order[1]):
                customer[order[1]] = dict()
                customer[order[1]][order[2]] = 1
            else:
                if not customer[order[1]].get(order[2]):
                    customer[order[1]][order[2]] = 1
                else:
                    customer[order[1]][order[2]] += 1
        foots = sorted(list(foots))
        customer = sorted(customer.items(), key=lambda x:int(x[0]))
        res = []
        temp = ['Table']
        temp.extend(foots)
        res.append(temp)
        for c in customer:
            temp = [c[0]]
            for foot in foots:
                if foot in c[1]:
                    temp.append(str(c[1][foot]))
                else:
                    temp.append("0")
            res.append(temp)
        return res

    def displayTableA(self, orders: List[List[str]]) -> List[List[str]]:
        import collections
        orders = sorted(orders, key=lambda x:int(x[1]))
        foots = set()
        customer = dict()
        for order in orders:
            foots.add(order[2])
            if not customer.get(order[1]):
                customer[order[1]] = collections.defaultdict(int)
            customer[order[1]][order[2]] += 1
        foots = sorted(list(foots))
        customer = sorted(customer.items(), key=lambda x:int(x[0]))
        res = []
        temp = ['Table']
        temp.extend(foots)
        res.append(temp)
        for c in customer:
            temp = [c[0]]
            for foot in foots:
                if foot in c[1]:
                    temp.append(str(c[1][foot]))
                else:
                    temp.append("0")
            res.append(temp)
        return res

if __name__ == "__main__":
    solution = Solution()
    res = solution.displayTableA([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]])
    print(res)