class Solution():
    def findLadders(self, beginWord, endWord, wordList):
        # edge case

        wordList = set(wordList)
        wordList.add(endWord)

        levels = {}
        levels[beginWord] = 1
        parent = {}

        result = []

        queue = [beginWord]
        wordLen = len(beginWord)
        currLevel = 0
        found = False

        while len(queue) > 0 and not found:
            currLevel += 1
            currWord = queue[0]
            del queue[0]
            for i in range(wordLen):
                left = currWord[:i]
                right = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != currWord[i]:
                        nextWord = left + j + right
                        if nextWord == endWord:
                            parent[nextWord].append(currWord)
                            found = True
                        else:
                            # Not a new word, but another transformation in the SAME LEVEL
                            if nextWord in levels and currLevel < levels[nextWord]:
                                parent[nextWord].append(currWord)

                    if nextWord not in wordList:
                        continue
                    wordList.remove(nextWord)
                    queue.append(nextWord)
                    levels[nextWord] = levels[currWord] + 1
                    parent[nextWord].append(currWord)

                nextWord = currWord

        # TODO: build path using DFS
        return result


class Solution1():
    def findLadders(self, start, end, dict):
        dict.append(start)
        dict.append(end)

        def buildPath(path, word):
            if len(preMap[word]) == 0:
                result.append([word] + path)
                return

            path.insert(0, word)
            for w in preMap[word]:
                buildPath(path, w)
            path.pop(0)


        length = len(start)
        preMap = {}
        for word in dict:
            preMap[word] = []
        result = []
        curr_level = set()
        curr_level.add(start)

        while True:
            pre_level = curr_level
            curr_level = set()
            for word in pre_level:
                dict.remove(word)
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i+1:]
                    for c in 'abcdefghijklmnokpqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in dict:
                                preMap[nextWord].append(word)
                                curr_level.add(nextWord)
            if len(curr_level) == 0:
                return []
            if end in curr_level:
                break

        buildPath([], end)
        return result

if __name__ == "__main__":
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
    sln = Solution1()
    result = sln.findLadders(start, end, dict)
    print(result)