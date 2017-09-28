class CheckPython:
    def __init__(self, fileName):
        self.fileName = fileName
        self.indent = 4

    def checkPython(self):
        with open(self.fileName, 'r') as f:
            stack = []
            indent, lastIndent = 0, 0
            lastColon = False
            for line in f:
                indent = 0
                for i in xrange(len(line)):
                    if line[i] == ' ':
                        indent += 1
                        continue
                    else:
                        break
                if abs(indent - lastIndent) % self.indent != 0:
                    return False
                if line[-1] == ':':
                    lastColon = True
                    lastIndent = indent
                    continue
                if lastColon:
                    if indent != (lastColon + self.indent):
                        return False
                lastIndent = indent
        return True

cp = CheckPython('ListInsideList.py')
print cp.checkPython()
