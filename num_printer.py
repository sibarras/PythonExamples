nums = input('Ingresa los numeros que quieras:')
print_list = ['','','','','']
patron_list = [
    [0b001,0b001,0b001,0b001,0b001],
    [0b111,0b001,0b111,0b100,0b111],
    [0b111,0b001,0b111,0b001,0b111],
    [0b101,0b101,0b111,0b001,0b001],
    [0b111,0b100,0b111,0b001,0b111],
    [0b111,0b100,0b111,0b101,0b111],
    [0b111,0b001,0b001,0b001,0b001],
    [0b111,0b101,0b111,0b101,0b111],
    [0b111,0b101,0b111,0b001,0b111],
    [0b111,0b101,0b101,0b101,0b111]
]

def code_num(num):
    num = int(num)
    num = (num-1 if num!=0 else 9)
    current_patron = patron_list[num]
    for i, row_patron in enumerate(current_patron):
        binary_patron = bin(row_patron)[2:]
        while len(binary_patron) < 3:
            binary_patron = '0'+binary_patron
        for flag in binary_patron:
            print_list[i] += ('#' if flag=='1' else ' ')
        print_list[i] += ' '

def print_patron(print_list):
    for row_str in print_list:
        print(row_str)

for num in nums:
    code_num(num)
print_patron(print_list)
