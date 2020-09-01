from os import strerror
# final lab
class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
	pass

class FileEmpty(StudentsDataException):
	pass

PATH = '/Users/Samuel/Documents/python/filesmodule6/lastlab_mod6.py/'

fileName = input('Filename: ')
print()

try:
    fileRead = open(PATH+'notes.txt', 'rt')  #change notes to a variable
    line = fileRead.readline()
    while line != '':
        for char in line:
            print(char, end = '')
        line = fileRead.readline()

    fileRead.close()

except IOError as err:
    print('Problem raised:', strerror(err.errno))