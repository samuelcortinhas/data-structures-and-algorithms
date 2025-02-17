class Solution:
    # Too slow...
    def numTilePossibilities(self, tiles: str) -> int:
        # Time O(n^n), Memory O(n!)
        res = set()

        def backtrack(stack, visit, i):
            if i == len(tiles):
                if stack:
                    res.add("".join(stack))
                return

            for j in range(len(tiles)):
                # add tiles[j]
                if j not in visit:
                    visit.add(j)
                    stack.append(tiles[j])
                    backtrack(stack, visit, i + 1)
                    stack.pop()
                    visit.remove(j)

                # don't add tiles[j]
                backtrack(stack, visit, i + 1)

        backtrack([], set(), 0)
        return len(res)
