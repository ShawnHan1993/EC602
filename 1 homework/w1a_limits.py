# AUTHOR ShenHan shawnhan@bu.edu
# AUTHOR ChanglongJiang cljiang@bu.edu
def calcu(numOfBytes,outType):
    return{
        'LU':int(2**(8*numOfBytes)-1),
        'MS':int((-2**(8*numOfBytes))/2),
        'MU':0,
        'LS':int((2**(8*numOfBytes))/2)-1,
    }[outType]
    
Table="{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes', 'Largest Unsigned Int', 'Minimum Signed Int', 'Maximum Signed Int'))
for i in range(0,4):
    #print(Table2.format(2**i,int(2**(8*(2**i))-1),int(-(2**(8*(2**i)))/2),int((2**(8*(2**i)))/2-1)))
    print(Table.format(2**i,calcu(2**i,'LU'),calcu(2**i,'MS'),calcu(2**i,'LS')))
