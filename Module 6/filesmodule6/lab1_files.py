from os import strerror
from pathlib import Path

filename = input('File name (with extension): ')  # text.txt is the file.
PATH = Path(__file__).parent.__str__()+'/'
print()

# read the file
try:
    txtfile = open(PATH+filename, 'rt')

    histogramDict = {}

    for ch in txtfile.read():
        for lettr in [chr(i) for i in range(ord('a'), ord('z'))]:
            if ch.lower() == lettr:
                if lettr not in histogramDict.keys():
                    histogramDict[lettr] = 1
                else: histogramDict[lettr] += 1
    txtfile.close()

except IOError as err:
    print('Cannot read destination file : ', strerror(err.errno))
    exit(err.errno)

sortedHist = sorted(histogramDict.items(), key= lambda frec : frec[1], reverse=True)

for lettr, frec in sortedHist:
    print(lettr,' -> ', frec)

try:
    newFile = open(PATH+filename.replace('.txt','.hist'), 'wt')
    for lttr, frec in sortedHist:
        newFile.writelines(lttr+' -> '+str(frec)+'\n')
    newFile.close()

except Exception as e:
    print('Cannot create the file '+filename+'.hist')
    print (e.__str__())
    exit(e.errno)