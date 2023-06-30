from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def splitFilePaths(filePath):
            dirAndFiles= filePath.split(" ")
            files = []

            for file in dirAndFiles[1:]:
                files.append(dirAndFiles[0]+"/" + file)
            return files

        files = defaultdict(list)
        for path in paths:
            path = splitFilePaths(path)
            for filePath in path:
                splitFile = filePath.split("(")
                content = splitFile[1][: len(splitFile[1]) - 1]
                filePath = splitFile[0]
                files[content].append(filePath)
        files = list(files.values())
        files = [f for f in files if len(f) > 1]
        return files
