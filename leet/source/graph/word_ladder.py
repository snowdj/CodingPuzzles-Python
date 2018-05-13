# BFS
## Search every "layer"
def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        wordLen = len(start)
        queue = [(start, 1)]
        while len(queue) > 0:
            curr = queue[0]
            del queue[0]
            currWord = curr[0]
            currLen = curr[1]
            if currWord == end:
                return currLen
            for i in range(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in dict:
                            queue.append((nextWord, currLen+1))
                            dict.remove(nextWord)
        return 0


# Bi-directional BFS
