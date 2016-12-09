# AUTHOR ShenHan shawnhan@bu.edu
# AUTHOR ChanglongJiang cljiang@bu.edu

Table = "{:<6} {:<22} {:<22} {:<22}"

def Largest_Unsigned_Int(bytes):
    result = 2**(8*bytes)-1
    return result

def Minimum_Signed_Int(bytes):
    result = -2**(8*bytes-1)
    return result

def Maximum_Signed_Int(bytes):
    result = 2**(8*bytes-1)-1
    return result


print(Table.format('Bytes', 'Largest Unsigned Int', 'Minimum Signed Int', 'Maximum Signed Int'))
print(Table.format(1, Largest_Unsigned_Int(1), Minimum_Signed_Int(1), Maximum_Signed_Int(1)))
print(Table.format(2, Largest_Unsigned_Int(2), Minimum_Signed_Int(2), Maximum_Signed_Int(2)))
print(Table.format(4, Largest_Unsigned_Int(4), Minimum_Signed_Int(4), Maximum_Signed_Int(4)))
print(Table.format(8, Largest_Unsigned_Int(8), Minimum_Signed_Int(8), Maximum_Signed_Int(8)))