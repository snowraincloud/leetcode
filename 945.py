import math

class Solution:
    def minIncrementForUnique(self, A: list) -> int:
        if len(A) == 0:
            return 0
        a_max = max(A)
        count_list = (a_max + 1) * [0]
        for num in A:
            count_list[num] += 1

        plural_count = 0
        plural_sum = 0
        empty_sum = 0
        for i in range(len(count_list)):
            if count_list[i] > 1:
                plural_count += count_list[i] - 1
                plural_sum += (count_list[i] - 1) * i
            elif plural_count > 0 and count_list[i] == 0:
                plural_count -= 1
                empty_sum += i
        if plural_count == 1:
            empty_sum += a_max + 1
        elif plural_count != 0:
            # empty_sum += (plural_count * (a_max*2 + plural_count + 1)) / 2
            empty_sum += plural_count * a_max + \
                (plural_count * plural_count + plural_count) / 2

        return int(empty_sum - plural_sum)

    def b_minIncrementForUnique(self, A: list) -> int:
        mark=0
        anw=0
        for i in A:
            if mark&1<<i!=0:
                tmp1=mark+(1<<i)
                tmp2=~mark
                tmp1=tmp1&tmp2
                num=int(math.log2(tmp1))
                anw+=num-i
                i=num
            mark+=1<<i
        return anw


if __name__ == "__main__":
    solution = Solution()
    res = solution.b_minIncrementForUnique([3,2,1,2,1,7])
    print(res)
