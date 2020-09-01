from os import strerror

# try:
# 	fo = open('newtext.txt', 'wt') # a new file (newtext.txt) is created
# 	for i in range(10):
# 		s = "line #" + str(i+1) + "\n"
# 		for ch in s:
# 			fo.write(ch)
# 	fo.close()
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))

# example for write bits
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))

# enter code that reads bytes from the stream here
