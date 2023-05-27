if __name__ == '__main__':
    N = int(input())
    operations = []
    result    = []
    
    while N > 0:
        line = input()
        line = line.split(" ")
        operations.append(line)
        N -= 1
    
    def operation(line):
        n = len(line)
        
        if n == 3:
            result.insert(int(line[1]), int(line[2]))
        elif n == 2:
            if line[0] == "remove":
                result.remove(int(line[1]))
            else:
                result.append(int(line[1]))
        else:
            if line[0] == "sort":
                result.sort()
            elif line[0] == "print":
                print(result)
            elif line[0] == "pop":
                result.pop()
            elif line[0] == "reverse":
                result.reverse()
    for op in operations:
        operation(op)
                
            
        