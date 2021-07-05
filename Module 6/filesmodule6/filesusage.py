from os import strerror
import pathlib

# Archivo para copiar documentos de bytes
srcname = input("Source file name? (With Extension): ")
path = pathlib.Path(__file__).parent.__str__()+'/'
try:
    src = open(path + srcname, 'rb')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)	
dstname = input("Destination file name?: ")
try:
    dst = open(path+dstname, 'wb')
except Exception as e:
    print("Cannot create destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0

try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()