# AUTHOR Shen_Han shawnhan@bu.edu
# AUTHOR Changlong_Jiang cljiang@bu.edu
import json
import copy

def insertWord(i, word, bD):
    if i == len(word) - 1:
        bD.setdefault(word[i], {})['exist'] = True
    else:
        insertWord(i + 1, word, bD.setdefault(word[i], {}))


def buildConnection(strMaze, n):
    connection = [0] * (n ** 2)
    for i in range(n ** 2):
        connection[i] = [False] * (n ** 2)
    for i in range(len(strMaze)):
        if strMaze[i] == '0':
            continue
        col = i // n
        row = i % n
        if row != 0:
            connection[i][i - 1] = True and strMaze[i - 1] != '0'
            if col != 0:
                connection[i][i - n - 1] = True  and strMaze[i - n - 1] != '0'
            if col != n - 1:
                connection[i][i + n - 1] = True and strMaze[i + n - 1] != '0'
        if row != n - 1:
            connection[i][i + 1] = True and strMaze[i + 1] != '0'
            if col != 0:
                connection[i][i - n + 1] = True and strMaze[i - n + 1] != '0'
            if col != n - 1:
                connection[i][i + n + 1] = True and strMaze[i + n + 1] != '0'
        if col != 0:
            connection[i][i - n] = True and strMaze[i - n] != '0'
        if col != n - 1:
            connection[i][i + n] = True and strMaze[i + n] != '0'
    return connection

def searchWord(i, counter, m, strMaze, connect, bD, result, unVist, curW):
    if strMaze[i] in bD:
        unVist[i] = False
        curW = curW + chr(i)
        if counter == m - 1:
            if 'exist' in bD[strMaze[i]]:
                result.append(curW)
            return
        for it in range(len(strMaze)):
            if connect[i][it] and unVist[it]: 
                searchWord(it, counter + 1, m, strMaze, connect, bD[strMaze[i]], result, unVist, curW)
                unVist[it] = True

def dropDown(strMaze, preRe, n):
    for i in preRe:
        strMaze[ord(i)] = '0'
    for j in range(n):
        for k in range(n):
            flag = False
            for i in range(n - 1, k - 1, - 1):
                if strMaze[j * n + i] == '0':
                    flag = True
                if strMaze[j * n + i] != '0' and flag:
                    strMaze[j * n + i], strMaze[j * n + i + 1] = strMaze[j * n + i + 1], strMaze[j * n + i]


def searchSolution(searchDeep, strMazeC, connectionC, bD, curSoluC, solution):
    for start in range(len(strMazeC)):
        if strMazeC[start] == '0':
            continue
        result = []
        unVistited = [True] * (n ** 2)
        searchWord(start, 0, lengths[searchDeep], strMazeC, connectionC, bD, result, unVistited, '')
        for nextWordInx in result:
            nextWord = ''
            curSolu = curSoluC
            for i in nextWordInx:
                nextWord = nextWord + strMazeC[ord(i)]
            curSolu = curSolu + ' ' + nextWord
            if searchDeep == len(lengths) - 1:
                solution.append(curSolu)
            else:
                strMaze = strMazeC[:]
                connection = [0] * len(strMaze)
                dropDown(strMaze, nextWordInx, n)
                connection = buildConnection(strMaze, n)
                searchSolution(searchDeep + 1, strMaze, connection, bD, curSolu, solution)


ws = open('small_word_list.txt').read().split()
ws2 = open('large_word_list.txt').read().split()
bD = {}
for word in ws:
    insertWord(0, word, bD)
bbD = {}
for word in ws2:
    insertWord(0, word, bbD)
inputFile = open('puzzles.txt')
answer = open('solutions.txt', 'w')
while(True):
    '''
    json_str = inputFile.readline()
    if json_str == '\n':
        break
    json_line = json.loads(json_str)
    strMaze = list(''.join(e for e in json_line['grid']))
    lengths = json_line['lengths']
    n = json_line['size']
    '''
    strMaze=list(input('the letters: '))
    n = int(input('the size: '))
    lengths=list(input('the length: '))
    for i in range(len(lengths)):
        lengths[i] = int(lengths[i])
    solution = []
    connection = buildConnection(strMaze, n)
    searchSolution(0, strMaze, connection, bD, '', solution)
    if len(solution) == 0:
        searchSolution(0, strMaze, connection, bbD, '', solution)
    for i in range(len(solution)):
        solution[i] = solution[i][1:len(solution[i])]
    solution = list(set(solution))
    solution.sort()
    solution = '\n'.join(e for e in solution)
    #answer.write(solution)
    #answer.write('.')
    print(solution)
    print('.')
