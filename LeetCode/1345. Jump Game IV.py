from collections import deque
from typing import List, Dict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        added_numbers: Dict[int, set] = dict()

        for i in range(len(arr)):
            if arr[i] not in added_numbers:
                added_numbers[arr[i]] = set()
            added_numbers[arr[i]].add(i)

        #print(added_numbers)

        q = deque([0])
        visited = [False] * len(arr)
        visited[0] = True

        steps = 0

        while q:

            for _ in range(len(q)):
                curr = q.popleft()
                #print(str(curr) + " steps = " + str(steps))
                if curr == len(arr) - 1:
                    return steps

                if curr > 0 and visited[curr - 1] is False:
                    visited[curr - 1] = True
                    q.append(curr - 1)

                if curr < len(arr) - 1 and visited[curr + 1] is False:
                    visited[curr + 1] = True
                    q.append(curr + 1)

                if arr[curr] in added_numbers:
                    for i in added_numbers[arr[curr]]:

                        if visited[i] is False:
                            visited[i] = True
                            q.append(i)
                    del added_numbers[arr[curr]]

            steps += 1


x = Solution()

print(x.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
