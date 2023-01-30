from random import randint

def fileFill(file, arr):
    f = open(file, 'w')
    for i in arr:
        f.write(str(i)+'\n')
    f.close()

def showFile(file):
    f = open(file, 'r')
    line = f.readline()
    while (line):
        print(int(line),end=' ')
        line = f.readline()
    f.close()

def mergeSort(fileA):

    fileB = 'B.txt'
    fileC = 'C.txt'
    sB = 2
    sC = 2
    while (sB>=1 and sC>=1):
        s = distribute(fileA, fileB, fileC, sB, sC)
        sB = s[0]
        sC = s[1]
        merge(fileA, fileB, fileC)


def distribute(fileA, fileB, fileC, sB, sC):
    s = []
    fA = open(fileA, 'r')
    fB = open(fileB, 'w')
    fC = open(fileC, 'w')
    wher = 'B'
    sB = 0
    sC = 0
    x = fA.readline()
    fB.write(x)
    line = x
    while (line):
        y = fA.readline()
        line = y
        if not line:  break

        if int(y)<int(x):
            if wher == 'B':
                wher = 'C'
                sB+=1
            elif wher == 'C':
                wher = 'B'
                sC+=1

        if wher == 'B':
            fB.write(y)

        if wher == 'C':
            fC.write(y)

        x = y
    fA.close()
    fB.close()
    fC.close()
    s.append(sB)
    s.append(sC)
    return s

def merge(fileA, fileB, fileC):
    fA = open(fileA,'w')
    fB = open(fileB,'r')
    fC = open(fileC,'r')
    x = fB.readline()
    y = fC.readline()
    lineB = x
    lineC = y
    while (lineB and lineC):
        if (int(x)<=int(y)):
            fA.write(x)
            x = fB.readline()
            lineB = x
        else:
            fA.write(y)
            y = fC.readline()
            lineC = y
    while(lineB):
        fA.write(x)
        x = fB.readline()
        lineB = x
    while(lineC):
        fA.write(y)
        y = fC.readline()
        lineC = y
    fA.close()
    fB.close()
    fC.close()



#main


x = [randint(1,50) for i in range(11)]

fileFill('A.txt', x)
print("До сортировки:")
showFile('A.txt')
print('\n')
mergeSort('A.txt')
print("После сортировки:")
showFile('A.txt')