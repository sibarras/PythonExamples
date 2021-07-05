from os import strerror
from pathlib import Path
# final lab
class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
	pass

class FileEmpty(StudentsDataException):
	pass

PATH = Path(__file__).parent

fileName = input('Filename: ')
filepath = Path(PATH, fileName).__str__()
try:
    fileRead = open(filepath, 'rt')  #change notes to a variable
    line = fileRead.readline()
    while line != '':
        for char in line:
            print(char, end = '')
        line = fileRead.readline()

    fileRead.close()

except IOError as err:
    print('Problem raised:', strerror(err.errno))