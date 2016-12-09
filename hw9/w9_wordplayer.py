import sys


def main():
    inputCmd = sys.argv
    filewordlist = open(inputCmd[1])
    words = filewordlist.read()
    words = words.split('\n')
    N = len(words)
    matrix = [[0 for i in range(27)] for i in range(N)]
    for k in range(N):
        matrix[k][26] = len(words[k])
        for b in words[k]:
            index=ord(b) - ord('a')
            matrix[k][index] = matrix[k][index] + 1
    while(True):
        #cmd="ndarmo 5"
        cmd=input().split()  
        n = int(cmd[1])
        if n == 0:
            return 0
        result = []
        current = [0] * 26
        for b in cmd[0]:
            index=ord(b) - ord('a')
            current[index] = current[index] + 1
        for k in range(N):
            if n != matrix[k][26]:
                pass
            else:
                for tmp in range(26):
                    if  current[tmp] - matrix[k][tmp] < 0:
                        break
                    if tmp==25:
                        wo = words[k]
                        result.append(words[k])
        result.sort()
        for c in result:
            print(c)
        print('.')

if __name__ == '__main__':
    main()
