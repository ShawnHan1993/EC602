# AUTHOR Shen_Han shawnhan@bu.edu
# AUTHOR Changlong_Jiang cljiang@bu.edu
import sys


def w9_wordplayer():
    ws = open(sys.argv[1]).read().split()
    bD = {}
    for k in range(len(ws)):
        tmp = list(ws[k])
        tmp.sort()
        mK = str(tmp)
        bD.setdefault(len(ws[k]), {mK: []}).setdefault(mK, []).append(ws[k])
    while(True):
        cmd = input().split()
        n = int(cmd[1])
        if n == 0:
            return 0
        probab = list(cmd[0])
        probab.sort()
        result = []
        if len(cmd[0]) == n:
            result = bD.get(n, {}).get(str(probab), [])
        if len(cmd[0]) > n:
            cur = list(range(0, n))
            flag = 0
            while(flag == 0):
                curMat = [' '] * n
                for jj in range(n):
                    curMat[jj] = probab[cur[jj]]
                curMat = str(curMat)
                result = (bD.get(n, {}).get(curMat, [])) + result
                for i in range(n - 1, -1, -1):
                    stop = len(probab) - n + i
                    tmp = cur[i]
                    cur[i] = stop + 1
                    while(tmp < stop):
                        tmp = tmp + 1
                        if probab[tmp] != probab[tmp - 1]:
                            cur[i] = tmp
                            break
                    if cur[i] > stop:
                        if i == 0:
                            flag = 1
                            break
                        continue
                    for kk in range(i + 1, n):
                        cur[kk] = cur[kk - 1] + 1
                    break
        result.sort()
        for c in result:
            print(c)
        print('.')

w9_wordplayer()
