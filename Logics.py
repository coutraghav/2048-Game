import random
def startGame(size=4):
    mat=[[0 for i in range(size)] for i in range(size)]
    return mat

def add_new_2(mat,size=4):
    r=random.randint(0,size-1)
    c=random.randint(0,size-1)
    while(mat[r][c]!=0):
        r=random.randint(0,size-1)
        c=random.randint(0,size-1)
    mat[r][c]=2
    
def Current_state(mat,size=4):
    for row in range(size):
        for col in range(size):
            if(mat[row][col]==16):
                return "WON"
    for row in range(size):
        for col in range(size):
            if(mat[row][col]==0):
                return "NOT OVER"
            
    for row in range(size=4):
        for col in range(size):
            
            if(col-1>=0):
                left=mat[row][col-1]
                if(left==mat[row][col]):
                    return "NOT OVER"
                
            if(col+1<size):
                right=mat[row][col+1]
                if(right==mat[row][col]):
                    return "NOT OVER"
                
            if(row-1<=0):
                up= mat[row-1][col]
                if(up==mat[row][col]):
                    return "NOT OVER"
            if(row+1<size):
                down=mar[row+1][col]
                if(down==mat[row][col]):
                    return "NOT OVER"

    return "LOSS"


def compress_l(mat,size=4):
    newMat=[[0 for i in range(size)] for j in range(size)]
    for row in range(size):
        i=0
        for col in range(size):
            if(mat[row][col]!=0):
                newMat[row][i]=mat[row][col]
                i+=1
    return newMat

def merge_l(mat,size=4):
    for row in range(size):
        for col in range (size):
            if(col+1<size and (mat[row][col]==mat[row][col+1])):
                mat[row][col]=mat[row][col]+mat[row][col+1]
                mat[row][col+1]=0

def reverse(mat,size=4):
    newMat=[[0 for i in range(size)] for j in range(size)]
    for row in range(size):
        i=0
        for col in range(size-1,-1,-1):
            newMat[row][i]=mat[row][col]
            i+=1
    return newMat

def transpose(mat,size=4):
    newMat=[[0 for i in range(size)] for j in range(size)]
    for row in range (size):
        for col in range(size):
            newMat[row][col]=mat[col][row]
    return newMat

def leftMove(mat,size=4):
    original=mat
    mat=compress_l(mat,size)
    merge_l(mat,size)
    mat=compress_l(mat,size)
    change=False
    for row in range(size):
        for col in range(size):
            if(mat[row][col]!=original[row][col]):
                change=True
    return mat,change

def rightMove(mat,size=4):
    original=mat
    change=False
    mat=reverse(mat,size)
    mat=compress_l(mat,size)
    merge_l(mat,size)
    mat=compress_l(mat,size)
    mat=reverse(mat,size)
    for row in range(size):
        for col in range(size):
            if(mat[row][col]!=original[row][col]):
                change=True
    
    return mat,change

def upMove(mat,size=4):
    original=mat
    change=False
    mat=transpose(mat,size)
    mat=compress_l(mat,size)
    merge_l(mat,size)
    mat=compress_l(mat,size)
    mat=transpose(mat,size)
    for row in range(size):
        for col in range(size):
            if(mat[row][col]!=original[row][col]):
                change=True
    return mat,change

def downMove(mat,size=4):
    original=mat
    change=False
    mat=transpose(mat,size)
    mat=reverse(mat,size)
    mat=compress_l(mat,size)
    merge_l(mat,size)
    mat=compress_l(mat,size)
    mat=reverse(mat,size)
    mat=transpose(mat,size)
    for row in range(size):
        for col in range(size):
            if(mat[row][col]!=original[row][col]):
                change=True
    return mat,change
    
                
