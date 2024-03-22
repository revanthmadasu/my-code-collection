'''
    problem: https://leetcode.com/problems/longest-absolute-file-path/
    concepts: recursion, backtracking, dfs
    performance: 9.53% runtime, 80.58% memory
'''
import re
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        nodes = input.split('\n')

        def getFilePaths(tCount, start):
            paths = []
            lastPath = None
            i = start
            while i < len(nodes):
                curTc = len(re.findall('\t', nodes[i]))
                nodeName = nodes[i].replace('\t', '')
                if curTc == tCount:
                    if '.' not in nodeName:
                        lastPath = nodeName
                    else:
                        paths.append(nodeName)
                    i += 1
                elif curTc > tCount:
                    i, subDirPaths = getFilePaths(curTc, i)
                    # if lastPath in paths:
                    #     paths.remove(lastPath)
                    paths.extend([lastPath+'/'+subDirPath for subDirPath in subDirPaths])
                elif curTc < tCount:
                    return (i, paths)
            return (i, paths)
        i, filepaths = getFilePaths(0, 0)
        # print(filepaths)

        return max([len(filepath) for filepath in filepaths]) if len(filepaths) else 0
