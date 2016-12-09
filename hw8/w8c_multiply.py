from numpy import *
import sys
def file2Mat(fileA,fileB,eletype,N,M,L):
    A=empty([M,N],dtype=eletype)
    B=empty([N,L],dtype=eletype)
    try:
        for i in range(M):
            newline=fileA.readline()
            newline=newline.split()
            for j in range(N):
                if eletype==float:
                    A[i,j]=float(newline[j])
                else:
                    A[i,j]=int(newline[j])
        
        for i in range(N):
            newline=fileB.readline()
            newline=newline.split()
            for j in range(L):
                if eletype==float:
                    B[i,j]=float(newline[j])
                else:
                    B[i,j]=int(newline[j])
        
        C=dot(A,B)
        return A,B,C
    except:
        sys.exit(3)
            
def main():
    inputCmd=sys.argv
    numCmd=len(sys.argv)
    A=0
    B=0
    C=0
    if numCmd==8 or numCmd==6:
        pass
    else:
        sys.exit(0)  
    if sys.argv[1]=="int" or sys.argv[1]=="double":
        pass
    else:
        sys.exit(1)  
    if numCmd==6:
        try:
            N=int(sys.argv[2])
            M=N;
            L=N;
        except:
            sys.exit(1)
        try:
            fileA=open(sys.argv[3])
            fileB=open(sys.argv[4])
        except:
            sys.exit(2)
        global A,B,C
        A,B,C=file2Mat(fileA,fileB,int,N,M,L)
    else:
        try:
            M=int(sys.argv[2])
            N=int(sys.argv[2])
            L=int(sys.argv[2])
        except:
            sys.exit(1)
        try:
            fileA=open(sys.argv[5])
            fileB=open(sys.argv[6])
        except:
            sys.exit(2)
        global A,B,C  
        A,B,C=file2Mat(fileA,fileB,float,N,M,L)
    
    try:
        fileC=open(argv[numCmd-1],"w")
    except:
        sys.exit(2)

    writeContent=''
    for i in range(M):
        for j in range(L):
            writeContent+=str(C[i,j])
            if j==L-1:
                writeContent+=' '
            else:
                writeContent+='\n'

    fileC.write(writeContent) 
    fileC.close()
    
if __name__=="__main__":
    main();
